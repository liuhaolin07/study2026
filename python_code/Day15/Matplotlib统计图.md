# Day 15 学习笔记：统计图

> 柱状图、直方图、饼图——数模论文里出场率最高的三类图。
> 配套练习：`test.py`（产出 4 张 png）

---

## 一、bar 和 hist 别再分不清！

| | bar 柱状图 | hist 直方图 |
|---|-----------|------------|
| 输入 | 类别 + 各一个数值 | 一批连续数据 |
| 问题 | "各科平均分多少？" | "分数是怎么分布的？" |
| x 轴 | 离散类别 | 连续数值区间 |

```python
plt.bar(categories, values, width=0.55, color=..., edgecolor="black")
plt.hist(data, bins=30, density=True, edgecolor="white")
```

`bins`：可以给整数（自动分组）或列表 `[20,40,...]`（自定义边界）。
`density=True`：把频数变成频率密度，方便叠加理论曲线。

## 二、柱顶标数字的通用写法

```python
for b, v in zip(bars, values):
    plt.text(b.get_x() + b.get_width()/2, v + 0.5, str(v), ha="center")
```

论文里柱状图带数值标注会显得专业很多。

## 三、双 y 轴（Day16-17 项目用到）

```python
ax2 = ax1.twinx()      # 第二个 y 轴共用 x 轴
```

两个量纲不同的量（降雨 mm / 雨天天数）画在一张图时用。

## 四、饼图 pie

```python
plt.pie(values, labels=names, autopct="%.1f%%", startangle=90)
```

类别别超过 5 个，否则可读性崩塌。

## 五、选图口诀

- 比**大小** → 柱状图
- 看**分布** → 直方图 / 箱线图
- 看**趋势** → 折线图
- 看**关系** → 散点图
- 看**占比** → 饼图（类别少时）

## 六、今日任务验收

- ✅ 带数值标注的柱状图
- ✅ 自定义 bins 的成绩直方图；正态样本 vs 理论曲线
- ✅ 练习：先统计分数段人数、再画柱状图（bar 与 hist 的桥梁）

**明日预告（Day 16–17）**：项目——天气数据可视化，把前五天全部串起来。
