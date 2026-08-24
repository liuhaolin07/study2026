# -*- coding: utf-8 -*-
"""Day 27：分类模型——KNN 与决策树（鸢尾花数据集）
前置：pip install scikit-learn matplotlib numpy
运行方式：python classification.py
产出：iris_scatter.png, model_comparison.png
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ========== 1. 数据：sklearn 自带经典数据集 ==========
# 150 朵鸢尾花，4 个特征，3 个品种 → 任务：由特征判断品种
iris = load_iris()
X = iris.data            # 花瓣长宽、花萼长宽
y = iris.target          # 0/1/2 三种花
print("特征名:", iris.feature_names)
print("类别名:", iris.target_names)
print("数据形状:", X.shape)

# 先画个散点图认识数据（取两个最有区分度的特征）
fig, ax = plt.subplots(figsize=(7, 5))
colors = ["tab:blue", "tab:orange", "tab:green"]
for i, name in enumerate(iris.target_names):
    m = y == i
    ax.scatter(X[m, 2], X[m, 3], s=25, alpha=0.7,
               c=colors[i], label=name)
ax.set_xlabel("花瓣长度 cm"); ax.set_ylabel("花瓣宽度 cm")
ax.set_title("三类鸢尾花（仅看两维已几乎可分）")
ax.legend(); ax.grid(alpha=0.3)
fig.savefig("iris_scatter.png", dpi=150, bbox_inches="tight")

# ========== 2. 划分 + 标准化 ==========
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)   # stratify 保持类别比例

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)   # 只在训练集上 fit！
X_test_s = scaler.transform(X_test)         # 测试集用同一套均值方差

# ========== 3. KNN 分类器 ==========
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_s, y_train)
y_knn = knn.predict(X_test_s)
acc_knn = accuracy_score(y_test, y_knn)
print(f"\nKNN (k=5) 测试集准确率: {acc_knn:.3f}")

# k 取不同值的对比：k 太小→过拟合敏感；太大→决策边界过粗
print("\nk 值扫描:")
for k in [1, 3, 5, 9, 15]:
    acc = accuracy_score(y_test,
        KNeighborsClassifier(n_neighbors=k).fit(X_train_s, y_train).predict(X_test_s))
    print(f"  k={k:>2} → {acc:.3f}")

# ========== 4. 决策树 ==========
tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train_s, y_train)
y_tree = tree.predict(X_test_s)
acc_tree = accuracy_score(y_test, y_tree)
print(f"\n决策树(深度3) 准确率: {acc_tree:.3f}")

# 决策树的可解释性：直接打印规则！
from sklearn.tree import export_text
print("\n--- 决策树学到的规则 ---")
print(export_text(tree, feature_names=["萼长", "萼宽", "瓣长", "瓣宽"]))

# ========== 5. 混淆矩阵与分类报告 ==========
print("--- 混淆矩阵（KNN）行=真实 列=预测 ---")
print(confusion_matrix(y_test, y_knn))
print("\n分类报告:")
print(classification_report(y_test, y_knn,
      target_names=list(iris.target_names)))

# ========== 6. 可视化对比 + 树图 ==========
fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
axes[0].bar(["KNN(k=5)", "决策树(深3)"], [acc_knn, acc_tree],
            color=["tab:blue", "tab:green"], width=0.45)
axes[0].set_ylim(0.8, 1.02); axes[0].grid(axis="y", alpha=0.3)
axes[0].set_title("测试集准确率对比")
for j, v in enumerate([acc_knn, acc_tree]):
    axes[0].text(j, v + 0.004, f"{v:.3f}", ha="center")

plot_tree(tree, feature_names=["萼长", "萼宽", "瓣长", "瓣宽"],
          class_names=list(iris.target_names), filled=True, fontsize=7,
          ax=axes[1])
axes[1].set_title("决策树结构")
fig.savefig("model_comparison.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n已保存 iris_scatter.png, model_comparison.png")

# ========== 今日练习 ==========
# 1) 去掉标准化步骤重跑 KNN，准确率变了吗？为什么？（本例量纲接近所以影响小，
#    把萼长改成“毫米”单位再试，差距就出来了）
# 2) max_depth 设为 1 和 None 分别训练，比较过拟合与欠拟合。
