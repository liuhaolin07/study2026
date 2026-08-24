# Day 18 学习笔记：Pandas 入门 · DataFrame

> 目标：会造表、会看表、会加列。pandas 是数据分析的主战场。
> 前置安装：`pip install pandas`
> 配套练习：`test.py`

---

## 一、两个核心对象

| 对象 | 是什么 | 类比 |
|------|--------|------|
| `Series` | 一列带索引的数据 | Excel 的一列 |
| `DataFrame` | 多列共用索引的表格 | 整张 Excel 表 |

## 二、创建 DataFrame 的最常用写法

```python
df = pd.DataFrame({
    "列名1": [值...],
    "列名2": [值...],
})
```

传字典：键=列名，值=该列数据。

## 三、看新表的固定动作（背下来）

```python
df.head()      # 前5行长什么样
df.info()      # 有多少行？哪些列有缺失？各列什么类型？
df.describe()  # 数值列的 mean/std/四分位数速览
df.shape       # (行, 列)
df.dtypes      # 各列类型（object 通常是字符串）
```

拿到任何新数据，**先跑这五个再看别的**。

## 四、选列与增列

```python
df["数学"]              # 选一列 → Series
df[["姓名", "数学"]]     # 选多列 → 双括号 → DataFrame

df["总分"] = df["语文"] + df["数学"]   # 新增列 = 向量化运算
```

## 五、loc 与 iloc

| 写法 | 按…取 | 示例 |
|------|-------|------|
| `df.loc[label]` | **标签** | `df.loc["张三"]` |
| `df.iloc[position]` | **整数位置** | `df.iloc[0]` |

`set_index("姓名")` 之后两者差异才显现。

## 六、value_counts —— 类别统计神器

```python
df["性别"].value_counts()      # 男 3 / 女 2
df["性别"].value_counts(normalize=True)   # 变成比例
```

## 七、Series/DataFrame 与 NumPy 的关系

DataFrame 底层就是多个 ndarray 拼起来的表。`df.values` 能取回 ndarray——所以 Day 6–9 学的所有 numpy 统计函数在 pandas 上都通用。

## 八、今日任务验收

- ✅ 从字典创建 DataFrame，说出 shape/dtypes
- ✅ head/info/describe 三连
- ✅ 加新列（总分、平均分）
- ✅ 练习：图书表 + 最贵的书

**明日预告（Day 19）**：从 csv/excel 读真实数据。
