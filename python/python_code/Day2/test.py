# -*- coding: utf-8 -*-
"""Day 2：条件与循环 —— if 分支、for/while、break/continue
前置：无依赖，仅标准库
运行方式：python test.py（猜数字环节需要键盘输入）
对应笔记：Python条件与循环.md
"""

# ========== 1. if / elif / else ==========
# 判断从上往下走，命中一个分支就不再继续
score = 85
if score >= 90:
    print("优秀")
elif score >= 60:          # elif 可以有多个
    print("及格")
else:                      # else 只能有一个，兜底所有剩余情况
    print("不及格")

# 嵌套 if 可以用"链式比较"写得更简洁（Python 特色写法）
age = 20
if 18 <= age < 60:         # 等价于 age >= 18 and age < 60
    print("成年且未退休")

# ⚠️ 条件后必须有冒号，下一行必须缩进（Python 用缩进表示代码块）

# ========== 2. range() 生成整数序列 ==========
# range(结束) / range(开始, 结束) / range(开始, 结束, 步长)
# ⚠️ 都是"含头不含尾"：包含开始，不包含结束
print("\n--- range 三件套 ---")
print(list(range(5)))          # [0, 1, 2, 3, 4]  从0开始
print(list(range(2, 8)))       # [2, 3, 4, 5, 6, 7]
print(list(range(1, 10, 2)))   # [1, 3, 5, 7, 9]  步长2 → 奇数
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]  步长可以为负 → 倒着数

# ========== 3. break 与 continue ==========
# break：立刻结束整个循环；continue：跳过本轮，进入下一轮
print("\n--- break / continue ---")
for i in range(1, 10):
    if i == 3:
        continue    # 跳过 3，不打印
    if i == 7:
        break       # 到 7 整个循环结束
    print(i, end=" ")   # 输出 1 2 4 5 6
print()

# for-else：循环"没被 break 打断"时才执行 else（常用于搜索场景）
for i in range(2, 6):
    if i == 99:
        break
else:
    print("循环正常结束，没有触发 break")

# ========== 4. 练习一：输出 100 以内的素数 ==========
# 素数：只能被 1 和自身整除的大于 1 的整数
# 关键优化：只需试除到 √num。因为如果 num = a×b，a、b 不可能都大于 √num，
# 所以只要 2~√num 里没有因子，更大的范围也一定没有
print("\n--- 100 以内的素数 ---")
for num in range(2, 101):
    is_prime = True                          # 先假设是素数（标志位技巧）
    for i in range(2, int(num ** 0.5) + 1):  # 试除 2 到 √num
        if num % i == 0:                     # 找到因子 → 不是素数
            is_prime = False
            break                            # 提前退出内层循环，省时
    if is_prime:
        print(num, end=" ")                  # end=" " 让结果横排显示
print()

# ========== 5. 练习二：猜数字游戏（while True 模式） ==========
# 循环次数未知时用 while；while True 死循环 + 条件成立时 break 是经典套路
import random

number = random.randint(1, 100)   # 随机生成 [1,100] 的整数（含两端）
count = 0
print("\n--- 猜数字（心里想好了 1~100 之间的数）---")
while True:
    guess = int(input("请输入 1 到 100 的整数："))
    count += 1
    if guess < number:
        print("太小了")
    elif guess > number:
        print("太大了")
    else:                          # 猜对了才 break，否则一直循环
        print("猜对了！")
        print("你一共猜了", count, "次")
        break

# ========== 6. 练习三：九九乘法表（双层 for 循环） ==========
# 外层 i 控制行，内层 j 控制每行打印的式子
# j 只循环到 i：避免重复（3*5 和 5*3 只保留一个），输出是三角形
print("\n--- 九九乘法表 ---")
for i in range(1, 10):
    for j in range(1, i + 1):
        # \t 是制表符，让每列对齐；end="" 阻止换行，一行式子连排
        print(f"{j}*{i}={i * j}\t", end="")
    print()                        # 空 print 只负责换行，进入下一行

# ========== 7. 练习四：水仙花数 ==========
# 三位数且各位数字的立方和等于自身，如 153 = 1³ + 5³ + 3³
# 拆位技巧：// 取高位，% 取低位
print("--- 三位水仙花数 ---")
for num in range(100, 1000):
    hundreds = num // 100          # 百位：153 // 100 = 1
    tens = num // 10 % 10          # 十位：153 // 10 = 15，再 % 10 = 5
    ones = num % 10                # 个位：153 % 10 = 3
    if hundreds ** 3 + tens ** 3 + ones ** 3 == num:
        print(num, end=" ")        # 153 370 371 407
print()

# ========== 学习小结 ==========
# if 处理分支，注意判断顺序和缩进
# for 适合固定次数/遍历，while 适合次数未知（别忘了让条件能变化，防死循环）
# break 结束整个循环，continue 只跳过本轮
# range 含头不含尾；拿不准边界就 list(range(...)) 打出来看一眼
