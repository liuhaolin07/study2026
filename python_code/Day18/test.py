# -*- coding: utf-8 -*-
"""Day 18：DataFrame 入门
前置：pip install pandas
运行方式：python test.py
"""
import pandas as pd
import numpy as np

# ========== 1. 什么是 Series / DataFrame ==========
# Series：一列（带索引的一维数据）
s = pd.Series([90, 85, 78], index=["张三", "李四", "王五"], name="数学")
print("--- Series ---")
print(s)

# DataFrame：一张表（多个 Series 共用行索引）
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "钱七"],
    "性别": ["男", "女", "男", "男", "女"],
    "年龄": [18, 19, 20, 17, 19],
    "语文": [90, 85, 78, 92, 66],
    "数学": [85, 72, 90, 88, 75],
})
print("\n--- DataFrame ---")
print(df)

# ========== 2. 查看数据的六个常用方法 ==========
print("\n--- 快速查看 ---")
print(df.head(3))          # 前3行（默认前5）
print(df.tail(2))          # 后2行
print(df.shape)            # (5, 5) 行数, 列数
print(df.columns.tolist()) # 所有列名
print(df.dtypes)           # 每列的数据类型

print("\ninfo() 总览:")
df.info()                  # 行数、缺失情况、内存——读进新表第一件事！

print("\ndescribe() 数值列统计:")
print(df.describe())       # count/mean/std/min/四分位/max 一表全出

# ========== 3. 取一列、取多列 ==========
math = df["数学"]              # 一列 → Series
subset = df[["姓名", "数学"]]  # 多列 → 双中括号 → 还是 DataFrame
print("\n取一列:\n", math.head(3))
print("取多列:\n", subset)

# 新增一列：直接赋值（向量化计算）
df["总分"] = df["语文"] + df["数学"]
df["平均分"] = df["总分"] / 2
print("\n新增列后:\n", df[["姓名", "总分", "平均分"]])

# ========== 4. 索引与 loc / iloc 预告 ==========
# 默认行索引是 0,1,2,...；也可以指定有意义的索引
df2 = df.set_index("姓名")
print("\n把姓名设为索引后:")
print(df2.loc["张三"])          # 按标签取一行
print(df2.iloc[0])              # 按位置取第0行，效果一样

# ========== 5. 简单统计 ==========
print("\n简单统计:")
print("数学最高:", df["数学"].max())
print("年龄均值:", df["年龄"].mean().round(2))
print("性别计数:")
print(df["性别"].value_counts())   # 类别频数统计（超常用）

# ========== 今日练习 ==========
# 用字典造一张 4 行的"图书表"：书名/价格/库存，然后：
# 1) 打印 info 和 describe；2) 加一列"总价值=价格×库存"；3) 找出最贵的书
books = pd.DataFrame({
    "书名": ["Python编程", "线性代数", "概率论", "机器学习"],
    "价格": [79.0, 45.0, 39.5, 89.0],
    "库存": [12, 30, 25, 8],
})
books["总价值"] = books["价格"] * books["库存"]
print("\n练习-图书表:")
print(books)
print("最贵的书:", books.loc[books["价格"].idxmax(), "书名"])
