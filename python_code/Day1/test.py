# -*- coding: utf-8 -*-
"""Day 1：Python 基础语法 —— 变量、类型、输入输出、运算符
前置：无依赖，仅标准库
运行方式：python test.py（末尾有 input()，运行时需要键盘输入）
对应笔记：Python基础语法.md
"""

# ========== 1. 变量 ==========
# 变量就是给数据起的"名字"，Python 不需要提前声明类型，赋值即创建
name = "Alice"          # str 字符串：必须用引号包住（单引号 '...' 也行）
age = 18                # int 整数
score = 95.5            # float 小数
is_adult = True         # bool 布尔：只有 True / False 两个值（首字母大写！）

# 命名规则：只能含字母/数字/下划线，不能数字开头，不能用关键字（如 if、for）
# 好习惯：变量名要有意义，多个单词用下划线连接（snake_case），如 student_name

# ========== 2. type() 查看类型 ==========
print("--- type() 查看类型 ---")
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(score))      # <class 'float'>
print(type(is_adult))   # <class 'bool'>

# ========== 3. 类型转换 ==========
print("\n--- 类型转换 ---")
a = int("42")           # 字符串 → 整数
b = float("3.5")        # 字符串 → 小数
c = str(100)            # 整数 → 字符串（拼接时常用）
d = int(3.9)            # 小数 → 整数：直接截断小数部分，不是四舍五入！
print(a, b, c, d)       # 42 3.5 100 3

# ⚠️ 不是所有字符串都能转数字：int("abc") 会直接报 ValueError
# 下面用 try/except 接住错误，让演示程序不至于崩溃
# （异常处理后面阶段会细讲，这里只需知道它能"试错而不崩溃"）
try:
    int("abc")
except ValueError:
    print('int("abc") 报错被捕获：不是数字的字符串没法转成 int')

# ========== 4. 字符串格式化 ==========
print("\n--- 字符串格式化 ---")
# f-string（Python 3.6+，最推荐）：字符串前加 f，{} 里直接放变量或表达式
print(f"{name}考了{score}分")
print(f"保留两位小数：{3.14159:.2f}")       # :.2f 表示保留 2 位小数
print(f"明年{age + 1}岁")                    # {} 里可以写表达式

# 两种旧写法（老代码里会遇到，了解即可）
print("姓名：%s" % name)                     # % 占位符
print("姓名：{}".format(name))               # format() 方法

# ========== 5. 输出 print ==========
print("\n--- print 的参数 ---")
print("Hello, Python")
print("a =", 10)                  # 多个值默认用空格隔开
print("a", "b", "c", sep="-")     # sep 指定分隔符 → a-b-c
print("等待", end="...")          # end 指定结尾（默认是换行）
print("完成")                      # 接上一行后面：等待...完成

# ========== 6. 输入 input ==========
print("\n--- input 输入 ---")
# ⚠️ 核心坑：input() 返回的一定是字符串！要做数值计算必须先转换
name = input("请输入你的名字：")
print("你好，", name)

age = int(input("请输入年龄："))        # 不套 int() 的话，下面 +1 会报错
print("明年", age + 1, "岁")

# ========== 7. 运算符 ==========
print("\n--- 运算符 ---")
# 算术：+ - * /（结果是小数） //（整除） %（取余） **（幂）
print("7 / 2 =", 7 / 2)          # 3.5
print("7 // 2 =", 7 // 2)        # 3，向下取整
print("7 % 2 =", 7 % 2)          # 1，余数（判断奇偶常用）
print("2 ** 3 =", 2 ** 3)        # 8

x = 10
x += 5                            # 等价于 x = x + 5，其余 -= *= /= 同理
print("x += 5 后:", x)

# 字符串也能"运算"：+ 拼接，* 重复
print("abc" + "def")             # abcdef
print("ha" * 3)                  # hahaha

# 比较运算符结果是 bool：== != > < >= <=
# 逻辑运算符：and（都真才真）、or（一真即真）、not（取反）
age = 20
print(age > 18 and age < 30)     # True
print(age < 18 or age > 60)      # False
print(not age > 18)              # False

# 记不住优先级就加括号，永远不会错：
print((2 + 3) * 4)               # 20

# ========== 8. 注释 ==========
# 单行注释：井号开头，不参与运行，给人和自己看
"""
多行说明：三个引号包起来，
常用来写文件或函数的说明文档。
"""

# ========== 今日练习 ==========
# 练习1：温度转换（公式 F = C * 9 / 5 + 32）
celsius = float(input("请输入摄氏度："))     # 注意用 float，小数温度也兼容
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}℃ = {fahrenheit:.1f}℉")

# 练习2：交换两个变量（Python 一行搞定，本质是元组解包，Day 3 细讲）
a = int(input("请输入 a："))
b = int(input("请输入 b："))
a, b = b, a
print("交换后 a =", a, "b =", b)

# 练习3：简单计算器（用到 if 分支，Day 2 会细讲）
num1 = float(input("请输入第一个数字："))
op = input("请输入运算符(+ - * /)：")
num2 = float(input("请输入第二个数字："))
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    result = "运算符错误"
print("结果：", result)
