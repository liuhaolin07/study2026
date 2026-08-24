# Day 6 学习笔记：NumPy 入门

> 目标：理解 ndarray——后面 NumPy/Matplotlib/Pandas/机器学习全都建立在它上面。
> 前置安装：`pip install numpy`
> 配套练习：`test.py`

---

## 一、为什么需要 NumPy？

Python 自带 list 慢，且不能直接做整体数学运算。NumPy 的 ndarray：

- **向量化运算**：`a * 2` 直接对每个元素乘 2，不用写 for 循环；
- 底层是 C 实现，**比纯 Python 循环快几十到上百倍**；
- 是 pandas、sklearn、scipy 的地基。

---

## 二、核心属性（以矩阵 A 为例）

| 属性 | 含义 | 示例 |
|------|------|------|
| `A.shape` | 形状 (行, 列) | `(3, 4)` |
| `A.ndim` | 维度数 | 2 |
| `A.size` | 元素总数 | 12 |
| `A.dtype` | 元素类型 | `int64` / `float64` / `bool` |

类型转换：`arr.astype(int)`、`arr.astype(float)`。

---

## 三、创建数组的常用方法

```python
np.array([1, 2, 3])            # 从列表创建
np.zeros((2, 3))               # 全 0
np.ones((2, 3))                # 全 1
np.full((2, 2), 7)             # 全部填指定值
np.eye(3)                      # 3x3 单位阵（线代！）
np.arange(0, 10, 2)            # 等差整数序列 [0,2,4,6,8]
np.linspace(0, 1, 5)           # 区间均匀取 N 个点（画函数必备）
np.random.rand(2, 3)           # 随机数组（Day 8 细讲）
```

**arange vs linspace**：arange 按“步长”取点；linspace 按“个数”均分区间。画 y=f(x) 时几乎总是用 linspace。

---

## 四、reshape 变形

```python
a = np.arange(12)
B = a.reshape(3, 4)     # 变成 3 行 4 列
C = a.reshape(-1, 4)    # -1 = 这一维自动计算（元素总数不变的前提下）
```

规则：变形前后 `size` 必须相等。

---

## 五、索引与切片（重点）

```python
M[i, j]        # 第 i 行第 j 列（下标从 0 开始）
M[0]           # 整行
M[:, 1]        # 整列 → 所有行的第 1 列
M[0:2, 1:]     # 行切片 + 列切片组合
M[M > 50]      # ★布尔筛选：取出所有满足条件的元素
```

布尔筛选是数模数据处理的基本功，Day 21 的 pandas 条件查询就是它的升级版。

---

## 六、今日任务验收

1. ✅ 会创建向量、矩阵，能说出 shape/dtype
2. ✅ 会用 zeros/eye/arange/linspace 快速构造数组
3. ✅ reshape 与 -1 用法
4. ✅ 基本索引、切片、布尔筛选
5. ✅ 练习：全 1 矩阵挖空对角线；linspace 生成 sin 曲线数据

**明日预告（Day 7）**：矩阵运算——`*` 和 `@` 的区别是新手必踩的坑。
