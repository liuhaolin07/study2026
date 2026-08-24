# -*- coding: utf-8 -*-
"""Day 6：NumPy 入门
首次使用前请先安装：pip install numpy
运行方式：python test.py
"""
import numpy as np

# ========== 1. 从列表创建 ndarray ==========
# 向量（一维）
v = np.array([1, 2, 3, 4, 5])
print("向量 v =", v)
print("shape =", v.shape, "| ndim =", v.ndim, "| size =", v.size)

# 矩阵（二维）：用嵌套列表
A = np.array([[1, 2, 3],
              [4, 5, 6]])
print("\n矩阵 A =\n", A)
print("shape =", A.shape, "   # (行数, 列数)")
print("dtype =", A.dtype)     # 元素类型 int64
print("size =", A.size)       # 元素总个数 6

# ========== 2. dtype：元素的数据类型 ==========
f = np.array([1.0, 2.5, 3.14])
i = np.array([1, 0, 1], dtype=bool)
print("\ndtype 示例:")
print(f.dtype)      # float64
print(i.dtype)      # bool

# 整型矩阵除法会自动变成 float
print(np.array([1, 2, 3]) / 2)

# 显式转换类型 astype
x = np.array([1.7, 2.3, 3.9])
print("astype(int):", x.astype(int))       # 截断小数 → [1 2 3]

# ========== 3. 快速创建数组 ==========
print("\n快速创建:")
print("zeros:\n", np.zeros((2, 3)))            # 全 0 矩阵
print("ones:\n", np.ones((2, 2)))              # 全 1
print("full:\n", np.full((2, 2), 7))           # 全部填 7
print("eye(单位阵):\n", np.eye(3))              # 对角线为 1
print("arange:", np.arange(0, 10, 2))          # [0 2 4 6 8] 类似 range
print("linspace:", np.linspace(0, 1, 5))       # [0,1] 均匀取 5 个点（画函数常用！）

# 随机矩阵（详细用法 Day 8 讲）
print("随机 2x3:\n", np.random.rand(2, 3))

# ========== 4. reshape 变形 ==========
a = np.arange(1, 13)          # [1..12]
B = a.reshape(3, 4)           # 变成 3行4列，元素总数不能变！
print("\nreshape(3,4):\n", B)
print("reshape(-1, 4)：-1 表示行数自动算")
C = a.reshape(-1, 4)
print(C.shape)                # (3, 4)

# ========== 5. 索引与切片 ==========
M = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])
print("\n索引与切片:")
print("M[1, 2]      =", M[1, 2])        # 第1行第2列 → 60（下标从0开始）
print("M[0]         =", M[0])           # 第0整行
print("M[:, 1]      =", M[:, 1])        # 所有行的第1列 → [20 50 80]
print("M[0:2, 1:]    =\n", M[0:2, 1:])   # 前2行、第1列之后
print("M[M > 50]     =", M[M > 50])      # 布尔筛选：所有大于50的元素！

# ========== 6. 向量化运算预告（NumPy 的灵魂） ==========
# 不用写 for 循环，直接对整个数组做运算
prices = np.array([10, 20, 30])
print("\n向量化运算:")
print("prices * 2    =", prices * 2)               # 每个元素乘2
print("prices + 100  =", prices + 100)             # 每个元素加100
print("prices ** 2   =", prices ** 2)

# 今日练习：
# 1) 创建一个 5x5 的矩阵，对角线为 0，其余全为 1（提示：ones - eye）
# 2) 用 linspace 生成 0~π 的 100 个点，计算 y = sin(x)
import math
x = np.linspace(0, math.pi, 100)
y = np.sin(x)
print("\n练习2: y=sin(x)，前5个点:", y[:5])
