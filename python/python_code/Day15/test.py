# -*- coding: utf-8 -*-
"""Day 15：统计图 bar / histogram
前置：pip install matplotlib numpy
运行方式：python test.py
产出：day15_bar.png, day15_hist.png, day15_pie.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False
rng = np.random.RandomState(7)

# ========== 1. 柱状图 bar：类别数据 ==========
# bar 高频参数：width 柱宽(0~1)、color/edgecolor 填色/描边、
# bottom 堆叠起点（堆叠柱状图用）；横轴是类别时直接传字符串列表即可
subjects = ["语文", "数学", "英语", "物理"]
avg_scores = [82, 88, 79, 85]

plt.figure(figsize=(6, 4))
bars = plt.bar(subjects, avg_scores,
               color=["tab:blue", "tab:orange", "tab:green", "tab:red"],
               width=0.55)
# 在每根柱顶标注数值
for b, v in zip(bars, avg_scores):
    plt.text(b.get_x() + b.get_width() / 2, v + 0.5, str(v),
             ha="center", fontsize=11)
plt.ylim(0, 100)
plt.ylabel("平均分")
plt.title("各科平均分")
plt.savefig("day15_bar.png", dpi=150)
print("已保存 day15_bar.png")

# ========== 2. 直方图 hist：连续数据的分布 ==========
# 注意区别：bar 是“类别→一个数”，hist 是“把连续区间切成 bins 数个数”
# hist 高频参数：bins 整数=等宽分组/列表=自定义边界；density 归一化为概率密度；
# edgecolor 描边；cumulative 累积分布（看“多少比例低于某值”）
scores = np.clip(rng.normal(75, 12, 300), 20, 100)   # 300个成绩样本

plt.figure(figsize=(6, 4))
plt.hist(scores, bins=[20, 40, 55, 65, 75, 85, 95, 101],
         edgecolor="white")
plt.xlabel("分数区间")
plt.ylabel("人数")
plt.title("成绩分布直方图（自定义分组）")
plt.savefig("day15_hist.png", dpi=150)
print("已保存 day15_hist.png")

# 正态数据 + 自动30个bins：看形状
plt.figure(figsize=(6, 4))
plt.hist(rng.normal(0, 1, 5000), bins=30, density=True,
         color="tab:purple", alpha=0.75)
# 叠加理论正态曲线做对比
xs = np.linspace(-4, 4, 200)
plt.plot(xs, np.exp(-xs**2 / 2) / np.sqrt(2 * np.pi), "r--", lw=2)
plt.title("标准正态分布：样本 vs 理论曲线（density=True 归一化）")
plt.savefig("day15_hist_normal.png", dpi=150)
print("已保存 day15_hist_normal.png")

# ========== 3. 补充：饼图 pie ==========
plt.figure(figsize=(5, 5))
labels = ["步行", "自行车", "公交", "地铁"]
counts = [35, 25, 22, 18]
plt.pie(counts, labels=labels, autopct="%.1f%%",
        startangle=90, explode=[0.05, 0, 0, 0])
plt.title("通勤方式占比")
plt.savefig("day15_pie.png", dpi=150)
print("已保存 day15_pie.png")

# ========== 今日练习 ==========
# 把 Day 9 的班级成绩 scores 重新生成，画分数段柱状图（先统计再画）
np.random.seed(7)
exam = np.clip(np.random.normal(75, 10, 40).round(), 0, 100)
segments = ["<60", "60-69", "70-79", "80-89", "90+"]
cnt = [int(((exam >= lo) & (exam < hi)).sum())
       for lo, hi in [(0, 60), (60, 70), (70, 80), (80, 90), (90, 101)]]
plt.figure(figsize=(6, 4))
plt.bar(segments, cnt, color="tab:cyan", edgecolor="black")
plt.title("班级成绩分段人数")
plt.ylabel("人数")
plt.show()
