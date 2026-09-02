# -*- coding: utf-8 -*-
"""Day 2 草稿本（prac = practice）
定位：学 if 语句时的第一次试手。最简单的两分支判断。
"""

age = 18
if age >= 18:            # 条件成立（True）走 if 块
    print("成年了")
else:                    # 条件不成立（False）走 else 块
    print("未成年")

# 注意三点（新手最容易踩）：
# 1) if 条件后面要写冒号 :
# 2) 下一行要缩进（4 个空格），Python 靠缩进区分代码块
# 3) 判断"相等"用 ==，单个 = 是赋值，写混了是经典错误

# 进阶写法：多档判断用 elif（详见 test.py 第 1 节）

if 18<= age < 60:         # 链式比较，等价于 age >= 18 and age < 60
    print("成年且未退休")

for i in range(1, 10):    # range(1, 10) 生成 1~9 的整数序列,左闭右开
    print(i)    #自动换行输出 1~9
print("循环结束")
for i in range(10):    # range(10) 生成 0~9 的整数序列
    print(i,end=" ")    # 不换行输出 0~9
print("\n循环结束")    # \n 换行

for i in range(1, 10):
    if i == 3:
        continue    # 跳过 3
    if i == 7:
        break       # 到 7 就停
    print(i)        # 输出 1 2 4 5 6

for i in range(2, 6):
    if i == 3:
        break
else:
    print("循环正常结束，没有触发 break")

# 在for-else语句中， 如果循环正常结束（没有遇到break），则执行else块

#list表示列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit=="banana":
        break
else:
    print("循环正常结束")

# 列表（list）：不要用 list 当变量名，会遮蔽内置类型
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

print(list(range(10)))
print(list(numbers))
print(numbers)

#练习一：输出 100 以内的素数
for num in range(2,101):
    is_prime=0
    # for i in range(2,num):
    for i in range(2,int(num*0.5)+1):
        if num%i==0:
            is_prime=1
            break
    if is_prime==0:
        print(num,end=" ")

#练习二：猜数字游戏
import random
target = random.randint(1, 100)
print("欢迎来到猜数字游戏！")
count=0
while True:
    guess = int(input("请输入你的猜测："))
    count += 1
    if guess == target:
        print("恭喜你，猜对了！")
        print(f"你一共猜了 {count} 次")
        break
    elif guess < target:
        print("太小了，请再试一次。")
    else:
        print("太大了，请再试一次。")

#练习三：九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}×{i}={i*j}", end=" ")
    print() #输出即会换行

# //表示整数除法，返回商的整数部分
print(10 // 3) # 输出 3
print(10 / 3)  # 输出 3.3333333333333335
