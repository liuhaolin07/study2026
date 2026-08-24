# -*- coding: utf-8 -*-
"""Day 8：随机数模拟
前置：pip install numpy
运行方式：python test.py
"""
import numpy as np

# ========== 0. 随机种子 seed ==========
# 固定种子 → 每次运行产生同一批“随机”数（结果可复现，写报告必备）
np.random.seed(42)
print("固定种子后前5个随机数:", np.random.rand(5))

np.random.seed(42)
print("重设同一种子再取:      ", np.random.rand(5), "← 和上面完全一样")

# ========== 1. 常用随机函数速览 ==========
print("\n--- 常用函数 ---")
print("rand(2,3):      0~1 均匀分布\n", np.random.rand(2, 3))
print("randn(3):       标准正态分布 N(0,1)\n", np.random.randn(3))
print("randint(1,7,5): [1,7) 整数（模拟骰子）", np.random.randint(1, 7, size=5))
print("choice:         从列表抽一个", np.random.choice(["甲", "乙", "丙"]))
print("normal(170,6):  均值170标准差6的正态抽样", np.random.normal(170, 6))

# ========== 2. 模拟一：抛硬币（大数定律） ==========
# 思路：rand < 0.5 记为正面。次数越多，频率越接近 0.5
print("\n--- 抛硬币 ---")
for n in [10, 100, 1000, 100000]:
    flips = np.random.rand(n) < 0.5     # True=正面
    freq = flips.mean()                  # True 当作 1 求平均 = 频率
    print(f"抛 {n:>6} 次，正面频率 = {freq:.4f}")

# ========== 3. 模拟二：掷骰子 ==========
print("\n--- 掷骰子6000次，各点数频率 ---")
rolls = np.random.randint(1, 7, size=6000)   # 1~6
for face in range(1, 7):
    print(f"{face} 点出现 {(rolls == face).mean():.3f}")   # 理论值 ≈ 0.167

# ========== 4. 模拟三：蒙特卡洛思想预热 ==========
# 在 1x1 正方形里随机撒点，统计落在四分之一圆内的比例
# 圆方程 x²+y²≤1，落在圆内 ⇒ 该点满足条件
N = 10000
xs = np.random.rand(N)
ys = np.random.rand(N)
inside = (xs**2 + ys**2 <= 1).mean()
print(f"\n--- 蒙特卡洛预热：{N} 个点中落入四分之一圆的比例 = {inside:.4f}")
print("理论值 π/4 =", np.pi / 4)

# 今日练习：
# 1) 模拟同时抛两枚硬币 10000 次，统计“恰好一正一反”的频率（理论值 0.5）
np.random.seed(0)
c1 = np.random.rand(10000) < 0.5
c2 = np.random.rand(10000) < 0.5
exactly_one = (c1 != c2).mean()
print(f"\n练习: 一正一反频率 = {exactly_one:.4f}")

# 2) 用 randint 模拟抽奖：从 1~100 中抽 5 个不重复号码
print("练习: 抽奖号码 =", np.random.choice(np.arange(1, 101), size=5, replace=False))
