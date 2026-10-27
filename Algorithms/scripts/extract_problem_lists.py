# -*- coding: utf-8 -*-
"""从题单 PDF 中提取 章节 -> 题目(名称+OJ链接) 结构，输出 JSON。"""
import pymupdf, json, re, sys, os

SRC = r"D:\File\OneDrive\Desktop\code\Algorithms\参考\2026题单"
OUT = r"D:\File\OneDrive\Desktop\code\Algorithms\site\data\problems_raw.json"

PDFS = [
    ("cpp", "1. 《算法竞赛-C++编程课》题目清单.pdf", "C++ 编程课", "语言基础"),
    ("ds", "2.《算法竞赛-数据结构&算法与STL》题目清单(1).pdf", "数据结构与STL", "数据结构"),
    ("basic", "3.《算法竞赛-算法基础篇》题目清单.pdf", "算法基础篇", "算法基础"),
    ("consolidate", "4.《算法竞赛 - 算法巩固篇》题目清单.pdf", "算法巩固篇", "算法巩固"),
    ("advanced", "5.《算法竞赛-算法提高篇》题目清单.pdf", "算法提高篇", "算法提高"),
]

chapter_re = re.compile(r"^(第\s*[\d零一二三四五六七八九十百]+\s*[章周节讲])")
day_re = re.compile(r"^(Day\s*\d+)\s*$", re.I)

def extract(pdf_path, key):
    doc = pymupdf.open(pdf_path)
    # basic/advanced：无链接的编号行是知识点小节；cpp：是"非OJ"真题
    use_sections = key in ("basic", "advanced")
    chapters = []   # [{title, sections:[{title, problems:[...]}]}]
    cur_sec = None
    week = ""
    def new_chapter(title):
        nonlocal cur_sec
        cur_sec = {"title": None, "problems": []}
        chapters.append({"title": title, "sections": [cur_sec]})
    for page in doc:
        # 收集链接，按出现顺序
        links = []
        for l in page.get_links():
            uri = l.get("uri")
            if uri and l.get("kind") == pymupdf.LINK_URI:
                links.append((l["from"].y0, l["from"].x0, uri))
        # 用 dict 模式取文本行
        d = page.get_text("dict")
        for block in d["blocks"]:
            if block.get("type") != 0:
                continue
            for line in block["lines"]:
                text = "".join(s["text"] for s in line["spans"]).strip()
                text = text.replace("\u200b", "").replace("\ufeff", "").strip()
                if not text:
                    continue
                bbox = pymupdf.Rect(line["bbox"])
                # 跳过页眉页脚类噪声
                if re.match(r"^\d+$", text):
                    continue
                # 找与该行相交的链接
                matched = None
                for (y0, x0, uri) in links:
                    if abs(y0 - bbox.y0) < 4 and bbox.x0 - 2 <= x0 <= bbox.x1 + 5:
                        matched = uri
                        break
                bare = re.sub(r"^\d+[.、]\s*", "", text)  # 去掉 "1. " 前缀
                m = chapter_re.match(bare)
                is_chapter = bool(m) and not matched and len(bare) <= 30
                if is_chapter:
                    week = m.group(1).replace(" ", "")
                    new_chapter(bare.replace(" ", ""))
                    continue
                if day_re.match(text) and not matched:
                    # 巩固篇：Day 分组，拼上周数
                    new_chapter(f"{week} {text.upper()}" if week else text.upper())
                    continue
                numbered = re.match(r"^\d+[.、)\s]", text)
                name = re.sub(r"^\d+[.、)\s]*", "", text).strip()
                if matched:
                    if cur_sec is not None:
                        cur_sec["problems"].append({"name": name, "url": matched})
                elif numbered and use_sections and cur_sec is not None:
                    # 知识点小节标题
                    cur_sec = {"title": name, "problems": []}
                    chapters[-1]["sections"].append(cur_sec)
                elif numbered and cur_sec is not None:
                    # 无链接真题（如"非OJ"题目）
                    cur_sec["problems"].append({"name": name, "url": None})
    # 清理空章节/空小节
    out = []
    for c in chapters:
        c["sections"] = [s for s in c["sections"] if s["problems"]]
        if c["sections"]:
            out.append(c)
    return out

OJ_MAP = [
    ("luogu.com.cn", "洛谷"),
    ("nowcoder.com", "牛客"),
    ("leetcode.cn", "力扣"),
    ("loj.ac", "LOJ"),
    ("ybt.ssoier.cn", "一本通"),
    ("vjudge.net", "VJudge"),
    ("biteketang.com", "课堂"),
]
def oj_of(url):
    if not url:
        return None
    for host, name in OJ_MAP:
        if host in url:
            return name
    return "其他"

def main():
    result = {}
    pid = 0
    for key, fname, display, stage in PDFS:
        path = os.path.join(SRC, fname)
        chs = extract(path, key)
        total = 0
        for ci, c in enumerate(chs):
            for si, s in enumerate(c["sections"]):
                for pi, p in enumerate(s["problems"]):
                    pid += 1
                    p["id"] = f"{key}-{ci}-{si}-{pi}"
                    p["oj"] = oj_of(p["url"])
                    total += 1
        result[key] = {
            "display": display, "stage": stage, "file": fname,
            "chapters": chs, "total": total,
        }
        print(f"{key}: {len(chs)} chapters, {total} problems")
        for c in chs[:2]:
            print("   ", c["title"], "| sections:", len(c["sections"]))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print("saved ->", OUT, "| total problems:", pid)

if __name__ == "__main__":
    main()
