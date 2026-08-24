# -*- coding: utf-8 -*-
"""Day 14：多图布局 subplot / 图例 / 标题
前置：pip install matplotlib numpy
运行方式：python test.py
产出：day14_subplot.png, day14_subplots.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

x = np.linspace(0, 2 * np.pi, 200)

# ========== 方式一：plt.subplot(行数, 列数, 编号) ==========
# 编号从 1 开始，按行优先排列
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)                 # 第1格
plt.plot(x, np.sin(x), "b")
plt.title("sin(x)")

plt.subplot(2, 2, 2)                 # 第2格
plt.plot(x, np.cos(x), "g")
plt.title("cos(x)")

plt.subplot(2, 2, 3)                 # 第3格
plt.plot(x, np.tan(x), "r")
plt.ylim(-5, 5)                      # tan 无界，限制 y 范围
plt.title("tan(x)")

plt.subplot(2, 2, 4)                 # 第4格
plt.plot(x, x**0.5 * np.sin(x), "m--")
plt.title("√x·sin(x)")

plt.suptitle("四个函数的对比", fontsize=14)   # 总标题
plt.tight_layout()                   # ★自动调整间距，防止标题互相重叠
plt.savefig("day14_subplot.png", dpi=150)
print("已保存 day14_subplot.png")

# ========== 方式二：面向对象风格 fig, ax = plt.subplots()（推荐进阶写法） ==========
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, np.sin(x), label="sin")
axes[0].plot(x, np.sin(2 * x), label="sin(2x)")
axes[0].set_title("同一张图多条曲线")
axes[0].legend(loc="upper right")        # 图例位置可指定
axes[0].grid(alpha=0.3)

t = np.linspace(0, 1, 100)
axes[1].plot(t, np.exp(-t) * np.cos(8 * t))
axes[1].set_title("阻尼振动")
axes[1].set_xlabel("时间")
axes[1].set_ylabel("幅值")

fig.suptitle("面向对象写法示例", fontsize=14)
plt.tight_layout()
plt.savefig("day14_subplots.png", dpi=150)
print("已保存 day14_subplots.png")

# ========== 两种写法对照表 ==========
# plt 风格            →  对象风格
# plt.title(...)      →  ax.set_title(...)
# plt.xlabel(...)     →  ax.set_xlabel(...)
# plt.xlim(a,b)       →  ax.set_xlim(a,b)
# plt.legend()        →  ax.legend()

# ========== 今日练习 ==========
# 用 subplot(2,1,x) 上下两张图画 y=e^x 和 y=ln(x)，都加上标题和网格
fig2, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
xs = np.linspace(0.01, 3, 100)
ax1.plot(xs, np.exp(xs), color="tab:blue")
ax1.set_title("y = eˣ"); ax1.grid(alpha=0.3)
ax2.plot(xs, np.log(xs), color="tab:orange")
ax2.set_title("y = ln(x)"); ax2.grid(alpha=0.3)
plt.tight_layout()
plt.show()
