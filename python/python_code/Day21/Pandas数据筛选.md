# Day 21 学习笔记：数据筛选

> 目标：像查数据库一样从表里捞数据——布尔索引、isin/between、query、排序。
> 配套练习：`test.py`

---

## 一、布尔索引：筛选的核心语法

```python
df[df["数学"] > 85]              # 返回满足条件的所有行
df[df["性别"] == "女"]["姓名"]   # 筛完再选列
```

原理和 Day 6 的 numpy 布尔筛选一模一样，只是对象换成了 DataFrame。

## 二、多条件组合（括号不能省！）

```python
df[(df["数学"] > 80) & (df["性别"] == "男")]    # 且
df[(df["语文"] < 70) | (df["英语"] < 70)]       # 或
df[~(df["班级"] == "1班")]                       # 非
```

⚠️ `&` `|` 的优先级高于 `>` `==`，**每个条件必须各自加括号**，否则报错或结果错。

## 三、快捷筛选

```python
df["班级"].isin(["1班", "3班"])      # 在集合中
df["数学"].between(70, 90)           # 区间内（含边界）
df.query("班级 == '2班' and 性别 == '女'")   # SQL 风格字符串
```

## 四、loc 一步到位：筛行 + 选列

```python
df.loc[条件, ["姓名", "数学"]]     # 行用条件，列用名字
df.iloc[[0, 5], :4]               # 全按整数位置
```

## 五、排序 sort_values

```python
df.sort_values("总分", ascending=False)              # 单列降序
df.sort_values(["班级", "数学"],                      # 多列
               ascending=[True, False])
df.nlargest(3, "总分")                                # 直接取前3名
```

排完序索引还是乱的，展示时加 `.reset_index(drop=True)`。

## 六、今日任务验收

- ✅ 单条件 / 组合条件 / isin / between 都写过一遍
- ✅ loc 条件+列组合查询
- ✅ 总分排名、分班排序、前三名
- ✅ 练习：全科均衡名单；各班数学第一名

**明日预告（Day 22）**：groupby 分组聚合——"分开算再合起来"的 split-apply-combine。
