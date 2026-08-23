# 练习：输出素数
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

# 练习：猜数字游戏
import random

number = random.randint(1, 100)
count = 0

while True:
    guess = int(input("请输入 1 到 100 的整数："))
    count += 1
    if guess < number:
        print("太小了")
    elif guess > number:
        print("太大了")
    else:
        print("猜对了！")
        print("你一共猜了", count, "次")
        break

# 练习：九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}*{j}={i * j}\t", end="")
    print()
