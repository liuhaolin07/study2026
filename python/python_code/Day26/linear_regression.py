# -*- coding: utf-8 -*-
"""Day 26：线性回归（sklearn 入门第一个模型）
前置：pip install scikit-learn matplotlib numpy
运行方式：python linear_regression.py
产出：regression_fit.png
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ========== 1. 造数据：学习时长 → 考试分数（线性关系+噪声） ==========
rng = np.random.RandomState(66)
n = 60
hours = rng.uniform(0.5, 10, n)                      # 特征 X
scores = 35 + 5.5 * hours + rng.normal(0, 6, n)      # 真实规律 y=35+5.5x+ε

# sklearn 约定：X 必须是二维 (样本数, 特征数)
X = hours.reshape(-1, 1)
y = scores

# ========== 2. 划分训练集 / 测试集 ==========
# 用训练集学参数，用测试集检验泛化能力——机器学习标准流程
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)
print(f"训练集 {len(X_train)} 条 | 测试集 {len(X_test)} 条")

# ========== 3. 建模、训练、预测（核心三行） ==========
# 最小二乘原理：在所有直线里，找让残差平方和 Σ(yᵢ−ŷᵢ)² 最小的那条；
# 用平方而不用绝对值：正负误差不抵消、处处可导、对大误差惩罚更重。
model = LinearRegression()
model.fit(X_train, y_train)                 # 训练：最小二乘求参数
y_pred = model.predict(X_test)              # 预测

print("\n--- 学到的模型 ---")
print(f"截距 b0 = {model.intercept_:.2f}")
print(f"斜率 b1 = {model.coef_[0]:.2f}   （每多学1小时，分数约提高这么多）")

# ========== 4. 评估 ==========
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print(f"\n测试集 RMSE = {rmse:.2f} 分   （平均偏差幅度）")
print(f"测试集 R^2  = {r2:.3f}     （1为完美拟合，越接近1越好）")
# 注：输出用 R^2 而非 R²，避免 GBK 控制台上标字符无法编码

# ========== 5. 可视化 ==========
fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(X_train, y_train, s=22, alpha=0.6, label="训练集")
ax.scatter(X_test, y_test, s=28, color="tab:red", label="测试集")
xs = np.linspace(0, 10.5, 100).reshape(-1, 1)
ax.plot(xs, model.predict(xs), "g-", lw=2,
        label=f"回归线 y={model.coef_[0]:.1f}x{model.intercept_:+.1f}")
ax.set_xlabel("每天学习时长 h"); ax.set_ylabel("考试分数")
ax.set_title("一元线性回归")
ax.legend(); ax.grid(alpha=0.3)
fig.savefig("regression_fit.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n已保存 regression_fit.png")

# ========== 6. 多元线性回归预览 ==========
# 现实问题往往是多个自变量：分数 ~ 时长 + 睡眠 + …
sleep = rng.uniform(5, 9, n)
X_multi = np.column_stack([hours, sleep])            # 两列特征
y_multi = 20 + 5 * hours + 2.5 * sleep + rng.normal(0, 5, n)
m2 = LinearRegression().fit(X_multi, y_multi)
print("--- 多元回归 y = b0 + b1·时长 + b2·睡眠 ---")
print(f"b0={m2.intercept_:.1f}, b1={m2.coef_[0]:.2f}, b2={m2.coef_[1]:.2f}")
print(f"R^2 = {r2_score(y_multi, m2.predict(X_multi)):.3f}")

# ========== 今日练习 ==========
# 把噪声 std 从 6 调到 15，观察 R² 如何变化；思考为什么。
