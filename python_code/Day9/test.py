# -*- coding: utf-8 -*-
"""Day 9：统计计算
前置：pip install numpy
运行方式：python test.py
"""
import numpy as np

# 统计量使用场景速查：
#   描述集中趋势 → mean 均值（受异常值影响）/ median 中位数（抗异常值）
#   描述离散程度 → std 标准差 / var 方差 / ptp 极差 / 四分位数看分布
#   不同量纲想比较 → z-score 标准化；判断两列线性关系强弱 → 相关系数

np.random.seed(7)

# ========== 1. 一组数据的基本统计量 ==========
# 模拟某班 40 人的数学成绩（均值75、标准差10的正态分布，截到0~100）
scores = np.random.normal(75, 10, 40).round()
scores = np.clip(scores, 0, 100)          # clip 把越界值裁剪回区间
print("成绩数据:", scores)

print("\n--- 基本统计量 ---")
print(f"人数   n       = {len(scores)}")
print(f"平均分 mean    = {scores.mean():.2f}")
print(f"中位数 median  = {np.median(scores):.2f}")
print(f"标准差 std     = {scores.std():.2f}")
print(f"方差   var     = {scores.var():.2f}")
print(f"最高分         = {scores.max()}")
print(f"最低分         = {scores.min()}")
print(f"极差   ptp     = {np.ptp(scores)}")

# 分位数：四分位数是箱线图的基础；相比均值，分位数对异常值更鲁棒
q1, q2, q3 = np.percentile(scores, [25, 50, 75])
print(f"四分位数 Q1={q1}, Q2={q2}, Q3={q3}")

# ========== 2. 二维数据的 axis 参数 ==========
# 模拟 5 名学生的 3 门课成绩
table = np.array([[90, 85, 88],
                  [85, 72, 95],
                  [78, 90, 80],
                  [92, 88, 91],
                  [66, 75, 70]])
print("\n--- 成绩表 (5人 x 3科) ---")
print("每人的总分 axis=1:", table.sum(axis=1))
print("每科均分 axis=0:", table.mean(axis=0).round(2))
print("全表最高分:", table.max(), "位置(行,列):", np.unravel_index(table.argmax(), table.shape))

# ========== 3. 标准化 z-score ==========
heights = np.array([165, 170, 172, 178, 182, 190])
z = (heights - heights.mean()) / heights.std()
print("\n--- z-score 标准化 ---")
print("原始身高:", heights)
print("标准化后:", z.round(2), "← 均值≈0，标准差≈1")
print("验证: z.mean =", round(z.mean(), 6), ", z.std =", round(z.std(), 6))

# ========== 4. 相关系数 ==========
# r ∈ [-1, 1]：|r|>0.8 强相关，0.5~0.8 中等，<0.3 弱相关；
# ⚠️ 它只衡量"线性"关系，而且相关不等于因果（后面阶段会反复用到）
# 学习时长 vs 考试分数（构造一组正相关数据）
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
points = np.array([55, 62, 66, 70, 76, 80, 83, 88])
r = np.corrcoef(hours, points)[0, 1]
print("\n--- 相关系数 ---")
print(f"学习时长与分数的相关系数 r = {r:.4f}  ← 强正相关")

# 反例：随机噪声之间几乎不相关
noise1 = np.random.randn(100)
noise2 = np.random.randn(100)
print("两组随机噪声的相关系数 ≈", round(np.corrcoef(noise1, noise2)[0, 1], 3))

# ========== 5. 直方图统计 ==========
print("\n--- 分数段统计 np.histogram ---")
counts, edges = np.histogram(scores, bins=[0, 60, 70, 80, 90, 101])
labels = ["不及格", "60-69", "70-79", "80-89", "90+"]
for label, c in zip(labels, counts):
    print(f"{label}: {'█' * c} {c} 人")

# ========== 6. 今日练习：输出班级分析报告 ==========
print("\n" + "=" * 40)
print("练习：班级成绩分析报告")
print("=" * 40)
print(f"参考人数: {len(scores)}")
print(f"平均分: {scores.mean():.1f} | 中位数: {np.median(scores):.1f} | 标准差: {scores.std():.1f}")
print(f"及格率: {(scores >= 60).mean():.1%}")
print(f"优秀率(≥90): {(scores >= 90).mean():.1%}")
print(f"最高分 {scores.max()} 分的同学超过全班 {(scores < scores.max()).mean():.1%} 的人")
