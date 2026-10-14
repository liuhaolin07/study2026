# -*- coding: utf-8 -*-
"""Day 20：数据清洗——缺失值 / 重复值 / 异常值
前置：pip install pandas
运行方式：python test.py（需与 messy_students.csv 同目录）
"""
import pandas as pd

# ========== 0. 先看数据有多“脏” ==========
df = pd.read_csv("messy_students.csv", dtype=str)   # 先全部按字符串读入，避免自动转换干扰
print("--- 原始数据 ---")
print(df)
print("\n各列缺失数:")
print(df.isnull().sum())          # isnull 标记缺失，sum 按列计数

# 这份脏数据包含四类问题：
# ① 姓名带多余空格：" 李四 "
# ② 完全重复的行：张三、李四 各出现两次
# ③ 缺失值：王五的性别和成绩是空
# ④ 异常/非法值：钱七年龄 -5；孙八年龄 "十九"（文字）

# ========== 1. 字符串清理：去空格 ==========
# df["列"].str.xxx 是对整列字符串批量操作（str 访问器）
df["姓名"] = df["姓名"].str.strip()
df["性别"] = df["性别"].str.strip()
print("\n--- 姓名去空格后 ---")
print(df)

# ========== 2. 数值列转换：to_numeric + coerce ==========
# "十九" 不是数字，errors="coerce" 会把它变成 NaN（转不动的都变缺失）
df["年龄"] = pd.to_numeric(df["年龄"], errors="coerce")
df["成绩"] = pd.to_numeric(df["成绩"], errors="coerce")
print("\n--- 转数值后（注意孙八的年龄变成了 NaN）---")
print(df.dtypes)
print(df)

# ========== 3. 删除重复行 ==========
print("\n重复行数量:", df.duplicated().sum())
df = df.drop_duplicates()
print("--- 去重后 ---")
print(df)

# ========== 4. 处理缺失值 ==========
# 策略A：dropna 丢弃（数据量大时简单粗暴）
df_drop = df.dropna()
print("\n策略A dropna 后:", df_drop.shape[0], "行")

# 策略B：fillna 填充（更常用！）
#   性别(类别型) → 众数填充；年龄 → 中位数；成绩 → 平均分
df_fill = df.copy()     # ⚠️ copy() 很关键：不拷贝的话两个变量共享同一块数据，
                        # 后面改 df_fill 会连带把策略A的基线也污染（视图/副本问题）
df_fill["性别"] = df_fill["性别"].fillna(df_fill["性别"].mode()[0])
df_fill["年龄"] = df_fill["年龄"].fillna(df_fill["年龄"].median())
df_fill["成绩"] = df_fill["成绩"].fillna(df_fill["成绩"].mean().round(1))
print("策略B fillna 后:")
print(df_fill)
# 注意：此时孙八年龄仍是 NaN（他不是缺失而是非法），下一步处理

# ========== 5. 处理异常值 ==========
# 年龄合理范围 [15, 60]：越界的一律置 NaN 再用中位数填
mask_bad = (df_fill["年龄"] < 15) | (df_fill["年龄"] > 60)
print("\n异常年龄的行:\n", df_fill[mask_bad])
# 用 .loc 一步到位改值：避免链式赋值（见 Day 18 的 SettingWithCopyWarning 陷阱）
df_fill.loc[mask_bad, "年龄"] = df_fill["年龄"].median()

print("\n--- 最终干净数据 ---")
print(df_fill)
print("剩余缺失总数:", int(df_fill.isnull().sum().sum()))

# ========== 6. 导出干净数据 ==========
df_fill.to_csv("clean_students.csv", index=False, encoding="utf-8-sig")
print("\n已导出 clean_students.csv")

# ========== 今日练习 ==========
# 在上面第4步里把“成绩”改成用中位数填充，对比平均分填充的差异；
# 思考：什么情况下选 dropna，什么情况下选 fillna？
