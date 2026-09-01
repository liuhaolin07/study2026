# -*- coding: utf-8 -*-
"""Day 4：函数 —— 定义、参数、返回值、lambda、递归
前置：无依赖，仅标准库
运行方式：python test.py
对应笔记：Python函数.md
"""

# ========== 1. 函数定义与 docstring ==========
# 函数 = 把一段常用代码封装起来反复调用；先想清楚"输入是什么，输出是什么"
def greet():
    """打个招呼——三引号写的是 docstring，即函数的说明文档"""
    print("你好，Python")

greet()
print("docstring 可以用 函数.__doc__ 查看:", greet.__doc__)

# ========== 2. 参数的四种玩法 ==========
# 2.1 位置参数：按顺序一一对应
def add(a, b):
    print("位置参数:", a + b)

add(3, 5)

# 2.2 默认参数：调用时可以不传（⚠️ 默认参数必须写在普通参数后面）
def power(x, n=2):
    return x ** n

print("power(3) =", power(3))          # n 用默认值 2 → 9
print("power(3, 3) =", power(3, 3))    # n 被覆盖为 3 → 27

# 2.3 关键字参数：用"参数名=值"调用，可以不按顺序
def introduce(name, city, age=18):
    print(f"{name}，来自{city}，{age}岁")

introduce(city="上海", name="张三")     # 顺序打乱也没问题

# 2.4 可变参数：不确定个数时用 *args（收进元组）/ **kwargs（收进字典）
def total(*args):
    print("args 收到:", args)           # (1, 2, 3)
    return sum(args)

def show(**kwargs):
    print("kwargs 收到:", kwargs)       # {"name": "张三", "score": 90}

print("total =", total(1, 2, 3))
show(name="张三", score=90)

# ========== 3. 返回值 return ==========
# return 把结果交回给调用方；执行到 return 函数立刻结束
def max_value(a, b):
    if a > b:
        return a
    return b

print("max_value =", max_value(8, 12))

# 返回多个值：Python 自动打包成元组，左边用解包一次接住
def get_min_max(nums):
    return min(nums), max(nums)

low, high = get_min_max([3, 1, 9, 5])
print("最小:", low, "最大:", high)     # 1 9

# 没有 return 的函数默认返回 None（print 就是这样的函数）
print("print 的返回值:", print("这句话本身就是 print 的副作用"))

# ========== 4. 局部变量与全局变量 ==========
total = 10          # 全局变量

def add_one():
    total = 100     # 这是函数内部新建的局部变量，与外面的同名变量无关
    return total

print("函数内:", add_one())   # 100
print("函数外:", total)       # 10，全局变量没被改动
# 经验：尽量靠参数传入、return 传出，少用全局变量，程序更好理解

# ========== 5. lambda 匿名函数 ==========
# 适合只写一次的简单函数，常配合 sorted/map/filter 的 key 参数
square = lambda x: x * x
print("lambda:", square(4))    # 16，等价于 def square(x): return x*x

students = [("张三", 90), ("李四", 85), ("王五", 95)]
students.sort(key=lambda s: s[1])      # 按元组第二个元素（成绩）排序
print("按成绩排序:", students)

# ========== 6. 递归：函数调用自己 ==========
# ⚠️ 必须有终止条件，否则会无限调用直到栈溢出
def factorial(n):
    if n == 1:          # 终止条件（递归出口）
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))     # 5*4*3*2*1 = 120

# ========== 7. 练习一：排序函数 ==========
# 用 sorted() 而不是 list.sort()：返回新列表，不修改原数据（更安全）
def sort_numbers(numbers, reverse=False):
    """返回排序后的新列表；reverse=True 时降序"""
    return sorted(numbers, reverse=reverse)


nums = [12, 18, 9, 25, 30]

print("\n原列表：", nums)
print("升序：", sort_numbers(nums))
print("降序：", sort_numbers(nums, reverse=True))
print("原列表未被修改:", nums)

# ========== 8. 练习二：数据统计函数 ==========
# 一次返回多项统计结果 → 用字典装（键就是说明书，比返回一堆变量清晰）
def data_statistics(numbers):
    """返回个数/总和/平均值/最大/最小；空列表返回 None"""
    if not numbers:     # 空列表是 False：先防御，避免除零错误
        return None

    total = sum(numbers)
    count = len(numbers)

    return {
        "count": count,
        "sum": total,
        "average": total / count,
        "max": max(numbers),
        "min": min(numbers),
    }


result = data_statistics(nums)
if result:              # None 也是 False，正好用来判断"有没有统计到"
    print("\n数据个数：", result["count"])
    print("总和：", result["sum"])
    print("平均值：", result["average"])
    print("最大值：", result["max"])
    print("最小值：", result["min"])
else:
    print("列表为空")

print("空列表测试:", data_statistics([]))    # None

# ========== 9. 练习三：斐波那契数列（递归经典题） ==========
# 每一项 = 前两项之和：1, 1, 2, 3, 5, 8, 13 ...
def fib(n):
    if n <= 2:          # 终止条件：第 1、2 项都是 1
        return 1
    return fib(n - 1) + fib(n - 2)

print("\n斐波那契前 10 项:")
for i in range(1, 11):
    print(fib(i), end=" ")
print()
# 想一想：fib(35) 就会明显变慢——重复计算太多。
# 优化方向：循环递推或缓存（Day 6 学 NumPy 后再回来体会性能差距）

# ========== 学习小结 ==========
# 写函数先问：输入是什么？输出是什么？
# 参数让函数灵活：默认参数省事，*args/**kwargs 收任意多个
# return 决定输出；多返回值自动打包元组；没 return 默认返回 None
# 递归虽直观，先问自己：终止条件是什么？日常优先用循环
