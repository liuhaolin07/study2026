# -*- coding: utf-8 -*-
"""Day 23-24 项目：校园消费数据分析（方向1）
流程：生成刷卡模拟数据 → 清洗 → 多维度分析 → 可视化 → 结论
前置：pip install pandas numpy matplotlib
运行方式：python campus_consumption.py
产出：consumption.csv + 4 张 png + 终端分析报告
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 分析思路导读（拿到一堆刷卡流水，问题从哪来？）：
#   从三个角度提问——时间（什么时候消费）、对象（谁在消费）、金额（花了多少）。
#   本项目四张图分别回答：
#   图1 全天什么时段刷卡最多？（时间分布）
#   图2 早/午/晚/超市的单笔价位差多少？（类别对比）
#   图3 一个月里每天流水怎么波动？（趋势）
#   图4 学生月消费怎么分布，低消费群体在哪？（分布与分位数，可作补助参考）

# ========== 第1步：生成一个月的食堂刷卡模拟数据 ==========
rng = np.random.RandomState(11)
n_records = 1200

stu_ids = [f"S{1000+i}" for i in rng.randint(0, 300, n_records)]
dates = pd.date_range("2024-03-01", periods=31)
days = pd.to_datetime(rng.choice(dates, n_records))

meal_types = rng.choice(["早餐", "午餐", "晚餐", "超市"], n_records,
                        p=[0.25, 0.33, 0.30, 0.12])
amounts = np.select(
    [meal_types == "早餐", meal_types == "午餐",
     meal_types == "晚餐", meal_types == "超市"],
    [rng.normal(6, 2, n_records), rng.normal(15, 4, n_records),
     rng.normal(14, 4, n_records), rng.exponential(20, n_records)],
).round(1).clip(0.5)

hours = np.select(
    [meal_types == "早餐", meal_types == "午餐",
     meal_types == "晚餐", meal_types == "超市"],
    [rng.normal(7.5, 0.5, n_records), rng.normal(12, 0.5, n_records),
     rng.normal(18, 0.5, n_records), rng.uniform(9, 21, n_records)],
).clip(6, 22)

df = pd.DataFrame({
    "学号": stu_ids,
    "时间": days,
    "时段类型": meal_types,
    "小时": hours.round(2),
    "金额": amounts,
})
df["日期"] = df["时间"].dt.date

# 人为塞进脏数据，让清洗环节有活干（对应真实场景）：
# ① 重复记录（刷卡系统重传）；② 负金额；③ 缺失的时段类型
extra = pd.concat([df.sample(5, random_state=2), df.sample(3, random_state=3)],
                  ignore_index=True)
df_all = pd.concat([df, extra], ignore_index=True)
df_all.loc[df_all.index[-3:], "金额"] = -1          # 负数金额（刷卡异常）
df_all.loc[df_all.index[-6], "时段类型"] = None     # 缺失类别
df_all.to_csv("consumption.csv", index=False, encoding="utf-8-sig")
print(f"已生成 consumption.csv：{len(df_all)} 条原始记录")

# ========== 第2步：清洗 ==========
raw_n = len(df_all)
d = pd.read_csv("consumption.csv", parse_dates=["时间"])
d = d.dropna(subset=["时段类型"])            # 缺时段类型的记录无法分析，剔除
d = d[d["金额"] > 0]                          # 剔除负数/零金额异常
d = d.drop_duplicates()                       # 刷卡系统重传导致的重复
n_dropped = raw_n - len(d)
print(f"清洗：{raw_n} → {len(d)} 条（共剔除 {n_dropped} 条重复/缺失/负金额脏记录）")

d["日期"] = d["时间"].dt.date
d["星期"] = d["时间"].dt.dayofweek.map(
    dict(zip(range(7), ["周一", "周二", "周三", "周四", "周五", "周六", "周日"])))

# ========== 第3步：核心统计 ==========
total_spend = d["金额"].sum()
n_students = d["学号"].nunique()
print("\n========== 分析报告 ==========")
print(f"覆盖学生: {n_students} 人 | 总流水: {total_spend:.0f} 元")
print(f"人均月消费: {total_spend / n_students:.1f} 元")
print(f"单笔均值: {d['金额'].mean():.1f} 元 | 中位数: {d['金额'].median():.1f} 元")

print("\n各时段消费画像:")
profile = d.groupby("时段类型").agg(
    笔数=("金额", "count"),
    单笔均值=("金额", "mean"),
    消费总额=("金额", "sum"),
).round(1)
print(profile)

# 消费水平 top10 学生（可能暗示贫困生补助对象或大额异常）
per_stu = d.groupby("学号")["金额"].sum().sort_values()
print(f"\n消费最低5人: {[f'{k}:{v:.0f}' for k, v in per_stu.head(5).items()]}")
print(f"消费最高5人: {[f'{k}:{v:.0f}' for k, v in per_stu.tail(5).items()]}")

# ========== 第4步：可视化 ==========
# 图1：一天内消费的时间分布直方图（早中晚三峰！）
fig, ax = plt.subplots(figsize=(9, 4))
ax.hist(d["小时"], bins=48, color="tab:blue", edgecolor="white")
for h in [7.5, 12, 18]:
    ax.axvline(h, color="red", ls="--", lw=1)
ax.set_title("全天刷卡时间分布（红线=三餐理论开餐点）")
ax.set_xlabel("小时"); ax.set_ylabel("笔数")
fig.savefig("spend_hourly.png", dpi=150, bbox_inches="tight")

# 图2：四类时段的单笔均值柱状图
fig, ax = plt.subplots(figsize=(7, 4))
order = ["早餐", "午餐", "晚餐", "超市"]
means = [d.loc[d["时段类型"] == t, "金额"].mean() for t in order]
bars = ax.bar(order, means, color="tab:orange", edgecolor="black")
for b, v in zip(bars, means):
    ax.text(b.get_x() + b.get_width()/2, v + 0.2, f"{v:.1f}", ha="center")
ax.set_title("各类时段单笔平均消费"); ax.set_ylabel("元")
fig.savefig("spend_by_meal.png", dpi=150, bbox_inches="tight")

# 图3：每日总消费趋势折线
daily = d.groupby("日期")["金额"].sum()
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(range(len(daily)), daily.values, "o-", ms=3)
ax.set_title("每日总消费额（3月）")
ax.set_xlabel("3月第N天"); ax.set_ylabel("总额 元")
ax.grid(alpha=0.3)
fig.savefig("spend_daily.png", dpi=150, bbox_inches="tight")

# 图4：学生月消费分布直方图（识别低消费群体）
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(per_stu.values, bins=25, color="tab:green", edgecolor="white")
ax.axvline(per_stu.mean(), color="red", ls="--", label=f"人均 {per_stu.mean():.0f} 元")
q10 = per_stu.quantile(0.1)
ax.axvline(q10, color="purple", ls=":", lw=2, label=f"10%分位 {q10:.0f} 元")
ax.set_title("学生月消费分布（虚线可用于贫困生认定参考）")
ax.set_xlabel("月消费额"); ax.set_ylabel("人数"); ax.legend()
fig.savefig("spend_distribution.png", dpi=150, bbox_inches="tight")

plt.show()
print("\n已输出图片: spend_hourly / spend_by_meal / spend_daily / spend_distribution .png")
