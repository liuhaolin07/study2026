# -*- coding: utf-8 -*-
"""Day 5：文件和模块——连接"程序"与"数据"的桥梁
为什么学：数据不会永远躺在代码里；真实的分析任务都是从读文件开始。
运行方式：在本文件夹打开终端，执行  python test.py
配套数据：scores.txt（文本成绩单）、scores.csv（CSV 成绩单）
"""

# ========== 1. 写入文本文件 ==========
# "w" 是覆盖写入；"a" 是追加写入；还有 "r" 读、"b" 二进制模式（图片/表格用）
# encoding="utf-8" 一定要写！否则 Windows 默认 GBK，容易乱码/报错。
# 原因：GBK 字库不全，遇到特殊字符（如 emoji）直接报 UnicodeEncodeError；
# utf-8 能表示所有 Unicode 字符，跨平台通用，读和写要用同一编码
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
    f.write("第二行：文件操作\n")

print("已写入 hello.txt")

# ========== 2. 读取文本文件的三种方式 ==========
# 方式一：read() 一次读全部（适合小文件）
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("--- read() 全部读取 ---")
print(content)

# 方式二：readlines() 按行读成列表（注意每行末尾带 \n）
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print("--- readlines() ---")
print(lines)

# 方式三：for line in f 逐行遍历（推荐！内存占用小，多大文件都行）
print("--- for line in f ---")
with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip() 去掉行首尾空白和换行符

# ========== 3. CSV 文件读取 ==========
import csv

# csv.reader：每一行解析成一个列表
print("--- csv.reader ---")
with open("scores.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # 第一行是表头，先单独取出
    print("表头:", header)
    for row in reader:
        print(row)

# csv.DictReader：每一行解析成字典，直接用列名取值（更好用，推荐）
print("--- csv.DictReader ---")
with open("scores.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["姓名"], "的数学成绩:", row["数学"])

# ========== 4. 追加模式 ==========
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("程序运行时追加的一条日志\n")
print("已向 log.txt 追加一行（多运行几次试试）")

# ========== 5. 模块导入 ==========
# 5.1 标准库：Python 自带，import 就能用
import math
import random
import os

print("--- 标准库 ---")
print("math.sqrt(2) =", math.sqrt(2))
print("math.pi =", math.pi)
print("random.randint(1, 6) =", random.randint(1, 6))  # 掷骰子
print("当前文件夹里的文件:", os.listdir("."))

# 5.2 三种导入写法
from math import sqrt          # 只导入单个函数，之后直接写 sqrt
import math as m               # 起别名
print("sqrt(16) =", sqrt(16), "| m.floor(3.7) =", m.floor(3.7))

# 5.3 导入自己写的模块（同文件夹下的 my_utils.py）
# 模块搜索顺序：脚本所在文件夹 → PYTHONPATH 环境变量 → 标准库目录 → site-packages
# 所以"先 cd 到当天文件夹再运行"不只是路径问题，也保证模块能被找到；
# ⚠️ 模块文件名别和标准库重名（如 math.py），否则 import 会先找到你自己的文件
from my_utils import average, max_min

print("--- 自定义模块 my_utils ---")
nums = [90, 85, 78, 92, 66]
print("平均分:", average(nums))
high, low = max_min(nums)
print("最高分:", high, "最低分:", low)

# ========== 6. 今日练习：读取成绩文件并分析 ==========
print("=" * 40)
print("练习：读取 scores.txt，统计平均分、最高分并排名")

results = {}  # 姓名 -> 分数
with open("scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()      # 按空格切成 ["张三", "90"]
        if len(parts) == 2:               # 跳过空行、坏行
            name, score = parts[0], int(parts[1])
            results[name] = score

avg = average(list(results.values()))
top_name = max(results, key=results.get)  # 按值找最大的键
print(f"共 {len(results)} 名学生，平均分 {avg:.2f}")
print(f"最高分：{top_name} {results[top_name]} 分")

print("--- 排名榜 ---")
ranked = sorted(results.items(), key=lambda kv: kv[1], reverse=True)
for rank, (name, score) in enumerate(ranked, start=1):
    print(f"{rank}. {name} {score}")

# 进阶：读取 scores.csv，算每人三科总分并排序
print("=" * 40)
print("进阶：读取 scores.csv，按三科总分排名")
rows = []
with open("scores.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        total = int(row["语文"]) + int(row["数学"]) + int(row["英语"])
        rows.append((row["姓名"], total))

for name, total in sorted(rows, key=lambda t: t[1], reverse=True):
    print(name, total)
