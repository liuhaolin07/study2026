# -*- coding: utf-8 -*-
"""把 Algorithms 仓库自有的 md 文档转成站点 HTML（site/docs/），并复制模板代码。
输出 site/data/repo_docs.json 供 gen_data.py 合入 data.js。"""
import os, re, json, shutil, hashlib

ROOT = r"D:\File\OneDrive\Desktop\code\Algorithms"
SITE = os.path.join(ROOT, "site")
DOCS = os.path.join(SITE, "docs")
OUT_JSON = os.path.join(SITE, "data", "repo_docs.json")

# ---------------- Markdown -> HTML ----------------
KEYWORDS = r"\b(int|long|double|float|char|bool|void|auto|const|constexpr|static|return|if|else|for|while|do|break|continue|using|namespace|struct|class|public|private|template|typename|new|delete|sizeof|switch|case|default|true|false|nullptr|vector|string|pair|map|set|unordered_map|unordered_set|queue|stack|priority_queue|deque|array|sort|lower_bound|upper_bound|max|min|abs|swap|push_back|pop_back|size|begin|end|first|second|make_pair|typedef|unsigned|inline|mutable|explicit|operator|this|virtual|override|friend|enum|union|goto|try|catch|throw|static_cast|dynamic_cast|cin|cout|endl|ios|sync_with_stdio|tie)\b"

def hl_code(code):
    t = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"(//.*?$)", r'<span class="c">\1</span>', t, flags=re.M)
    t = re.sub(r"(/\*.*?\*/)", r'<span class="c">\1</span>', t, flags=re.S)
    t = re.sub(r'("(?:[^"\\]|\\.)*")', r'<span class="s">\g<0></span>', t)
    t = re.sub(r"'(?:[^'\\]|\\.|&(?:amp|lt|gt|quot|#39);)'", r'<span class="s">\g<0></span>', t)
    t = re.sub(KEYWORDS, r'<span class="k">\1</span>', t)
    t = re.sub(r"\b(0x[0-9a-fA-F]+|\d+\.?\d*(?:e[+-]?\d+)?U?L{0,2})\b", r'<span class="n">\1</span>', t)
    return t

def inline_md(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*\s][^*]*)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"<a href=\"\2\" target=\"_blank\" rel=\"noopener\">\1</a>", s)
    return s

def md_table_rows(lines):
    cells = [inline_md(c.strip()) for c in lines.strip().strip("|").split("|")]
    return cells

def md2html(md):
    out, i, lines = [], 0, md.split("\n")
    list_stack = []  # "ul"/"ol"
    para = []

    def flush_para():
        if para:
            out.append("<p>" + " ".join(para) + "</p>"); para.clear()
    def close_lists():
        while list_stack:
            out.append(f"</{list_stack.pop()}>")

    while i < len(lines):
        ln = lines[i]
        # 代码块
        if ln.startswith("```"):
            flush_para(); close_lists()
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i]); i += 1
            out.append(f'<pre class="code">{hl_code(chr(10).join(code))}</pre>')
            i += 1; continue
        # 表格
        if ln.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            flush_para(); close_lists()
            head = md_table_rows(ln)
            i += 2
            body = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                body.append(md_table_rows(lines[i])); i += 1
            out.append('<div class="tblwrap"><table><thead><tr>' +
                       "".join(f"<th>{c}</th>" for c in head) + "</tr></thead><tbody>" +
                       "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) for row in body) +
                       "</tbody></table></div>")
            continue
        # 标题
        m = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if m:
            flush_para(); close_lists()
            lvl = min(len(m.group(1)) + 1, 5)
            out.append(f"<h{lvl}>{inline_md(m.group(2))}</h{lvl}>")
            i += 1; continue
        # 分隔线
        if re.match(r"^\s*([-*_])\1{2,}\s*$", ln) or re.match(r"^---+\s*$", ln):
            flush_para(); close_lists(); out.append("<hr>")
            i += 1; continue
        # 引用
        if ln.startswith(">"):
            flush_para(); close_lists()
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(inline_md(lines[i].lstrip("> ").rstrip())); i += 1
            out.append("<blockquote>" + "<br>".join(q for q in quote if q) + "</blockquote>")
            continue
        # 列表
        m = re.match(r"^(\s*)([-*+])\s+(.*)$", ln)
        m2 = re.match(r"^(\s*)(\d+)[.、)]\s+(.*)$", ln)
        if m or m2:
            flush_para()
            ordered = bool(m2)
            want = "ol" if ordered else "ul"
            if not list_stack or list_stack[-1] != want:
                close_lists()
                out.append(f"<{want}>"); list_stack.append(want)
            content = (m2 or m).group(3)
            cb = re.match(r"^\[( |x|X)\]\s+(.*)$", content)
            if cb:
                box = "☑" if cb.group(1).lower() == "x" else "☐"
                content = f'<span class="cb">{box}</span> ' + cb.group(2)
            else:
                content = inline_md(content)
            out.append(f"<li>{content}</li>")
            i += 1; continue
        # 空行
        if not ln.strip():
            flush_para(); close_lists()
            i += 1; continue
        para.append(inline_md(ln.rstrip()))
        i += 1
    flush_para(); close_lists()
    return "\n".join(out)

