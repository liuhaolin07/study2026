# -*- coding: utf-8 -*-
"""Day 1 草稿本（prac = practice）
定位：学完 test.py 后自己动手试写的探索记录，保留原样思路并逐行加注释。
对照阅读：先看 test.py 的规范写法，再看这里"想到哪写到哪"的过程，体会差异。
"""

# ---------- 变量与比较 ----------
name = "haolin"      # 字符串
age = 20             # 整数
score = 99.99        # 小数

# int 和 float 可以直接比较（20 < 99.99 成立）；
# 这个判断本身没有实际意义，只是试试 if 的语法
if age < score:
    print(name)

print(type(name))    # <class 'str'>
print(age)
# ⚠️ int("abc") 会报 ValueError：只有长得像数字的字符串才能转
#    （test.py 第 3 节里用 try/except 演示了这个报错）

# ---------- f-string ----------
print(f"{name} is {age} years old")
# 加 f 告知解释器：{} 会被求值后替换成结果

print(b"{name} is {age} years old")
# 解答当年的疑问：前缀 b 表示 bytes（字节串），不是 f-string！
# 字节串里 {name} 会原样输出，不做插值。它存的是原始字节（0~255），
# 用于文件读写、网络传输等需要"字节"的场合；文本处理用普通字符串即可。

# ---------- print 的常见写法 ----------
print(1, 2, 3)                  # 多个值默认用空格隔开
print("a=", 20)

# name = input("输入你的名字：")
# age = int(input("请输入年龄："))
# ⚠️ input() 返回的一定是字符串；要做数值运算必须套 int()/float()
# int() 对小数是"截断"（类似 C 语言的强转）：int(3.9) → 3，不是四舍五入
# （这两行被注释掉，避免草稿脚本运行时卡在等待输入）

print("a", "b", "c")            # 多个值默认用空格隔开
print("a", "b", sep="-")        # sep 指定分隔符
print("等待", end="...")        # end 指定结尾（默认换行）
print()

# ---------- 算术与逻辑 ----------
print(20 // 3)                  # 整除 → 6
print(3 ** 2)                   # 幂 → 9

print(age > 18 and age < 30)    # True：and 要求两边都真
print(age < 18 or age > 60)     # False：or 只需一边为真
print(not age > 18)             # False：not 取反

"""
多
行
注
释：三引号包起来，不参与运行
"""

# ---------- 练习一：摄氏 → 华氏 ----------
# 公式：F = C * 9/5 + 32
c = float(input("输入摄氏度："))    # 用 float 兼容小数输入
f = c * 9 / 5 + 32
print(f"华氏度：{f}")

# ---------- 练习二：简单计算器 ----------
# 思路：两个数 + 一个运算符，用 if/elif 分支匹配运算符
num1 = float(input("number1:"))
op = input("运算符：")
num2 = float(input("number2:"))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)            # 若 num2=0 会报 ZeroDivisionError
else:
    print("error")

# ---------- 练习三：交换两个变量 ----------
a = int(input("a="))      # 一定要套 int()，input 返回的是字符串
b = int(input("b="))

a, b = b, a               # Python 一行交换：右侧先打包成元组，再解包赋值
# 其他语言常要借助临时变量：t=a; a=b; b=t，Python 不需要

print("交换后 a =", a)
print("交换后 b =", b)

a, b = b, a               # 再交换一次就换回来了
print("再交换 a =", a, "b =", b)
