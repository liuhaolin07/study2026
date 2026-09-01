# -*- coding: utf-8 -*-
"""Day 22：分组聚合 groupby / 聚合统计
前置：pip install pandas
运行方式：python test.py
"""
import pandas as pd
import numpy as np

rng = np.random.RandomState(3)

# 造一份 30 名学生、3 个班、4 门课的成绩表（含出勤天数）
n = 30
classes = rng.choice(["1班", "2班", "3班"], n)
genders = rng.choice(["男", "女"], n)
df = pd.DataFrame({
    "学号": [f"2023{i:03d}" for i in range(1, n + 1)],
    "班级": classes,
    "性别": genders,
    "语文": rng.normal(78, 9, n).round().clip(40, 100),
    "数学": rng.normal(75, 11, n).round().clip(40, 100),
    "英语": rng.normal(82, 8, n).round().clip(40, 100),
    "缺勤天": rng.randint(0, 6, n),
})
df["总分"] = df[["语文", "数学", "英语"]].sum(axis=1)
print("--- 数据前5行 ---")
print(df.head(), "\n")

# ========== 1. groupby 的基本思想 ==========
# split（按班级切开）→ apply（每块算平均）→ combine（拼回一张表）
# 这就是经典的 split-apply-combine 模式：把"对每组分别做某事"统一成一行代码。
# ⚠️ 分组列会变成结果的行索引；想让它变回普通列，接 .reset_index()
class_mean = df.groupby("班级")[["语文", "数学", "英语"]].mean()
print("--- 各班各科平均分 ---")
print(class_mean.round(1))

# ========== 2. 单列多统计量 ==========
print("\n各班数学：均值/最高/最低/人数")
agg1 = df.groupby("班级")["数学"].agg(["mean", "max", "min", "count"])
print(agg1.round(1))

# ========== 3. agg 给不同列配不同统计量 ==========
agg2 = df.groupby("班级").agg(
    平均总分=("总分", "mean"),
    数学最高=("数学", "max"),
    英语最低=("英语", "min"),
    总缺勤=("缺勤天", "sum"),
)
print("\n--- 一表看全班的综合画像 ---")
print(agg2.round(1))
# 命名聚合写法：新列名=("原列名", 函数)，推荐！

# ========== 4. 多级分组 ==========
two_level = df.groupby(["班级", "性别"])["总分"].mean()
print("\n--- 班级 × 性别 平均总分 ---")
print(two_level.round(1).unstack())     # unstack 把内层索引变成列

# ========== 5. value_counts 与 crosstab ==========
print("\n各班人数:")
print(df["班级"].value_counts())

print("\n班级×性别 交叉表:")
print(pd.crosstab(df["班级"], df["性别"]))

# ========== 6. transform：把统计量广播回每一行 ==========
# groupby 三兄弟分工：agg 组→一行；transform 组→广播回每一行（形状不变）；
# filter 按组条件整组去留。这里用 transform 算"每人与班均的偏离"
df["班均"] = df.groupby("班级")["总分"].transform("mean")
df["偏离"] = (df["总分"] - df["班均"]).round(1)
print("\n--- transform 示例（前5行）---")
print(df[["学号", "班级", "总分", "班均", "偏离"]].head())

# 组内排名
df["班内排名"] = df.groupby("班级")["总分"].rank(ascending=False).astype(int)
top2_each = df[df["班内排名"] <= 2].sort_values(["班级", "班内排名"])
print("\n各班前两名:")
print(top2_each[["姓名" if "姓名" in df.columns else "学号", "班级", "总分", "班内排名"]])

# ========== 今日练习 ==========
# 1) 缺勤是否影响成绩？按“缺勤0-2天/3天以上”两组比较平均总分
df["缺勤组"] = np.where(df["缺勤天"] <= 2, "少缺勤(≤2)", "常缺勤(≥3)")
print("\n练习-缺勤与成绩:")
print(df.groupby("缺勤组")[["总分", "缺勤天"]].mean().round(1))
# 2) 找出每个班总分标准差最小的科目（提示：groupby.std）
print("\n练习-各班三科分数波动(std):")
print(df.groupby("班级")[["语文", "数学", "英语"]].std().round(1))
