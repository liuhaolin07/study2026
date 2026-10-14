# -*- coding: utf-8 -*-
"""Day 30 综合评价：AHP 层次分析法 + TOPSIS 逼近理想解
流程：定权重(AHP含一致性检验) → 构造决策矩阵 → 正向化/标准化 → TOPSIS排序 → 可视化
前置：pip install numpy pandas matplotlib
运行方式：python ahp_topsis.py
产出：ahp_topsis.png
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ========== 1. AHP：由专家两两比较得出指标权重 ==========
# 问题：评价 5 个城市是否宜居，用 4 个指标
#   经济水平 / 空气质量 / 房价压力 / 交通便利度
# 判断矩阵 A：a_ij 表示"指标i 比 指标j 重要多少倍"（1~9 标度，互反 a_ji=1/a_ij）
# 为什么要一致性检验：防止专家打分自相矛盾（A比B重要、B比C重要、却C比A重要）；
# CR < 0.1 认为打分自洽可用，否则要重新调整判断矩阵
criteria = ["经济水平", "空气质量", "房价压力", "交通便利度"]
A = np.array([
    [1,   3,   2,   4],     # 经济 vs 其他
    [1/3, 1,   1/2, 2],     # 空气 vs 其他
    [1/2, 2,   1,   3],     # 房价 vs 其他
    [1/4, 1/2, 1/3, 1],
])


def ahp_weights(A):
    """AHP求权重：特征值法（最大特征值对应的归一化特征向量）+ 一致性检验"""
    lam, vec = np.linalg.eig(A)
    k = int(np.argmax(lam.real))              # 最大特征值位置
    lam_max = lam[k].real
    w = np.abs(vec[:, k].real)
    w = w / w.sum()                            # 归一化成权重

    n = A.shape[0]
    CI = (lam_max - n) / (n - 1)               # 一致性指标
    RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.90,
               5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
    CR = CI / RI_dict[n]                       # 一致性比率
    return w, lam_max, CR


w, lam_max, CR = ahp_weights(A)
print("--- AHP 权重计算 ---")
for name, wi in zip(criteria, w):
    print(f"{name:<6} 权重 = {wi:.4f}")
print(f"λmax = {lam_max:.4f}, CI = {(lam_max-4)/3:.4f}, CR = {CR:.4f}",
      "→ 通过一致性检验（CR<0.1）" if CR < 0.1 else "→ 未通过，判断矩阵需调整！")
# 注：不用✅/❌等 emoji，避免 GBK 控制台上 UnicodeEncodeError

# ========== 2. 构造决策矩阵（5个城市 × 4个指标） ==========
# 真实比赛换成 pd.read_excel 读原始数据
cities = ["城市A", "城市B", "城市C", "城市D", "城市E"]
X = pd.DataFrame(
    {"经济水平": [8.2, 6.5, 7.1, 5.8, 9.0],     # 越大越好（效益型）
     "空气质量": [62, 88, 74, 91, 55],          # AQI 越小越好（成本型）
     "房价压力": [3.2, 1.4, 2.1, 1.1, 3.8],     # 万元/m²，成本型
     "交通便利度": [9.0, 6.2, 7.5, 5.0, 8.5]},  # 效益型
    index=cities)
print("\n--- 决策矩阵 ---")
print(X)

# ========== 3. 数据预处理：正向化 + 向量标准化 ==========
# TOPSIS 要求所有指标统一"越大越好"
cost_idx = [1, 2]                       # 空气质量、房价压力是成本型
X_pos = X.copy()
for j in cost_idx:
    X_pos.iloc[:, j] = X.iloc[:, j].max() - X.iloc[:, j]   # 成本→效益

X_norm = X_pos / np.sqrt((X_pos ** 2).sum())               # 列向量归一化
X_weighted = X_norm.mul(w, axis=1)                         # 加权

# ========== 4. TOPSIS：贴近理想解者胜 ==========
# 直观理解：构造两个"虚拟极端城市"——每项指标都最好的（正理想解）
# 和每项都最差的（负理想解）；好城市应离前者近、离后者远，
# 得分 = 到最差的距离 ÷（到最差+到最好），把"近"和"远"合成一个 0~1 的数
ideal_best = X_weighted.max()          # 每列最大值 = 正理想解
ideal_worst = X_weighted.min()         # 每列最小值 = 负理想解

d_best = np.sqrt(((X_weighted - ideal_best) ** 2).sum(axis=1))
d_worst = np.sqrt(((X_weighted - ideal_worst) ** 2).sum(axis=1))
score = d_worst / (d_best + d_worst)   # 相对贴近度 C，∈[0,1]，越大越好

result = pd.DataFrame({"正理想距离 d+": d_best.round(4),
                       "负理想距离 d-": d_worst.round(4),
                       "TOPSIS得分": score.round(4)})
result["排名"] = result["TOPSIS得分"].rank(ascending=False).astype(int)
print("\n--- TOPSIS 评价结果 ---")
print(result.sort_values("排名"))

# ========== 5. 可视化：权重分布 + 城市排名 ==========
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.6))

# 左：AHP 指标权重
axes[0].bar(criteria, w, color="tab:blue", alpha=0.8)
for i, wi in enumerate(w):
    axes[0].text(i, wi + 0.01, f"{wi:.3f}", ha="center", fontsize=10)
axes[0].set_title(f"AHP 指标权重（CR={CR:.3f} 通过检验）")
axes[0].set_ylabel("权重"); axes[0].grid(axis="y", alpha=0.3)

# 右：TOPSIS 得分排名
res_sorted = result.sort_values("TOPSIS得分")
colors = plt.cm.RdYlGn(res_sorted["TOPSIS得分"] / res_sorted["TOPSIS得分"].max())
axes[1].barh(res_sorted.index, res_sorted["TOPSIS得分"], color=colors)
axes[1].set_title("TOPSIS 城市宜居性排名")
axes[1].set_xlabel("相对贴近度得分"); axes[1].grid(axis="x", alpha=0.3)

fig.savefig("ahp_topsis.png", dpi=150, bbox_inches="tight")
plt.show()

print("""
========== 结论 ==========
1) AHP 把主观判断转成客观权重，CR=%.3f < 0.1 说明专家打分自洽；
2) TOPSIS 得分最高的是 %s——它离"理想城市"最近、离"最差城市"最远；
3) AHP+TOPSIS 组合是数模评价类赛题（C 题）最常用套路：
   AHP 定权 →（也可搭配熵权法客观定权）→ TOPSIS/灰色关联排序。
""" % (CR, result["TOPSIS得分"].idxmax()))
print("已保存 ahp_topsis.png")

# ========== 练习 ==========
# 1) 用熵权法定权：w_j = (1-e_j)/Σ(1-e_k)，e_j = -k·Σ(p_ij·ln p_ij)，
#    再和 AHP 权重按 α 组合（组合权重），比较排名是否变化；
# 2) 把城市 E 的房价改成 5.0（翻倍），看排名会不会被 AHP 主观权重"救回来"。
