# -*- coding: utf-8 -*-
"""Day 3：数据结构 —— list / tuple / dict / set 四件套
前置：无依赖，仅标准库
运行方式：python test.py（末尾综合练习需要键盘输入）
对应笔记：Python数据结构.md
"""

# ========== 1. list 列表：有序、可修改、最常用的容器 ==========
nums = [1, 2, 3]
nums.append(4)          # 末尾追加 → [1,2,3,4]
nums.insert(1, 10)      # 在下标1处插入 → [1,10,2,3,4]
nums.remove(2)          # 删除第一个值为2的元素
nums.extend([8, 9])     # 把另一个列表追加到末尾
print("list 操作后:", nums)
print("长度:", len(nums), "| 3 出现次数:", nums.count(3))

# ========== 2. 下标与切片 ==========
# ⚠️ 下标从 0 开始！负数从尾部倒数；切片含头不含尾
nums = [10, 20, 30, 40, 50]
print("\n--- 下标与切片 ---")
print(nums[0], nums[-1])      # 10 50（-1 是最后一个）
print(nums[1:3])              # [20, 30]，不包含下标3
print(nums[:2])               # [10, 20]
print(nums[::2])              # [10, 30, 50]，步长2隔一个取一个
print(20 in nums, 99 in nums) # True False（判断元素是否存在）

# 列表推导式：一行生成列表，比 for 循环简洁（进阶但极常用）
squares = [x * x for x in range(1, 6)]          # [1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]    # 带条件的推导式
print("平方:", squares, "| 偶数:", evens)

# ========== 3. tuple 元组：有序、不可修改 ==========
# 适合存"不该被改动"的数据，如坐标、日期
point = (3, 5)
print("\npoint[0] =", point[0])

# ⚠️ 单元素元组必须带逗号，否则括号会被当成普通括号
a = (3)       # 这是整数 3！
b = (3,)      # 这才是元组
print(type(a), type(b))

# 元组解包：一次性取出所有元素（Day1 交换变量 a,b=b,a 的本质）
x, y = point
print("解包:", x, y)

# ========== 4. dict 字典：键值对，按键快速查找 ==========
student = {"name": "张三", "score": 90}
print("\n--- dict ---")
print(student["name"])         # 按键取值；键不存在会报 KeyError！
print(student.get("age"))      # get 安全取值：键不存在返回 None 不报错
print(student.get("age", 18))  # 还可以指定默认值

student["score"] = 95          # 键存在 → 修改
student["city"] = "北京"       # 键不存在 → 新增

# 三种遍历姿势
for name, score in student.items():    # 最常用：键值对一起拿
    print(name, score)
# student.keys() 只拿键；student.values() 只拿值

# ========== 5. set 集合：无序、不重复，去重利器 ==========
nums2 = {1, 2, 2, 3}
print("\nset 自动去重:", nums2)        # {1, 2, 3}

a_set, b_set = {1, 2, 3, 4}, {3, 4, 5, 6}
print("并集:", a_set | b_set)          # {1,2,3,4,5,6}
print("交集:", a_set & b_set)          # {3,4}
print("差集:", a_set - b_set)          # {1,2}

# 列表去重套路：转成 set 再转回来（⚠️ 会丢失原有顺序）
unique = list(set([1, 2, 2, 3, 3, 3]))
print("去重:", unique)

# ========== 6. 通用操作：len / max / min / sum / sorted ==========
nums3 = [3, 1, 4, 1, 5]
print("\n--- 通用操作 ---")
print(len(nums3), max(nums3), min(nums3), sum(nums3))
print(sorted(nums3))              # 返回新列表，不修改原列表
print("原列表没变:", nums3)

# ========== 7. 综合练习：学生成绩统计 ==========
# 设计思路（为什么两种结构都要？）：
#   scores 用 list：方便 sum()/max()/len() 做数值统计
#   dict 的键必须唯一，同名会覆盖 —— 这里先不处理，体会即可
scores = []
students = {}

while True:
    try:
        line = input("请输入姓名和成绩（直接回车结束）：").strip()
    except EOFError:
        # 管道/重定向输入读完时会触发 EOFError，接住它优雅退出
        # （正常键盘输入不会遇到，这是防御性写法）
        break

    if not line:                 # 空行 → 结束输入
        break

    name, score_text = line.split()   # split() 按空格切成两个字符串
    score = int(score_text)           # ⚠️ split 出来的都是字符串，要转 int
    students[name] = score            # 字典存"姓名→成绩"，方便按名查找
    scores.append(score)              # 列表存所有成绩，方便整体统计

if scores:                       # 空列表的布尔值是 False，可防除零错误
    average_score = sum(scores) / len(scores)
    highest_score = max(scores)
    print("平均分：", average_score)
    print("最高分：", highest_score)
    print("录入明细:", students)
    # 找出最高分是谁：遍历字典按值比较（Day 5 会学到更简洁的写法）
    top_name = max(students, key=students.get)
    print("最高分得主:", top_name)
else:
    print("没有输入任何成绩")

# ========== 8. 练习：字符统计 ==========
# 统计一段文字里每个字符出现的次数（dict 的经典应用）
text = input("请输入一段文字：")
counts = {}
for ch in text:
    # get(ch, 0)：第一次出现时按 0 算，再 +1；比 if 判断简洁得多
    counts[ch] = counts.get(ch, 0) + 1

print("--- 字符统计结果 ---")
for ch, count in counts.items():
    print(f"{ch}: {count}")

# ========== 学习小结 ==========
# list：可变的有序数据（成绩、日志）；  tuple：固定不变的数据（坐标、配置）
# dict：按键查找（姓名→成绩、单词→词频）；  set：去重与集合运算
# 选型口诀：要顺序用 list，要查找用 dict，要唯一用 set，要冻结用 tuple
