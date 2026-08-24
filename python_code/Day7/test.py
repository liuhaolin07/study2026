# -*- coding: utf-8 -*-
"""Day 7：矩阵运算（对应线性代数）
前置：pip install numpy
运行方式：python test.py
"""
import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# ========== 1. 加减法和数乘（对应元素运算） ==========
print("--- 加减、数乘 ---")
print("A + B =\n", A + B)
print("A - B =\n", A - B)
print("3 * A =\n", 3 * A)

# ========== 2. 两种“乘法”，千万别混！ ==========
print("\n--- 两种乘法 ---")
print("* 是【对应元素相乘】（Hadamard积）：")
print(A * B)
print("@ 或 np.dot() 才是【矩阵乘法】：")
print(A @ B)
# 手算验证：A@B 的第0行第0列 = 1*5 + 2*7 = 19 ✔

# ========== 3. 向量点积（内积） ==========
u = np.array([1, 2, 3])
w = np.array([4, 5, 6])
print("\n--- 点积 ---")
print("u · w =", np.dot(u, w))          # 1*4+2*5+3*6 = 32
print("u @ w =", u @ w)                  # 一维时等价

# ========== 4. 转置 ==========
print("\n--- 转置 ---")
print("A.T =\n", A.T)                    # 行变列
print("(A @ B).T == B.T @ A.T ?",         # 线代重要性质
      np.array_equal((A @ B).T, B.T @ A.T))

# ========== 5. 方阵的重要量：行列式、逆矩阵 ==========
print("\n--- 行列式与逆 ---")
det = np.linalg.det(A)
print("|A| =", det)                       # 1*4-2*3 = -2
A_inv = np.linalg.inv(A)
print("A 的逆 =\n", A_inv)

# 验证 A @ A_inv = 单位阵 I
I = A @ A_inv
print("A @ A_inv =\n", np.round(I))       # 浮点误差，round 一下看更清楚
print("np.allclose(I, eye)?", np.allclose(I, np.eye(2)))

# ⚠️ 注意：奇异矩阵（行列式=0）没有逆，inv 会报错 LinAlgError

# ========== 6. 解线性方程组（数模最常用！） ==========
# 方程组： 2x + y = 5 ; x + 3y = 10
# 矩阵形式： M @ [x, y] = b
M = np.array([[2, 1],
              [1, 3]])
b = np.array([5, 10])

xyz = np.linalg.solve(M, b)
print("\n--- 解方程组 ---")
print("解得 x, y =", xyz)
print("验证 M @ 解 =", M @ xyz, "应等于", b)   # 应输出 [ 5. 10.]

# ========== 7. 综合练习：判断三条直线围成的三角形面积 ==========
# 顶点 P1(0,0), P2(4,0), P3(1,3)，用行列式公式求面积
pts = np.array([[0, 0], [4, 0], [1, 3]])
area = abs(np.linalg.det(pts[1:] - pts[0])) / 2
print("\n三角形面积 =", area)             # 6.0
