# -*- coding: utf-8 -*-
"""Day 28：优化基础 scipy.optimize
前置：pip install scipy numpy matplotlib
运行方式：python optimization.py
产出：optimization_surface.png
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, linprog, curve_fit

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ========== 1. 无约束优化：求函数最小值 ==========
# 目标：f(x) = (x - 3)² + 5，显然最小值在 x=3
def f(x):
    return (x[0] - 3) ** 2 + 5

res = minimize(f, x0=[0], method="BFGS")     # x0 是初值（重要！）
print("--- 一维最小化 ---")
print(f"最优解 x* = {res.x[0]:.4f}（理论值3）, 最小值 f(x*) = {res.fun:.4f}")
print("是否收敛:", res.success)

# 二维：碗状函数 (x-2)² + (y+1)² + 7
def g(v):
    return (v[0] - 2) ** 2 + (v[1] + 1) ** 2 + 7

res2 = minimize(g, x0=[0, 0])
print("\n--- 二维最小化 ---")
print(f"最优解 = {res2.x.round(3)}（理论 [2,-1]）, 最小值 = {res2.fun:.3f}")
# ⚠️ 局部最小值陷阱：非凸函数换几个初值多跑几次

# ========== 2. 带约束优化：线性规划（生产计划问题） ==========
# 问题：工厂生产 A、B 产品，最大化利润
#   max  z = 3x + 5y
#   s.t. x ≤ 4          （车间一工时）
#        2y ≤ 12        （车间二工时）
#        3x + 2y ≤ 18   （原料）
#        x, y ≥ 0
# linprog 只做"最小化"，max 要变成 min(-z)
c = [-3, -5]
A_ub = [[1, 0],      # x ≤ 4
        [0, 2],      # 2y ≤ 12
        [3, 2]]      # 3x+2y ≤ 18
b_ub = [4, 12, 18]

res3 = linprog(c=c, A_ub=A_ub, b_ub=b_ub,
               bounds=[(0, None), (0, None)], method="highs")
print("\n--- 线性规划：生产计划 ---")
print(f"A产品产量 x = {res3.x[0]:.2f}, B产品产量 y = {res3.x[1]:.2f}")
print(f"最大利润 z = {-res3.fun:.2f}   （教材理论解 x=2, y=6, z=36）")

# ========== 3. curve_fit：非线性拟合（数模高频！） ==========
# 观测数据符合 y = a·e^(-b·x)，反推 a、b
rng = np.random.RandomState(8)
xs = np.linspace(0, 4, 25)
ys = 6 * np.exp(-1.3 * xs) + rng.normal(0, 0.15, xs.size)   # 真值 a=6,b=1.3

def model(x, a, b):
    return a * np.exp(-b * x)

params, cov = curve_fit(model, xs, ys, p0=[1, 1])   # p0 初值
perr = np.sqrt(np.diag(cov))                        # 参数标准误
print("\n--- curve_fit 拟合 ---")
print(f"a = {params[0]:.3f} ± {perr[0]:.3f}（真值6）")
print(f"b = {params[1]:.3f} ± {perr[1]:.3f}（真值1.3）")

# ========== 4. 可视化：目标曲面 + 最优点 + 拟合曲线 ==========
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.6))

# 左：二维目标函数等高线与最优点
gx, gy = np.meshgrid(np.linspace(-2, 6, 200), np.linspace(-5, 3, 200))
gz = (gx - 2) ** 2 + (gy + 1) ** 2 + 7
cs = axes[0].contourf(gx, gy, gz, levels=30, cmap="viridis")
fig.colorbar(cs, ax=axes[0], label="g(x,y)")
axes[0].plot(*res2.x, "r*", ms=15, label="最优点")
axes[0].set_title("目标函数等高线与最优解"); axes[0].legend()

# 右：curve_fit 结果
xx = np.linspace(0, 4, 200)
axes[1].scatter(xs, ys, s=20, alpha=0.7, label="观测数据")
axes[1].plot(xx, model(xx, *params), "r-", lw=2,
             label=f"拟合 a={params[0]:.2f}, b={params[1]:.2f}")
axes[1].set_title("非线性拟合 curve_fit")
axes[1].set_xlabel("x"); axes[1].set_ylabel("y"); axes[1].legend()

fig.savefig("optimization_surface.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n已保存 optimization_surface.png")

# ========== 今日练习 ==========
# 1) 把生产计划改为 max 4x+3y、约束 x+y≤10, x≤6, y≤8，重解；
# 2) 给 minimize 一个“双谷”函数 (x²-1)²+x/2，从不同 x0 出发看会掉进哪个谷。
