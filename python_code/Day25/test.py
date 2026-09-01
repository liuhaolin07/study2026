# -*- coding: utf-8 -*-
"""Day 25：建模流程演示——人口增长的两个经典模型
前置：pip install numpy matplotlib
运行方式：python test.py
产出：population_models.png

模型背景：
  Malthus 指数模型   dN/dt = rN            → 解为 N = N0·e^(rt)
  Logistic 阻滞模型  dN/dt = rN(1 - N/K)   → 资源有限时更现实
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ========== 第1步：问题分析 ==========
# 问题：预测种群数量随时间的变化
# 关键变量：t 时间, N(t) 数量；参数：r 增长率, K 环境容量
# 假设A(Malthus)：增长率恒定 → 无限资源；适合早期/短期预测（如培养初期的细菌）
# 假设B(Logistic)：增长受环境容量 K 限制 → 更符合长期现实，多数建模题的默认选择
# 参数含义：r = 内禀增长率（人均出生率−死亡率，决定增长快慢）；
#           K = 资源能长期承载的最大规模（曲线最终趋近的水平渐近线）

N0, r, K = 10.0, 0.5, 500.0        # 初始数量、增长率、容量

# ========== 第2步：模型公式化（解析解） ==========
t = np.linspace(0, 20, 200)
malthus = N0 * np.exp(r * t)                                # 指数解
logistic = K / (1 + (K / N0 - 1) * np.exp(-r * t))          # S形曲线解

# ========== 第3步：“数据”——模拟带噪声的观测值 ==========
# 真实世界按 Logistic 规律运行 + 测量噪声（我们假装不知道真相）
rng = np.random.RandomState(5)
obs_t = np.arange(0, 21, 2)                                  # 每2年观测一次
truth = K / (1 + (K / N0 - 1) * np.exp(-r * obs_t))
obs_n = truth + rng.normal(0, 15, len(obs_t))                # 加噪声

# ========== 第4步：求解——分别用两个模型拟合参数 ==========
from scipy.optimize import curve_fit    # 曲线拟合（Day 28 还会细讲）

def f_malthus(t, N0_, r_):
    return N0_ * np.exp(r_ * t)

def f_logistic(t, N0_, r_, K_):
    return K_ / (1 + (K_ / N0_ - 1) * np.exp(-r_ * t))

p_m, _ = curve_fit(f_malthus, obs_t, obs_n, p0=[N0, 0.3])
p_l, _ = curve_fit(f_logistic, obs_t, obs_n, p0=[N0, 0.3, 400])

def rmse(y_true, y_pred):
    return float(np.sqrt(np.mean((np.asarray(y_true) - y_pred)**2)))

fit_m = f_malthus(obs_t, *p_m)
fit_l = f_logistic(obs_t, *p_l)
print("--- 拟合结果 ---")
print(f"Malthus:  N0={p_m[0]:.2f}, r={p_m[1]:.3f}            RMSE={rmse(obs_n, fit_m):.2f}")
print(f"Logistic: N0={p_l[0]:.2f}, r={p_l[1]:.3f}, K={p_l[2]:.1f}  RMSE={rmse(obs_n, fit_l):.2f}")

# ========== 第5步：可视化检验 ==========
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(t, malthus, "r--", label=f"Malthus 模型 (r={p_m[1]:.2f})")
ax.plot(t, logistic, "g-", label="Logistic 模型")
ax.scatter(obs_t, obs_n, c="black", zorder=3, label="观测数据")
ax.axhline(K, color="gray", ls=":", label=f"容量 K≈{p_l[2]:.0f}")
ax.set_xlabel("时间 t"); ax.set_ylabel("数量 N(t)")
ax.set_title("同一批数据、两种假设：模型选择决定结论质量")
ax.legend(); ax.grid(alpha=0.3)
fig.savefig("population_models.png", dpi=150, bbox_inches="tight")
plt.show()

# ========== 结论讨论（写论文的“模型评价”） ==========
print("""
讨论：
1) Malthus 在早期与数据接近，但后期指数爆炸，明显偏离；
2) Logistic 出现 S 形并趋于容量 K，RMSE 更小 → 对这组数据更合理；
3) 若只看前8年数据，两模型都“看起来不错”→ 说明观测窗口要覆盖关键阶段。
""")
