# -*- coding: utf-8 -*-
"""Day 19：数据读取 csv / excel + 导出
前置：pip install pandas openpyxl   （openpyxl 是读 .xlsx 的引擎）
运行方式：python test.py（需与本文件夹的 students.csv 同目录）
"""
import pandas as pd

# ========== 1. 读取 CSV ==========
df = pd.read_csv("students.csv", encoding="utf-8")
print("--- 读入的学生表 ---")
print(df.head())
print(df.shape)

# 常用参数：
# df = pd.read_csv("students.csv",
#                  encoding="utf-8",     # 中文乱码时先试 utf-8，再试 gbk
#                  index_col="学号",      # 指定某列做行索引
#                  nrows=5)              # 只读前几行（大文件预览用）

# ========== 2. Excel 的读写 ==========
# 先把 csv 转存成 xlsx，再读回来（演示完整闭环）
df.to_excel("students.xlsx", sheet_name="成绩表", index=False)
df2 = pd.read_excel("students.xlsx")
print("\n--- 从 xlsx 读回 ---")
print(df2.head(3))
# 若报 ImportError: 缺少 openpyxl → pip install openpyxl

# ========== 3. 导出 ==========
# to_csv / to_excel；index=False 表示不把行索引写进文件
# encoding="utf-8-sig"：让 Windows Excel 双击打开中文不乱码
df.to_csv("students_backup.csv", index=False, encoding="utf-8-sig")
print("\n已导出 students_backup.csv")

# ========== 4. 读进来之后的老三样 ==========
print("\n--- 检查数据 ---")
df.info()                      # 有没有缺失？类型对不对？
print(df.describe().round(1))  # 数值列速览

# ========== 5. 小分析：每班人数与各科平均分 ==========
print("\n按班级汇总:")
print(df.groupby("班级")[["语文", "数学", "英语"]].mean().round(1))
print("\n每班人数:")
print(df["班级"].value_counts())

# ========== 今日练习 ==========
# 1) 只读取"学号/姓名/数学"三列（提示：usecols 参数）
cols = pd.read_csv("students.csv", usecols=["学号", "姓名", "数学"])
print("\n练习-usecols:\n", cols.head(3))

# 2) 把每人的三科总分追加成新列，导出成 total.xlsx
df["总分"] = df[["语文", "数学", "英语"]].sum(axis=1)
df.to_excel("total.xlsx", index=False)
print("已导出 total.xlsx（含总分列）")
print(df[["姓名", "总分"]].sort_values("总分", ascending=False).head(3))
