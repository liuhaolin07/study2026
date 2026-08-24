# -*- coding: utf-8 -*-
"""Day 10-12 项目：蒙特卡洛法求 π（数学建模经典案例）
前置：pip install numpy matplotlib
运行方式：python monte_carlo_pi.py
产出：pi_convergence.png（收敛曲线）、pi_scatter.png（撒点图）
"""
import numpy as np
import matplotlib.pyplot as plt

# 让图里能正常显示中文（Windows 自带微软雅黑/黑体）
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False


# ========== 第一部分：原理回顾 ==========
# 单位正方形内均匀撒点，四分之一圆面积/正方形面积 = π/4
# 所以 π ≈ 4 × (圆内点数 / 总点数)


# ========== 第二部分：纯 Python 循环版（帮助理解） ==========
def estimate_pi_loop(n, seed=0):
    """用普通 for 循环估计 pi —— 慢，仅用于理解原理"""
    rng = np.random.RandomState(seed)
    inside = 0
    for _ in range(n):
        x, y = rng.rand(), rng.rand()
        if x**2 + y**2 <= 1:
            inside += 1
    return 4 * inside / n


# ========== 第三部分：NumPy 向量化版（实战写法） ==========
def estimate_pi_vectorized(n, seed=0):
    """向量化：一次生成全部点，快几十倍"""
    rng = np.random.RandomState(seed)
    xs, ys = rng.rand(n), rng.rand(n)
    inside = ((xs**2 + ys**2) <= 1).sum()
    return 4 * inside / n, xs, ys


# ========== 第四部分：对比两种版本的耗时 ==========
import time

N = 1_000_000
t0 = time.time()
pi_loop = estimate_pi_loop(N)
t_loop = time.time() - t0

t0 = time.time()
pi_vec, xs, ys = estimate_pi_vectorized(N)
t_vec = time.time() - t0

print("--- 耗时对比（N = 百万点）---")
print(f"循环版:   π ≈ {pi_loop:.5f}, 耗时 {t_loop:.2f}s")
print(f"向量化版: π ≈ {pi_vec:.5f}, 耗时 {t_vec:.3f}s")
print(f"提速约 {t_loop / max(t_vec, 1e-9):.0f} 倍；真值 π = {np.pi:.5f}")


# ========== 第五部分：不同 N 的误差表（Day 11 内容） ==========
print("\n--- 收敛性实验 ---")
print(f"{'N':>12} | {'估计值':>9} | {'绝对误差':>10}")
Ns = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
errors = []
for n in Ns:
    est, _, _ = estimate_pi_vectorized(n, seed=42)
    err = abs(est - np.pi)
    errors.append(err)
    print(f"{n:>12} | {est:>9.5f} | {err:>10.5f}")
# 观察规律：N 每扩大 100 倍，误差大约缩小 10 倍（O(1/√N)）

# ========== 第六部分：可视化（Day 12 内容） ==========
# 图1：前2000个点的撒点图，圆内蓝色、圆外橙色
fig1, ax = plt.subplots(figsize=(6, 6))
mask = xs[:2000] ** 2 + ys[:2000] ** 2 <= 1
ax.scatter(xs[:2000][mask], ys[:2000][mask], s=3, color="tab:blue", label="圆内")
ax.scatter(xs[:2000][~mask], ys[:2000][~mask], s=3, color="tab:orange", label="圆外")
theta = np.linspace(0, np.pi / 2, 200)
ax.plot(np.cos(theta), np.sin(theta), color="black", lw=1.5)
ax.set_aspect("equal")
ax.set_title(f"蒙特卡洛撒点（N=2000），π ≈ {4 * mask.mean():.3f}")
ax.legend(loc="lower left")
fig1.savefig("pi_scatter.png", dpi=150, bbox_inches="tight")

# 图2：估计值随 N 的收敛曲线（对数坐标）
fig2, ax = plt.subplots(figsize=(7, 5))
ax.loglog(Ns, errors, "o-", label="绝对误差")
ref = [errors[0] * (Ns[0] / n) ** 0.5 for n in Ns]      # O(1/√N) 参考线
ax.loglog(Ns, ref, "--", label=r"$O(1/\sqrt{N})$ 参考线")
ax.axhline(0.001, color="gray", ls=":", lw=1)
ax.set_xlabel("试验次数 N")
ax.set_ylabel("|π估计 − π|")
ax.set_title("蒙特卡洛求 π 的收敛速度")
ax.legend()
fig2.savefig("pi_convergence.png", dpi=150, bbox_inches="tight")
plt.show()

print("\n已保存图片: pi_scatter.png, pi_convergence.png")
