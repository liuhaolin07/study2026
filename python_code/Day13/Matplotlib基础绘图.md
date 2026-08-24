# Day 13 学习笔记：Matplotlib 基础绘图

> 目标：会画折线图和散点图，能加标题、坐标轴、图例、网格，能存成图片。
> 配套练习：`test.py`（产出 3 张 png）

---

## 一、每个脚本的第一步：中文设置

```python
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False
```

不设置的话，中文全部显示为方框 □，负号显示异常。这是 Windows 上第一个坑。

## 二、画一张图的固定套路（五件套）

```python
x = np.linspace(-2, 2, 100)   # ① 准备数据
plt.figure(figsize=(6, 4))    # ② 新建画布
plt.plot(x, x**2)             # ③ 画图
plt.title("y = x²")           # ④ 装饰：标题/轴标签
plt.xlabel("x"); plt.ylabel("y")
plt.savefig("out.png", dpi=150)  # ⑤ 先保存
plt.show()                       #   再显示（show 之后画布清空！）
```

**savefig 必须写在 show 之前**——show 会关闭当前画布，之后保存的是空白图。

## 三、plot 的样式速查

格式字符串 = `颜色 + 线型 + 标记`：

| 颜色 | 线型 | 标记 |
|------|------|------|
| b 蓝 g 绿 r 红 c 青 m 紫 y 黄 k 黑 | `-` 实线 `--` 虚线 `:` 点线 `-.` 点划线 | `o` 圆 `s` 方 `^` 三角 `*` 星 |

也可以用关键字参数写得更明确：

```python
plt.plot(x, y, color="tab:blue", linestyle="--", marker="o",
         linewidth=2, markersize=4, alpha=0.8, label="实验组")
```

## 四、散点图 scatter

```python
plt.scatter(x, y, s=25, c="tab:red", alpha=0.7)
```

- 散点图看**关系与分布**；折线图看**趋势**；
- 点很多时把 `s` 调小、`alpha` 调低；
- `c=` 还可以传数组做渐变着色（进阶）。

## 五、图例 legend

给每条线加 `label="..."`，最后 `plt.legend()` 显示。

## 六、今日任务验收

- ✅ 画出 y=x² 曲线并保存 png
- ✅ 一张图画三条不同样式的曲线 + 图例
- ✅ 画出“学习时长 vs 分数”散点图

**明日预告（Day 14）**：subplot 多图布局——论文里一排对比图的画法。
