# -*- coding: utf-8 -*-
"""Day 16-17 项目：天气数据可视化
流程：生成模拟数据 → 保存 csv → pandas/numpy 分析 → 四张图
前置：pip install numpy matplotlib pandas
运行方式：python weather_project.py
产出：weather.csv 及 4 张 png
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ========== 第1步：生成一年的模拟天气数据 ==========
rng = np.random.RandomState(2024)
days = pd.date_range("2024-01-01", periods=365)

# 用正弦波模拟季节温度（夏天高冬天低）+ 噪声
t = np.arange(365)
temp_high = 22 + 12 * np.sin((t - 105) / 365 * 2 * np.pi) + rng.normal(0, 3, 365)
temp_low = temp_high - rng.uniform(6, 12, 365)

# 降雨：夏季概率更高
rain_prob = 0.25 + 0.2 * np.clip(np.sin((t - 120) / 365 * 2 * np.pi), 0, None)
rain = (rng.rand(365) < rain_prob) * rng.exponential(5, 365).round(1)

weather = pd.DataFrame({
    "日期": days.strftime("%Y-%m-%d"),
    "最高温": temp_high.round(1),
    "最低温": temp_low.round(1),
    "降雨量": rain,
})
weather.to_csv("weather.csv", index=False, encoding="utf-8-sig")
print(f"已生成 weather.csv，共 {len(weather)} 天")
print(weather.head())

# ========== 第2步：读取并预处理 ==========
df = pd.read_csv("weather.csv", parse_dates=["日期"])
df["月份"] = df["日期"].dt.month
monthly = df.groupby("月份")[["最高温", "最低温", "降雨量"]].mean()
print("\n各月平均:")
print(monthly.round(1))

# ========== 第3步：可视化 ==========
# 图1：全年温度变化折线
fig, ax = plt.subplots(figsize=(11, 4.5))
ax.plot(df["日期"], df["最高温"], lw=0.8, color="tab:red", label="最高温")
ax.plot(df["日期"], df["最低温"], lw=0.8, color="tab:blue", label="最低温")
ax.fill_between(df["日期"], df["最低温"], df["最高温"], color="tab:orange", alpha=0.15)
ax.axhline(0, color="gray", lw=0.8)
ax.set_title("2024年每日温度变化（模拟数据）")
ax.set_ylabel("温度 ℃"); ax.legend(); ax.grid(alpha=0.3)
fig.autofmt_xdate()                       # 日期标签自动倾斜
fig.savefig("weather_temp.png", dpi=150, bbox_inches="tight")

# 图2：月均温度对比柱状图
fig, ax = plt.subplots(figsize=(9, 4))
xpos = np.arange(12)
w = 0.38
ax.bar(xpos - w/2, monthly["最高温"], w, label="平均最高温", color="tab:red", alpha=0.85)
ax.bar(xpos + w/2, monthly["最低温"], w, label="平均最低温", color="tab:blue", alpha=0.85)
ax.set_xticks(xpos, [f"{m}月" for m in range(1, 13)])
ax.set_ylabel("温度 ℃"); ax.set_title("各月平均温度")
ax.legend(); ax.grid(axis="y", alpha=0.3)
fig.savefig("weather_monthly.png", dpi=150, bbox_inches="tight")

# 图3：降雨趋势——月降雨总量 + 有雨天数
fig, ax1 = plt.subplots(figsize=(9, 4.5))
rain_sum = df.groupby("月份")["降雨量"].sum()
rain_days = df[df["降雨量"] > 0].groupby("月份").size().reindex(range(1, 13), fill_value=0)
ax1.bar(xpos, rain_sum, color="tab:cyan", alpha=0.8, label="月总降雨量(mm)")
ax1.set_xlabel("月份"); ax1.set_ylabel("总降雨量 mm")
ax2 = ax1.twinx()                          # 双 y 轴
ax2.plot(xpos, rain_days, "o-", color="tab:red", label="有雨天数")
ax2.set_ylabel("天数")
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
ax1.set_title("降雨趋势（左轴：雨量，右轴：雨日）")
fig.savefig("weather_rain.png", dpi=150, bbox_inches="tight")

# 图4：降雨量分布直方图（绝大多数天没雨 → 右偏分布）
fig, ax = plt.subplots(figsize=(7, 4))
rainy = df.loc[df["降雨量"] > 0, "降雨量"]
ax.hist(rainy, bins=25, color="tab:cyan", edgecolor="white")
ax.set_title(f"有雨日的日降雨量分布（共 {len(rainy)} 个雨天）")
ax.set_xlabel("日降雨量 mm"); ax.set_ylabel("天数")
fig.savefig("weather_rain_hist.png", dpi=150, bbox_inches="tight")

print("\n已输出图片: weather_temp / weather_monthly / weather_rain / weather_rain_hist .png")
plt.show()

# ========== 思考题 ==========
# 1) 最热的一天是几号？最长的连续降雨有多少天？（提示：groupby + cumsum 技巧）
# 2) 把城市改成南方城市（更热更湿），只需改哪些参数？