TPL = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · 算法训练站</title>
<script>
(function () {{
  var t = "light";
  try {{ t = localStorage.getItem("algoTrain.theme") || "light"; }} catch (e) {{ }}
  document.documentElement.setAttribute("data-theme", t);
}})();
</script>
<style>
:root {{ color-scheme: dark; --bg:#0a0e14; --bg2:#10151d; --bd:#232d3d; --fg:#e8eef5; --fg2:#8b98a9; --acc:#4da3ff; --cyan:#4fd6e0; }}
html[data-theme="light"] {{ color-scheme: light;
  --bg:#f2f5fa; --bg2:#ffffff; --bd:#dfe6f1; --fg:#1c2739; --fg2:#4f6076; --acc:#2f7de1; --cyan:#0995b5;
  --code-bg:#f6f8fc; --code-bd:#e2e9f3; --thead:#f0f4fa; --quote:#3d4f68; }}
html[data-theme="light"] pre.code .k {{ color:#9333ea; }}
html[data-theme="light"] pre.code .s {{ color:#127a45; }}
html[data-theme="light"] pre.code .c {{ color:#93a1b5; }}
html[data-theme="light"] pre.code .n {{ color:#c0500c; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ font-family:-apple-system,"Segoe UI","Microsoft YaHei","PingFang SC",sans-serif;
  background:var(--bg); color:var(--fg); font-size:15px; line-height:1.75; padding:28px 16px 60px; }}
.wrap {{ max-width:860px; margin:0 auto; }}
.back {{ display:inline-block; margin-bottom:18px; font-size:13px; color:var(--fg2);
  text-decoration:none; border:1px solid var(--bd); padding:5px 14px; border-radius:8px; }}
.back:hover {{ color:var(--acc); border-color:var(--acc); }}
h2 {{ font-size:22px; margin:8px 0 18px; padding-bottom:12px; border-bottom:1px solid var(--bd); }}
h3 {{ font-size:17.5px; margin:26px 0 10px; color:#cfe6ff; }}
h4 {{ font-size:15.5px; margin:20px 0 8px; color:var(--cyan); }}
h5 {{ font-size:14px; margin:14px 0 6px; color:var(--fg2); }}
p {{ margin:9px 0; }}
a {{ color:var(--acc); }}
ul,ol {{ margin:8px 0 8px 24px; }}
li {{ margin:4px 0; }}
code {{ font-family:Consolas,monospace; background:var(--code-bg,#1a2331); border:1px solid var(--bd);
  border-radius:5px; padding:1px 6px; font-size:13px; color:var(--cyan); }}
pre.code {{ font-family:Consolas,"Cascadia Code",monospace; background:var(--code-bg,#0d131c); border:1px solid var(--bd);
  border-radius:10px; padding:16px 18px; overflow-x:auto; font-size:13px; line-height:1.6; margin:12px 0; }}
pre.code .k {{ color:#c792ea; }} pre.code .s {{ color:#7ee0a3; }}
pre.code .c {{ color:#5d6b7d; font-style:italic; }} pre.code .n {{ color:#f78c6c; }}
blockquote {{ border-left:3px solid var(--acc); background:rgba(77,163,255,.06);
  padding:10px 16px; border-radius:0 8px 8px 0; margin:12px 0; color:var(--quote,#c7d5e4); }}
table {{ border-collapse:collapse; width:100%; margin:12px 0; font-size:13.5px; }}
th,td {{ border:1px solid var(--bd); padding:7px 11px; text-align:left; vertical-align:top; }}
th {{ background:var(--thead,#151d29); color:var(--acc); }}
tr:nth-child(even) td {{ background:rgba(128,128,128,.05); }}
.tblwrap {{ overflow-x:auto; }}
hr {{ border:0; border-top:1px solid var(--bd); margin:20px 0; }}
.cb {{ color:var(--cyan); }}
.meta {{ color:var(--fg2); font-size:12.5px; margin-bottom:14px; }}
</style></head><body><div class="wrap">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px">
<a class="back" href="javascript:history.back()">← 返回训练站</a>
<button id="themeBtn" style="cursor:pointer;font-size:13px;color:var(--fg2);background:var(--bg2);border:1px solid var(--bd);padding:5px 14px;border-radius:8px">🌙 深色</button></div>
<script>
(function () {{
  var b = document.getElementById('themeBtn');
  function lb() {{ b.textContent = document.documentElement.getAttribute('data-theme') === 'light' ? '🌙 深色' : '☀️ 浅色'; }}
  b.onclick = function () {{
    var n = document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', n);
    try {{ localStorage.setItem('algoTrain.theme', n); }} catch (e) {{ }}
    lb();
  }};
  lb();
}})();
</script>
{body}
</div></body></html>"""

def convert_file(md_path, out_rel, meta=""):
    md = open(md_path, encoding="utf-8").read()
    body = md2html(md)
    m = re.match(r"^#\s+(.+)$", md, re.M)
    title = m.group(1).strip() if m else os.path.basename(md_path)
    html = TPL.format(title=title, body=body + (f'<p class="meta">{meta}</p>' if meta else ""))
    outp = os.path.join(DOCS, *out_rel.split("/"))
    os.makedirs(os.path.dirname(outp), exist_ok=True)
    with open(outp, "w", encoding="utf-8") as f:
        f.write(html)
    return {"title": title, "file": f"docs/{out_rel}"}

# ---------------- 采集 ----------------
def main():
    if os.path.exists(DOCS):
        shutil.rmtree(DOCS)
    index = {"solutions": [], "topics": [], "notes": [], "templates": [], "plan": {}, "icpcGuide": ""}

    TOPIC_NAMES = {
        "00-language": "C++ 语言基础", "01-stl": "数据结构实现 & STL", "02-basics": "基础算法",
        "03-search": "搜索", "04-data-structure": "数据结构", "05-dp": "动态规划",
        "06-graph": "图论", "07-math": "数学", "08-string": "字符串",
        "09-geometry": "计算几何", "10-constructive-greedy": "构造 & 思维", "11-drill-40day": "40 天集训",
    }
    td_root = os.path.join(ROOT, "题单")
    # 专题题单 README + 题解
    for topic in sorted(os.listdir(td_root)):
        tdir = os.path.join(td_root, topic)
        if not os.path.isdir(tdir) or topic.startswith("."):
            continue
        readme = None
        if os.path.exists(os.path.join(tdir, "README.md")):
            readme = convert_file(os.path.join(tdir, "README.md"), f"topics/{topic}.html")
        sols = []
        for fn in sorted(os.listdir(tdir)):
            m = re.match(r"^(P\d+|CF\d+[A-Z]?)_?(.*?)\.md$", fn)
            if not m or fn == "README.md":
                continue
            pid, name = m.group(1), m.group(2)
            doc = convert_file(os.path.join(tdir, fn), f"solutions/{topic}/{fn[:-3]}.html")
            doc["pid"] = pid
            doc["topic"] = topic
            sols.append(doc)
        index["topics"].append({
            "id": topic, "name": TOPIC_NAMES.get(topic, topic),
            "readme": readme, "solutions": sols,
        })
        index["solutions"].extend(sols)
    # 题单总览
    index["tdIndex"] = convert_file(os.path.join(td_root, "README.md"), "题单总览.html")
    # 学习路径（完整文档 + 一/二节片段）
    plan_doc = convert_file(os.path.join(ROOT, "学习路径.md"), "学习路径.html")
    plan_md = open(os.path.join(ROOT, "学习路径.md"), encoding="utf-8").read()
    m = re.search(r"(## 一、.*?)## 三、", plan_md, re.S)
    index["plan"] = {"doc": plan_doc, "fragment": md2html(m.group(1)) if m else ""}
    # 仓库总览
    index["repoIndex"] = convert_file(os.path.join(ROOT, "README.md"), "仓库总览.html")
    # 笔记
    note_root = os.path.join(ROOT, "笔记")
    NOTE_NAMES = {
        "checklist.md": "知识点清单", "redo-list.md": "重做清单", "易错点与调试.md": "易错点与调试",
        "比赛策略.md": "比赛策略", "资源导航.md": "资源导航", "README.md": "笔记索引",
    }
    for fn in sorted(os.listdir(note_root)):
        p = os.path.join(note_root, fn)
        if fn.endswith(".md"):
            d = convert_file(p, f"notes/{fn[:-3]}.html")
            d["name"] = NOTE_NAMES.get(fn, fn[:-3])
            index["notes"].append(d)
    su = os.path.join(note_root, "速查")
    for fn in sorted(os.listdir(su)):
        if fn.endswith(".md"):
            d = convert_file(os.path.join(su, fn), f"notes/速查-{fn[:-3]}.html")
            d["name"] = "速查 · " + fn[:-3].split("-", 1)[-1]
            index["notes"].append(d)
    # 模板：指南文档 + 代码复制
    tpl_root = os.path.join(ROOT, "模板")
    TPL_DOCS = {"README.md": "模板总览", "QUICKSTART.md": "快速上手", "STANDARDS.md": "模板规范", "TEMPLATE_GUIDE.md": "模板指南"}
    for fn, name in TPL_DOCS.items():
        p = os.path.join(tpl_root, fn)
        if os.path.exists(p):
            d = convert_file(p, f"templates/{fn[:-3]}.html")
            d["name"] = name
            index["templates"].append(d)
    code_dst = os.path.join(SITE, "assets", "mycode")
    if os.path.exists(code_dst):
        shutil.rmtree(code_dst)
    shutil.copytree(os.path.join(tpl_root, "XCPC_Templates"), os.path.join(code_dst, "XCPC_Templates"))
    shutil.copy2(os.path.join(tpl_root, "contest.cpp"), os.path.join(code_dst, "contest.cpp"))
    # 模板文件清单
    headers = []
    for root, _, files in os.walk(os.path.join(code_dst, "XCPC_Templates")):
        for f in files:
            if f.endswith((".h", ".hpp", ".cpp")):
                rel = os.path.relpath(os.path.join(root, f), SITE).replace("\\", "/")
                headers.append({"n": f, "p": rel, "g": os.path.basename(root)})
    index["tplFiles"] = sorted(headers, key=lambda x: x["p"])
    # ICPC 指南
    icpc_md = open(os.path.join(ROOT, "比赛", "icpc", "README.md"), encoding="utf-8").read()
    index["icpcGuide"] = convert_file(os.path.join(ROOT, "比赛", "icpc", "README.md"), "icpc-vp指南.html")
    # 解析渠道表 -> 平台链接
    PLAT_URL = {"Codeforces Gym": "https://codeforces.com/gyms", "牛客网": "https://ac.nowcoder.com/acm/contest",
                "ICPC 官方 (icpc.global)": "https://icpc.global/worldfinals/problems", "QOJ / 洛谷": "https://qoj.ac"}
    plats = []
    for ln in icpc_md.split("\n"):
        if ln.strip().startswith("|") and not re.match(r"^\s*\|[\s:|-]+\|\s*$", ln):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cells) == 2 and cells[0] not in ("渠道", "---", ":--"):
                plats.append({"n": inline_md(cells[0]), "u": PLAT_URL.get(cells[0], ""), "use": inline_md(cells[1])})
    index["icpcPlatforms"] = plats[:4]

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
    n_sol = len(index["solutions"])
    print(f"docs: {n_sol} solutions, {len(index['topics'])} topics, {len(index['notes'])} notes, "
          f"{len(index['templates'])} tpl docs, {len(index['tplFiles'])} template files, icpc ok")

if __name__ == "__main__":
    main()
