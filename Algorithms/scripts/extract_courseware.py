# -*- coding: utf-8 -*-
"""从课件 PDF 的目录（书签）生成知识树数据。

输出 site/assets/js/courseware.js：
  window.COURSEWARE = {
    "cpp-0": {
      files: [{path, pages}],
      toc: [{l,t,p,f}],
      points: [{t,p,f,end,ids:[problemId]}],
      problems: {problemId: {p,f,t}},
      sections: {sectionIndex: {p,f,t}}
    }, ...
  }

知识点（points）的取法：
- 章节有具名 section（basic/advanced）→ 直接用 section，并匹配 PDF 目录页码；
- 无具名 section（cpp/ds/consolidate）→ 用 PDF 目录的下一层条目；
  consolidate 先定位 DayNN，再取其下题目条目。
- 题目按 PDF 页码落到对应知识点的页码范围里。
"""
import json
import os
import re
import sys
import unicodedata
from difflib import SequenceMatcher

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
OUT = os.path.join(SITE, "assets", "js", "courseware.js")

GENERIC = {"练习题", "练习", "模板题", "例题", "阶段小结", "小结", "引入", "总结", "习题", "作业"}


def load_data():
    s = open(os.path.join(SITE, "assets", "js", "data.js"), encoding="utf-8").read()
    m = re.search(r"window\.SITE_DATA\s*=\s*(\{.*\})\s*;?\s*$", s, re.S)
    if not m:
        raise SystemExit("data.js 解析失败")
    return json.loads(m.group(1))


def norm(s):
    s = unicodedata.normalize("NFKC", s or "")
    s = s.replace("【模板】", "").replace("（", "(").replace("）", ")")
    s = re.sub(r"^\s*第\s*[0-9一二三四五六七八九十百]+\s*[章节讲周]\s*", "", s)
    s = re.sub(r"^\s*\d+(\.\d+)*[\.、\s]*", "", s)
    s = re.sub(r"^(P\d+|B\d+|CF\d+[A-Z]?|AT_\d+|SP\d+|T\d+)\s*", "", s, flags=re.I)
    s = re.sub(r'[\s\-—_·:：,，.。()（）\[\]【】<>《》"“”\'’]+', "", s)
    return s.lower()


def score(a, b):
    """a=TOC 标题, b=section/题目名，越大越像"""
    if not a or not b:
        return 0
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return 0
    if na == nb:
        return 1.0
    if len(nb) >= 3 and (nb in na or na in nb):
        return 0.86 + min(len(na), len(nb)) / max(len(na), len(nb)) * 0.1
    r = SequenceMatcher(None, na, nb).ratio()
    return r if r >= 0.72 else 0


def read_pdfs(paths):
    files, toc = [], []
    for fi, rel in enumerate(paths):
        p = os.path.join(SITE, rel)
        if not os.path.exists(p):
            print("  ! missing", rel)
            continue
        doc = pymupdf.open(p)
        files.append({"path": rel.replace("\\", "/"), "pages": doc.page_count})
        for lvl, title, page in doc.get_toc(simple=True):
            title = unicodedata.normalize("NFKC", title or "").strip()
            if title and page and page > 0:
                toc.append({"l": int(lvl), "t": title, "p": int(page), "f": fi})
        doc.close()
    return files, toc


def best_match(toc, name, allow_generic=True):
    best, bs = None, 0
    for e in toc:
        if not allow_generic and norm(e["t"]) in {norm(x) for x in GENERIC}:
            continue
        sc = score(e["t"], name)
        if sc > bs:
            best, bs = e, sc
    return best if bs >= 0.72 else None


def descendants(toc, idx):
    root = toc[idx]
    out = []
    for e in toc[idx + 1:]:
        if e["l"] <= root["l"]:
            break
        out.append(e)
    return out


def flatten_points(toc, chapter_title, course_key):
    """无具名 section 时，从 PDF 目录里选一层做知识点"""
    if not toc:
        return []
    # consolidate：先定位 DayNN，再取题目层
    if course_key == "consolidate":
        day = None
        m = re.search(r"(DAY\s*\d+)", chapter_title, re.I)
        if m:
            target = norm(m.group(1))
            for i, e in enumerate(toc):
                if norm(e["t"]).startswith(target) or target in norm(e["t"]):
                    day = i
                    break
        if day is not None:
            kids = [e for e in descendants(toc, day) if e["l"] == toc[day]["l"] + 1]
            if kids:
                return kids
    # 找章节根条目（必须明确是“第N章”，否则会把某一节误当整章）
    root = None
    for i, e in enumerate(toc):
        sc = score(e["t"], chapter_title)
        if sc >= 0.95 or ("章" in e["t"] and sc >= 0.78):
            root = i
            break
    if root is not None:
        kids = [e for e in descendants(toc, root) if e["l"] == toc[root]["l"] + 1]
        if len(kids) >= 2:
            return kids
    # 没有根：取最浅的一层（通常 level 1）
    level = min(e["l"] for e in toc)
    pts = [e for e in toc if e["l"] == level]
    if len(pts) <= 1:
        level += 1
        pts = [e for e in toc if e["l"] == level]
    return pts


