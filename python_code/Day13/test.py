# -*- coding: utf-8 -*-
"""Day 13：Matplotlib 基础绘图
前置：pip install matplotlib numpy
运行方式：python test.py
产出：day13_plot.png, day13_styles.png, day13_scatter.png
"""
import numpy as np
import matplotlib.pyplot as plt

# ★ 中文显示设置：每个画图脚本开头都放这两行（否则中文/负号显示为方块）
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False   # 让负号正常显示

# 概念铺垫（贯穿后面所有画图代码）：
#   figure = 一整张"画布"（一个窗口），Axes = 画布上的一块"绘图区"；
#   一张画布可以有多个绘图区（Day 14 的多子图就是）。
#   plt.xxx() 是快捷接口，作用于"当前"绘图区；复杂图建议用面向对象的 ax.xxx()

# ========== 1. 最简单的折线图 plot ==========
x = np.linspace(-2, 2, 100)      # [-2,2] 取100个点
y = x**2                          # 计划要求：画 y = x²

plt.figure(figsize=(6, 4))        # 新建画布，单位英寸
plt.plot(x, y)                    # 折线连接各点
plt.title("y = x²")               # 标题
plt.xlabel("x")                   # x 轴标签
plt.ylabel("y")
plt.grid(True)                    # 显示网格
plt.savefig("day13_plot.png", dpi=150)   # 先保存！
print("已保存 day13_plot.png")

# ========== 2. 定制线条样式 ==========
# 格式字符串："颜色 + 线型 + 标记"连写，例如 "r--o" = 红色虚线圆点
plt.figure(figsize=(6, 4))
xs = np.linspace(0, 10, 30)
plt.plot(xs, xs, "b-", label="y=x    (蓝实线)")       # blue 实线
plt.plot(xs, xs**0.5, "g--", label="y=√x (绿虚线)")   # green 虚线
plt.plot(xs, np.sin(xs) * 3 + 5, "r:o", label="y=3sinx+5 (红点线)")
plt.legend()                      # 显示图例（配合 label）
plt.title("线型样式示例")
plt.grid(alpha=0.3)
plt.savefig("day13_styles.png", dpi=150)
print("已保存 day13_styles.png")

# ========== 3. 散点图 scatter ==========
rng = np.random.RandomState(42)
n = 80
study_hours = rng.uniform(0.5, 8, n)               # 学习时长
scores = 40 + study_hours * 6 + rng.normal(0, 5, n)  # 分数≈线性+噪声

plt.figure(figsize=(6, 4))
plt.scatter(study_hours, scores, s=25, alpha=0.7, c="tab:blue")
plt.xlabel("每天学习时长（小时）")
plt.ylabel("考试分数")
plt.title("学习时长 vs 分数（散点图）")
plt.grid(alpha=0.3)
plt.savefig("day13_scatter.png", dpi=150)
print("已保存 day13_plot.png, day13_styles.png, day13_scatter.png")
# 观察点云走向：正相关。Day 26 会在这张图上拟合回归线！

# ========== 4. 常用参数速记 ==========
# 格式字符串三段式："颜色+线型+标记"，如 "r--o"；拆开写则是下面这些参数：
# color / c : 颜色 ("red","tab:blue","#ff8800")
# linestyle: "-"实线 "--"虚线 ":"点线 "-."点划线
# marker    : "o"圆 "s"方 "^"三角 "*"星
# linewidth : 线宽     markersize/ms: 点大小
# alpha     : 透明度 0~1（点重叠多时设小一点）

plt.show()   # 最后统一弹出所有窗口
