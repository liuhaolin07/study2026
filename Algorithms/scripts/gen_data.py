# -*- coding: utf-8 -*-
"""生成 site/assets/js/data.js：题库 + 学习路线 + 课件清单 + 真题清单。"""
import json, os, re

SITE = r"D:\File\OneDrive\Desktop\code\Algorithms\site"
ASSETS = os.path.join(SITE, "assets")

# ---------- 学习路线（来自 参考/2026题单/path.docx） ----------
ROADMAP = {
    "stages": [
        {
            "id": "intro", "title": "入门阶段：语言 + 基础算法",
            "goal": "能独立写题、调试、理解复杂度。推荐语言 C++（竞赛主流）。",
            "courses": ["cpp", "basic"],
            "items": [
                {"t": "基础语法", "d": ["输入输出", "数组 / 字符串", "函数", "STL：vector / queue / stack / set / map / priority_queue"]},
                {"t": "时间复杂度", "d": ["必须真正理解 O(1)、O(log n)、O(n)、O(n log n)、O(n²) —— 这是后面所有优化的核心"]},
                {"t": "基础算法（练到看题能秒想到）", "d": ["排序", "二分", "前缀和", "差分", "双指针", "滑动窗口", "模拟", "贪心", "枚举"]},
            ],
        },
        {
            "id": "ds", "title": "数据结构阶段",
            "goal": "能处理中大型题目。",
            "courses": ["ds", "basic", "advanced"],
            "items": [
                {"t": "栈与队列", "d": ["单调栈", "单调队列"]},
                {"t": "链表（简单了解）", "d": ["竞赛里用得不多，但思想重要"]},
                {"t": "堆（优先队列）", "d": ["TopK", "贪心优化"]},
                {"t": "并查集（非常高频）", "d": ["连通块", "Kruskal"]},
                {"t": "树状数组", "d": ["单点修改", "区间查询"]},
                {"t": "线段树（重要分水岭）", "d": ["区间查询", "区间修改", "lazy tag"]},
            ],
        },
        {
            "id": "graph", "title": "图论阶段（核心）",
            "goal": "很多竞赛真正开始“拉开差距”的地方。",
            "courses": ["basic"],
            "items": [
                {"t": "图的基础", "d": ["邻接表", "DFS", "BFS"]},
                {"t": "最短路（按顺序学）", "d": ["Dijkstra", "Floyd", "Bellman-Ford（了解）"]},
                {"t": "最小生成树", "d": ["Kruskal", "Prim"]},
                {"t": "拓扑排序", "d": []},
                {"t": "强连通分量", "d": ["Tarjan"]},
                {"t": "二分图", "d": ["染色", "匈牙利算法"]},
            ],
        },
        {
            "id": "dp", "title": "动态规划（最难长期模块）",
            "goal": "很多人真正卡死的地方，学习顺序非常关键。",
            "courses": ["basic", "advanced"],
            "items": [
                {"t": "第一阶段", "d": ["线性 DP", "背包 DP", "LIS"]},
                {"t": "第二阶段", "d": ["区间 DP", "状压 DP", "树形 DP"]},
                {"t": "第三阶段", "d": ["数位 DP", "DP 优化"]},
            ],
        },
        {
            "id": "math", "title": "数学部分",
            "goal": "竞赛后期必须学。",
            "courses": ["basic"],
            "items": [
                {"t": "基础数论", "d": ["gcd", "快速幂", "素数筛", "逆元", "同余"]},
                {"t": "组合数学", "d": ["排列组合", "容斥"]},
                {"t": "博弈论（可后学）", "d": []},
            ],
        },
        {
            "id": "adv", "title": "高级阶段",
            "goal": "当你能稳定做 Codeforces Div2 C/D、洛谷普及+/提高题，再进入。",
            "courses": ["advanced"],
            "items": [
                {"t": "高级数据结构", "d": ["平衡树", "可持久化线段树", "树链剖分"]},
                {"t": "高级图论", "d": ["网络流", "最小费用流"]},
                {"t": "字符串", "d": ["KMP", "Trie", "AC 自动机", "后缀数组"]},
            ],
        },
    ],
    "rhythm": [
        {"t": "前 3 个月", "d": "主攻：基础算法、STL、DFS/BFS、二分、贪心"},
        {"t": "3~6 个月", "d": "进入：DP、图论、并查集、线段树"},
        {"t": "6 个月后", "d": "开始：大量比赛、补弱项、学高级算法"},
    ],
    "growth": "学一个算法 → 刷专题 20~50 题 → 参加比赛 → 被虐 → 补知识 → 再比赛。算法竞赛真正提升最快的不是“看懂题解”，而是“在比赛压力下独立思考”。",
    "method": {
        "avoid": ["只看题解", "不复盘", "不整理模板", "不总结错误"],
        "record": ["为什么想到这个算法", "为什么自己没想到", "复杂度为什么对", "有没有更优写法"],
    },
    "levels": [
        {"t": "入门", "d": "CF Div3"}, {"t": "中级", "d": "CF Div2 C"},
        {"t": "较强", "d": "CF Div2 D/E"}, {"t": "强", "d": "ICPC 银牌"},
        {"t": "很强", "d": "NOI / AGC"},
    ],
    "platforms": {
        "国内": [
            {"n": "洛谷", "u": "https://www.luogu.com.cn"},
            {"n": "牛客", "u": "https://ac.nowcoder.com"},
            {"n": "AcWing", "u": "https://www.acwing.com"},
        ],
        "国际": [
            {"n": "Codeforces", "u": "https://codeforces.com"},
            {"n": "AtCoder", "u": "https://atcoder.jp"},
            {"n": "LeetCode", "u": "https://leetcode.cn"},
        ],
        "工具": [
            {"n": "OI Wiki", "u": "https://oi-wiki.org"},
            {"n": "XCPC 学习路线", "u": "https://github.com/hh2048/XCPC"},
        ],
    },
    "books": ["《算法竞赛入门经典》", "《挑战程序设计竞赛》"],
    "images": [
        {"n": "语法基础篇", "p": "assets/roadmap/1. 语法基础篇.png"},
        {"n": "数据结构与STL", "p": "assets/roadmap/2. 数据结构与STL.png"},
        {"n": "算法基础篇", "p": "assets/roadmap/3. 算法基础篇.png"},
        {"n": "算法进阶篇", "p": "assets/roadmap/4. 算法进阶篇.png"},
    ],
}

