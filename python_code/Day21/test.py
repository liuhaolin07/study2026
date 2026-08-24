# -*- coding: utf-8 -*-
"""Day 21：数据筛选——条件查询与排序
前置：pip install pandas
运行方式：python test.py
"""
import pandas as pd

df = pd.DataFrame({
    "学号": ["2023001", "2023002", "2023003", "2023004", "2023005",
            "2023006", "2023007", "2023008", "2023009", "2023010"],
    "姓名": ["张三", "李四", "王五", "赵六", "钱七",
            "孙八", "周九", "吴十", "郑一", "冯二"],
    "性别": ["男", "女", "男", "男", "女", "女", "男", "男", "女", "男"],
    "班级": ["1班", "1班", "1班", "2班", "2班", "2班", "3班", "3班", "3班", "3班"],
    "语文": [90, 85, 78, 92, 66, 88, 73, 81, 95, 60],
    "数学": [85, 72, 90, 88, 75, 79, 68, 93, 89, 55],
    "英语": [88, 95, 80, 91, 70, 84, 77, 85, 92, 64],
})
print("--- 学生表 ---")
print(df, "\n")

# ========== 1. 布尔索引：单条件 ==========
high_math = df[df["数学"] > 85]
print("--- 数学 > 85 的学生 ---")
print(high_math)

girls = df[df["性别"] == "女"]
print("\n--- 女生（只看姓名列）---")
print(girls["姓名"].tolist())

# ========== 2. 多条件组合 & | ~（每个条件必须加括号！） ==========
cond = (df["数学"] > 80) & (df["性别"] == "男")
print("\n--- 数学好且是男生 ---")
print(df[cond][["姓名", "数学"]])

cond2 = (df["语文"] < 70) | (df["英语"] < 70)
print("\n--- 语文或英语不及格倾向(<70) ---")
print(df[cond2]["姓名"].tolist())

not_class1 = df[~(df["班级"] == "1班")]     # ~ 取反
print("\n--- 非1班人数:", len(not_class1))

# ⚠️ 常见错误：
#   df[df["数学"]>85 & df["性别"]=="男"]   ← 报错！&优先级高于比较
#   正确写法每个条件都套括号

# ========== 3. isin / between 快捷筛选 ==========
sel = df[df["班级"].isin(["1班", "3班"])]
print("\n--- isin: 1班或3班的同学 ---")
print(sel["姓名"].tolist())

mid = df[df["数学"].between(70, 90)]        # 含边界 [70, 90]
print("数学在[70,90]之间的人数:", len(mid))

# ========== 4. query 写法（像 SQL，可读性好） ==========
print("\n--- query: 2班的女生 ---")
print(df.query("班级 == '2班' and 性别 == '女'"))

# ========== 5. loc / iloc 精准定位 ==========
# loc[行条件, 列名] —— 筛选行的同时选列
result = df.loc[df["数学"] >= 88, ["姓名", "数学"]]
print("\n--- loc: 数学≥88 的姓名和分数 ---")
print(result)

# iloc 按位置：第0、5行的前4列
print(df.iloc[[0, 5], :4])

# ========== 6. 排序 sort_values ==========
by_total = df.assign(总分=df[["语文", "数学", "英语"]].sum(axis=1))
ranked = by_total.sort_values("总分", ascending=False)
print("\n--- 总分排名 ---")
print(ranked[["姓名", "班级", "总分"]].reset_index(drop=True))

# 多列排序：先按班级升序，同班再按数学降序
multi = by_total.sort_values(["班级", "数学"], ascending=[True, False])
print("\n--- 分班后按数学排名 ---")
print(multi[["姓名", "班级", "数学"]].head(6).to_string(index=False))

# 排名前三
top3 = ranked.nlargest(3, "总分")
print("\n总分前三:", top3["姓名"].tolist())

# ========== 今日练习 ==========
# 1) 找出三门课都 ≥75 的学生姓名（提示：三条件相 &）
all_good = df[(df["语文"] >= 75) & (df["数学"] >= 75) & (df["英语"] >= 75)]
print("\n练习-全科均衡名单:", all_good["姓名"].tolist())
# 2) 找出每班数学第一名（提示：sort + group/first，或 nlargest per group）
first_each = multi.groupby("班级").first()
print("\n练习-各班数学第一:")
print(first_each[["姓名", "数学"]])
