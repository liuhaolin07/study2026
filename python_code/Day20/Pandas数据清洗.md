# Day 20 学习笔记：数据清洗

> 真实数据永远是脏的。清洗通常占数模比赛 30%–50% 的数据处理时间。
> 配套练习：`test.py` + 脏数据 `messy_students.csv`

---

## 一、脏数据的四大类（本课数据各占一种）

| 问题 | 示例 | 处理 |
|------|------|------|
| 格式噪音 | `" 李四 "` 带空格 | `.str.strip()` |
| 重复行 | 张三整行出现两次 | `drop_duplicates()` |
| 缺失值 | 王五的成绩为空 | `dropna()` 或 `fillna()` |
| 异常/非法值 | 年龄 −5、"十九" | 转换置 NaN → 过滤或填充 |

## 二、缺失值三板斧

```python
df.isnull().sum()                 # ① 先统计每列缺多少
df.dropna()                       # ②a 有缺失的整行丢掉
df["成绩"] = df["成绩"].fillna(df["成绩"].mean())   # ②b 填充
```

填充值怎么选：

- 数值列、分布对称 → **均值**；有偏/有异常值 → **中位数**；
- 类别列（性别/城市）→ **众数**；
- 时间序列 → 前值填充 `method="ffill"`；
- 关键字段缺失且占比小 → 直接 dropna。

## 三、类型转换：to_numeric(errors="coerce")

```python
df["年龄"] = pd.to_numeric(df["年龄"], errors="coerce")
```

`coerce` 把转不动的值统一变 NaN，之后走缺失值流程——**"先 coerce 再 fill"是清洗非法值的万能套路**。

## 四、重复值

```python
df.duplicated().sum()     # 有几行完全重复
df.drop_duplicates()      # 删掉（默认保留第一次出现）
df.drop_duplicates(subset=["姓名"], keep="first")   # 按某列去重
```

⚠️ 先做 strip 清理再查重，否则 `"李四 "` 和 `"李四"` 不算重复。

## 五、异常值检测（入门两招）

```python
# 招式1：业务范围法（简单可靠，首选）
bad = (df["年龄"] < 15) | (df["年龄"] > 60)

# 招式2：3σ 法 / IQR 法
z = (df["成绩"] - df["成绩"].mean()) / df["成绩"].std()
outliers = df[z.abs() > 3]
q1, q3 = df["成绩"].quantile([0.25, 0.75])
iqr_outliers = df[(df["成绩"] < q1 - 1.5*(q3-q1)) | (df["成绩"] > q3 + 1.5*(q3-q1))]
```

处理方式：修正 > 置为缺失再填 > 剔除，视业务而定并**在论文里说明**。

## 六、标准清洗流水线

```
读入(dtype=str 更稳) → str.strip → to_numeric(coerce)
→ drop_duplicates → isnull 统计 → fillna/dropna → 异常值过滤 → 导出
```

## 七、今日任务验收

- ✅ 找出并修复四类问题，产出 clean_students.csv
- ✅ 能说清 fillna 各种填充策略的选择依据
- ✅ 思考题：dropna vs fillna 的取舍

**明日预告（Day 21）**：数据筛选——布尔索引与排序。