# ---------- 课程定义 ----------
COURSES_META = [
    {"key": "cpp", "name": "C++ 编程课", "stage": "语法基础", "dir": "courses/cpp",
     "desc": "C++ 入门到进阶语法：输入输出、分支循环、数组、string、函数递归、位运算、结构体类、指针"},
    {"key": "ds", "name": "数据结构与STL", "stage": "数据结构", "dir": "courses/ds",
     "desc": "顺序表/链表/栈/队列/树/二叉树/堆/红黑树(set/map)/哈希表/排序，配套课堂代码"},
    {"key": "basic", "name": "算法基础篇", "stage": "算法基础", "dir": "courses/basic",
     "desc": "基础算法、搜索、数据结构、动态规划、图论基础、数学（数论/组合/线代/博弈）"},
    {"key": "consolidate", "name": "算法巩固篇", "stage": "综合训练", "dir": "courses/consolidate",
     "desc": "40 天集训：每天 4 题、难度递增，共 160+ 题综合巩固"},
    {"key": "advanced", "name": "算法提高篇", "stage": "算法提高", "dir": "courses/advanced",
     "desc": "线段树/树状数组/ST表/树形DP/状压DP/数位DP/搜索进阶/LCA/图论进阶/字符串(KMP/Manacher)"},
]

