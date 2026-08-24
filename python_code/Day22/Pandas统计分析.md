# Day 22 学习笔记：groupby 分组聚合

> "按班级算平均分"——split-apply-combine 是数据分析的灵魂操作。
> 配套练习：`test.py`

---

## 一、思想三步：Split → Apply → Combine

```
整表 ──按"班级"切开──▶ [1班块, 2班块, 3班块]
      ──每块求均值──▶ 三个结果向量
      ──拼回一张表──▶ 各班平均分表
```

```python
df.groupby("班级")[["语文", "数学", "英语"]].mean()
```

## 二、agg：一次算多个量 / 不同列不同量

```python
# 同列多函数
df.groupby("班级")["数学"].agg(["mean", "max", "min", "count"])

# 命名聚合（推荐）：结果列名一目了然
df.groupby("班级").agg(
    平均总分=("总分", "mean"),
    数学最高=("数学", "max"),
    总缺勤=("缺勤天", "sum"),
)
```

## 三、多级分组与 unstack

```python
df.groupby(["班级", "性别"])["总分"].mean()   # 得到多级索引
.unstack()                                     # 内层索引转成列 → 矩阵视图
```

交叉频数直接用 `pd.crosstab(df["班级"], df["性别"])`。

## 四、transform：统计结果"贴回"每一行

| | agg | transform |
|---|-----|-----------|
| 返回 | 每组一行 | **与原表同长** |
| 用途 | 汇总报表 | 组内对比、派生列 |

```python
df["班均"] = df.groupby("班级")["总分"].transform("mean")
df["偏离"] = df["总分"] - df["班均"]        # 组内标准化思想的雏形

df.groupby("班级")["总分"].rank(ascending=False)   # 组内排名
```

## 五、常用聚合函数速查

`mean` `sum` `count`(非缺失计数) `size`(含缺失) `max/min` `std/var`
`median` `nunique`(去重计数) `first/last` `rank`

## 六、今日任务验收

- ✅ 会写 groupby + mean 的基本聚合
- ✅ 会用命名agg 一表出综合画像
- ✅ 会 transform 求组内偏离与组内排名
- ✅ 练习：缺勤分组对比、各班波动 std

**明日预告（Day 23–24）**：项目——校园消费数据分析，四天所学全串起来。