def main():
    data = load_data()
    out = {"version": 1, "generatedAt": "", "chapters": {}}
    stats = {"chapters": 0, "points": 0, "problems": 0, "problem_pages": 0, "section_pages": 0}

    for course in data["courses"]:
        ck = course["key"]
        chap_pdfs = data.get("chapPdfs", {}).get(ck, {})
        for ci, ch in enumerate(data["problems"][ck]["chapters"]):
            rels = chap_pdfs.get(str(ci)) or chap_pdfs.get(ci) or []
            if not rels:
                continue
            files, toc = read_pdfs(rels)
            if not toc:
                continue
            key = f"{ck}-{ci}"
            cw = {"files": files, "toc": toc, "points": [], "problems": {}, "sections": {}}
            sections = ch.get("sections", [])
            named = [s for s in sections if (s.get("title") or "").strip()]

            if named:
                # 具名 section → 知识点
                for si, sec in enumerate(sections):
                    st = (sec.get("title") or "").strip()
                    if not st:
                        st = f"第 {si + 1} 部分"
                    hit = best_match(toc, st)
                    cw["sections"][str(si)] = {"t": st, "p": hit["p"] if hit else None,
                                               "f": hit["f"] if hit else None,
                                               "tt": hit["t"] if hit else st}
                    ids = [p["id"] for p in sec.get("problems", [])]
                    cw["points"].append({"t": st, "p": hit["p"] if hit else None,
                                         "f": hit["f"] if hit else None,
                                         "tt": hit["t"] if hit else st, "ids": ids})
                    if hit:
                        stats["section_pages"] += 1
            else:
                # 无具名 section → 从目录取知识点
                pts = flatten_points(toc, ch["title"], ck)
                # 去掉纯“练习题”等，但如果只剩这些就保留
                cleaned = [e for e in pts if norm(e["t"]) not in {norm(x) for x in GENERIC}]
                if len(cleaned) >= 1:
                    pts = cleaned
                all_problems = [p for sec in sections for p in sec.get("problems", [])]
                # 先给每道题找 PDF 目录页
                prob_page = {}
                for p in all_problems:
                    hit = best_match(toc, p["name"], allow_generic=False)
                    if hit:
                        prob_page[p["id"]] = hit
                # 按页码把题分到知识点
                by_file = {}
                for i, e in enumerate(pts):
                    by_file.setdefault(e["f"], []).append((i, e))
                for f, arr in by_file.items():
                    arr.sort(key=lambda x: x[1]["p"])
                    for j, (i, e) in enumerate(arr):
                        nxt = arr[j + 1][1]["p"] if j + 1 < len(arr) else (files[f]["pages"] + 1 if f < len(files) else 10 ** 9)
                        ids = []
                        for p in all_problems:
                            hit = prob_page.get(p["id"])
                            if hit and hit["f"] == f and e["p"] <= hit["p"] < nxt:
                                ids.append(p["id"])
                        cw["points"].append({"t": re.sub(r"^\s*\d+(\.\d+)*[\.、\s]*", "", e["t"]).strip(),
                                             "p": e["p"], "f": f, "tt": e["t"], "ids": ids})
                if not cw["points"]:
                    ids = [p["id"] for p in all_problems]
                    cw["points"].append({"t": "本章题目", "p": None, "f": None, "tt": "", "ids": ids})
                # 没落到任何知识点页码里的题，单独兜底
                assigned = {pid for pt in cw["points"] for pid in pt["ids"]}
                leftover = [p["id"] for p in all_problems if p["id"] not in assigned]
                if leftover:
                    cw["leftover"] = leftover

            # 题目 → PDF 页码（所有题都尝试）
            for sec in sections:
                for p in sec.get("problems", []):
                    hit = best_match(toc, p["name"], allow_generic=False)
                    if hit:
                        cw["problems"][p["id"]] = {"p": hit["p"], "f": hit["f"], "t": hit["t"]}
                        stats["problem_pages"] += 1
                    stats["problems"] += 1

            stats["chapters"] += 1
            stats["points"] += len(cw["points"])
            out["chapters"][key] = cw

    out["generatedAt"] = __import__("datetime").datetime.now().isoformat(timespec="seconds")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("/* 由 scripts/extract_courseware.py 生成，勿手改 */\n")
        f.write("window.COURSEWARE = ")
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";\n")
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    print("OUT:", OUT, os.path.getsize(OUT) // 1024, "KB")


if __name__ == "__main__":
    main()
