# Day 14 学习笔记：多图布局

> 目标：一张画布排多张子图；掌握图例位置与总标题。
> 配套练习：`test.py`（产出 2 张 png）

---

## 一、subplot 三参数

```python
plt.subplot(2, 2, 3)   # 画布分成 2行2列，当前画第 3 格
```

编号从 **1** 开始、按行优先。写完一格再写下一格，最后统一 `plt.show()`。

## 二、防重叠三板斧

```python
plt.suptitle("总标题")   # 整个画布的大标题
plt.tight_layout()       # 自动拉开子图间距（几乎每次多图都要加）
fig.subplots_adjust(...) # 手动微调（tight_layout 不够用时）
```

## 三、面向对象风格（推荐）

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(x, y)
axes[0].set_title("...")
```

- `plt.subplots()` 一次建好画布和全部子图，返回数组 `axes`；
- 方法名从 `title → set_title`、`xlim → set_xlim`；
- 混用两种风格容易踩坑，同一脚本里保持一致。

## 四、图例进阶

```python
ax.legend(loc="upper right")   # best / upper left / lower right ...
```

多条曲线共用一图时，每条 `plot(..., label=...)` 都要给 label。

## 五、今日任务验收

- ✅ 2×2 四格图画四个函数 + 总标题
- ✅ 同一张图叠两条曲线 + 指定图例位置
- ✅ 练习：上下两图画 eˣ 与 ln(x)

**明日预告（Day 15）**：柱状图与直方图——统计数据的表达。
