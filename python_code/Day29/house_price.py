# -*- coding: utf-8 -*-
"""Day 29 项目：预测房价——五步建模流程完整落地
流程：问题分析 → 造数据 → 数据处理 → 建模求解 → 结果与可视化
前置：pip install numpy pandas matplotlib scikit-learn
运行方式：python house_price.py
产出：house_price.png, feature_importance.png
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ========== 第1步：问题分析 ==========
# 目标：根据 面积/房龄/地铁距离/楼层 预测房价（万元）
# 模型选择：目标 y 连续 → 回归问题；先线性回归，再试随机森林对比
# 假设：价格由上述特征近似线性决定 + 市场噪声

# ========== 第2步：生成模拟数据（真实比赛换成读 csv） ==========
rng = np.random.RandomState(29)
n = 300
area = rng.uniform(40, 160, n)                    # 面积 m²
age = rng.randint(0, 30, n)                       # 房龄 年
metro = rng.uniform(0.2, 5.0, n)                  # 距地铁 km
floor = rng.choice(["低层", "中层", "高层"], n)     # 楼层类别

# 真实规律：单价 = 基准 + 面积效应(边际递减) - 折旧 - 距离衰减 + 楼层溢价
price = (80
         + 1.8 * area - 0.004 * area**2          # 面积非线性！
         - 1.5 * age                              # 每年折旧1.5万
         - 12 / (metro + 0.3)                     # 地铁越近越贵
         + pd.Series(floor).map({"低层": -5, "中层": 0, "高层": 4})
         + rng.normal(0, 10, n)).round(1)

df = pd.DataFrame({"面积": area.round(1), "房龄": age,
                   "地铁距离": metro.round(2), "楼层": floor, "房价": price})
print("--- 数据预览 ---")
print(df.head())
df.to_csv("houses.csv", index=False, encoding="utf-8-sig")

# ========== 第3步：数据处理 ==========
print("\n--- 数据检查 ---")
print(df.describe().round(1))
print("缺失值:", int(df.isnull().sum().sum()))

# 类别特征 → 独热编码（模型只吃数字）
X = pd.get_dummies(df.drop(columns=["房价"]),
                   columns=["楼层"], drop_first=False)
y = df["房价"]
print("\n编码后的特征列:", X.columns.tolist())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

# ========== 第4步：建模与求解 ==========
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


def evaluate(name, model):
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    rmse = float(np.sqrt(mean_squared_error(y_test, pred)))
    r2 = float(r2_score(y_test, pred))
    print(f"{name:<14} RMSE={rmse:6.2f} 万   R²={r2:.3f}")
    return model, pred


print("\n--- 模型对比 ---")
lin, pred_lin = evaluate("线性回归", LinearRegression())
rf, pred_rf = evaluate("随机森林", RandomForestRegressor(
    n_estimators=200, random_state=42))

best_name, best_model = ("随机森林", rf) if r2_score(y_test, pred_rf) >= \
    r2_score(y_test, pred_lin) else ("线性回归", lin)
best_pred = pred_rf if best_name == "随机森林" else pred_lin

# 用最优模型预测一套新房子：
# 新数据要走同样的编码流程，再 reindex 对齐训练时的列（顺序必须一致！）
new_raw = pd.DataFrame({
    "面积": [89.0], "房龄": [6], "地铁距离": [0.8], "楼层": ["中层"]})
new_house = (pd.get_dummies(new_raw, columns=["楼层"])
             .reindex(columns=X.columns, fill_value=0))
pred_price = float(best_model.predict(new_house)[0])
print(f"\n新样本预测（89m²/房龄6/距地铁0.8km/中层）≈ {pred_price:.1f} 万元")

# ========== 第5步：可视化与结论 ==========
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.8))

# 左：预测值 vs 真实值（点贴着对角线=预测准）
axes[0].scatter(y_test, pred_lin, s=18, alpha=0.6, label="线性回归")
axes[0].scatter(y_test, pred_rf, s=18, alpha=0.6, label="随机森林")
lims = [y_test.min() - 5, y_test.max() + 5]
axes[0].plot(lims, lims, "r--", lw=1, label="完美预测线")
axes[0].set_xlabel("真实房价 万"); axes[0].set_ylabel("预测房价 万")
axes[0].set_title("预测 vs 真实"); axes[0].legend(); axes[0].grid(alpha=0.3)

# 右：随机森林的特征重要性
importances = pd.Series(rf.feature_importances_, index=X.columns).sort_values()
axes[1].barh(importances.index, importances.values, color="tab:cyan")
axes[1].set_title("随机森林特征重要性")
axes[1].grid(axis="x", alpha=0.3)
fig.savefig("house_price.png", dpi=150, bbox_inches="tight")
plt.show()

print("""
========== 结论 ==========
1) 两类模型 R² 都较高，说明选的特征确实承载了价格信息；
2) 特征重要性前三通常是 面积/房龄/地铁距离，符合常识 → 模型可信；
3) 局限：模拟数据无地段/学区变量；真实数据需重新清洗并检验残差。
""")
print("已保存 house_price.png 和 houses.csv")