CN_NUM = {"零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}

def cn_to_int(s):
    if s.isdigit():
        return int(s)
    if s in CN_NUM:
        return CN_NUM[s]
    m = re.match(r"^十(\d|[零一二三四五六七八九])?$", s)
    if m:
        return 10 + (CN_NUM.get(m.group(1), 0) if m.group(1) else 0)
    return None

def chap_key(title):
    """'第1章...'/'第01节...'/'第1周 DAY01' -> (unit, num)"""
    m = re.match(r"^第\s*(\d+|[零一二三四五六七八九十]+)\s*([章周节讲])", title)
    if not m:
        return None
    n = cn_to_int(m.group(1))
    return (m.group(2), n) if n is not None else None

def rel_files(base):
    """列出目录下所有文件（相对 site 根的路径），带大小。"""
    out = []
    for root, _, files in os.walk(base):
        for f in files:
            p = os.path.join(root, f)
            rel = os.path.relpath(p, SITE).replace("\\", "/")
            out.append({"p": rel, "n": f, "size": os.path.getsize(p)})
    return out

def natural_key(name):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", name)]

def main():
    problems = json.load(open(os.path.join(SITE, "data", "problems_raw.json"), encoding="utf-8"))

    # 每门课：课件文件清单 + 章节->课件关联
    course_files = {}
    chap_pdfs = {}
    for meta in COURSES_META:
        base = os.path.join(ASSETS, *meta["dir"].split("/"))
        pdfs = [f for f in rel_files(base) if f["p"].lower().endswith(".pdf")]
        pdfs.sort(key=lambda f: natural_key(f["n"]))
        course_files[meta["key"]] = pdfs
        # 章节关联
        mapping = {}
        for ci, ch in enumerate(problems[meta["key"]]["chapters"]):
            k = chap_key(ch["title"])
            hits = []
            if k:
                unit, num = k
                for f in pdfs:
                    for m in re.finditer(r"第\s*(\d+|[零一二三四五六七八九十]+)\s*([章周节讲])", f["n"]):
                        n2 = cn_to_int(m.group(1))
                        if n2 == num and m.group(2) == unit:
                            hits.append(f["p"])
                            break
            mapping[ci] = hits
        # 基础篇数学：题目清单用“第N节”，课件用“第 6 章 数学-第 N 讲”
        if meta["key"] == "basic":
            for ci, ch in enumerate(problems["basic"]["chapters"]):
                m = re.match(r"^第([一二三四五六七八九\d]+)节", ch["title"])
                if m and not mapping.get(ci):
                    n = cn_to_int(m.group(1))
                    for f in pdfs:
                        if re.search(rf"数学\s*-\s*第\s*{n}\s*讲", f["n"]):
                            mapping[ci] = [f["p"]]
        chap_pdfs[meta["key"]] = mapping

    # 真题
    provincial = sorted(rel_files(os.path.join(ASSETS, "exams", "provincial")), key=lambda f: -f["size"])
    national = sorted(rel_files(os.path.join(ASSETS, "exams", "national")), key=lambda f: -f["size"])

    # 历年真题目录树
    def build_tree(base, rel_base):
        tree = {"n": os.path.basename(rel_base) or rel_base, "c": []}
        entries = sorted(os.listdir(base), key=natural_key)
        dirs = [e for e in entries if os.path.isdir(os.path.join(base, e))]
        files = [e for e in entries if os.path.isfile(os.path.join(base, e))]
        for d in dirs:
            tree["c"].append(build_tree(os.path.join(base, d), rel_base + "/" + d))
        for f in files:
            tree["c"].append({"n": f, "p": (rel_base + "/" + f)})
        return tree

    hist_base = os.path.join(ASSETS, "exams", "history")
    hist_tree = None
    if os.path.exists(hist_base):
        sub = os.listdir(hist_base)
        if len(sub) == 1 and os.path.isdir(os.path.join(hist_base, sub[0])):
            hist_tree = build_tree(os.path.join(hist_base, sub[0]), "assets/exams/history/" + sub[0])
        else:
            hist_tree = build_tree(hist_base, "assets/exams/history")

    # 历年真题在线练习链接
    practice_link = None
    for root, _, files in os.walk(hist_base):
        if "蓝桥杯真题在线练习及答案.txt" in files:
            with open(os.path.join(root, "蓝桥杯真题在线练习及答案.txt"), encoding="utf-8", errors="ignore") as f:
                m = re.search(r"https?://\S+", f.read())
                if m:
                    practice_link = m.group(0)
            break

    # 仓库自有文档（题解/笔记/模板/ICPC，来自 scripts/gen_docs.py）
    repo = json.load(open(os.path.join(SITE, "data", "repo_docs.json"), encoding="utf-8"))
    sol_by_pid = {}
    for sol in repo["solutions"]:
        sol_by_pid[sol["pid"]] = {"file": sol["file"], "topic": sol["topic"], "title": sol["title"]}

    data = {
        "version": 3,
        "repo": repo,
        "solutionByPid": sol_by_pid,
        "generatedAt": "2026-10-24",
        "problems": problems,
        "roadmap": ROADMAP,
        "courses": COURSES_META,
        "courseFiles": course_files,
        "chapPdfs": chap_pdfs,
        "exams": {
            "provincial": provincial,
            "national": national,
            "historyTree": hist_tree,
            "practiceLink": practice_link,
        },
        "guide": "assets/guide/算法竞赛课程学习指南.pdf",
        "dsCodeTree": build_tree(os.path.join(ASSETS, "courses", "ds-code"), "assets/courses/ds-code") if os.path.exists(os.path.join(ASSETS, "courses", "ds-code")) else None,
    }

    total = sum(v["total"] for v in problems.values())
    out = os.path.join(ASSETS, "js", "data.js")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("// 自动生成：python scripts/gen_data.py（题库 + 路线 + 课件 + 真题）\n")
        f.write("window.SITE_DATA = ")
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";\n")
    print("data.js written:", round(os.path.getsize(out) / 1024), "KB | problems:", total,
          "| practice link:", practice_link)

if __name__ == "__main__":
    main()
