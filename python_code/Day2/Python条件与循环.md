# Python条件与循环

## 1. if 语句

### 基本结构

```python
age = 18
if age >= 18:
    print("成年人")
else:
    print("未成年人")
```

### 多分支

```python
score = 85
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

### 嵌套 if

条件里再套条件：

```python
age = 20
if age >= 18:
    if age < 60:
        print("成年且未退休")
    else:
        print("已退休")
else:
    print("未成年人")
```

也可以用 `and` 写成一行：

```python
if 18 <= age < 60:
    print("成年且未退休")
```

### 注意

- `elif` 可以有多个，`else` 只能有一个
- 判断顺序从上往下，命中一个就不再继续
- 条件后面必须有冒号，下一行要缩进

## 2. for 循环

for 循环常用于遍历序列。

```python
for i in range(5):
    print(i)
```

### 例子：遍历字符串

```python
for ch in "Python":
    print(ch)
```

### break 和 continue

- `break`：立刻结束整个循环
- `continue`：跳过本次循环，直接进入下一次

```python
for i in range(1, 10):
    if i == 3:
        continue    # 跳过 3
    if i == 7:
        break       # 到 7 就停
    print(i)        # 输出 1 2 4 5 6
```

### for-else
当循环正常结束（即没有被 `break` 中断）时，会执行 `else` 代码块：

```python
for i in range(2, 6):
    if i == 3:
        break
# 注意：这里的 else 与 for 对齐（顶格），因此它是 for...else 结构。
# 在 Python 中，else 和谁搭配完全由缩进决定，没和 if 对齐就不会和 if 搭配。
else:
    print("循环正常结束，没有触发 break")
```

## 3. while 循环

while 循环会一直执行，直到条件不满足为止。

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

### 注意

- 循环体内要有让条件变化的语句，否则会死循环
- **不确定循环次数时优先用 while**

### break 与 continue 同样适用

```python
total = 0
while True:
    n = int(input("输入一个数字（输入 0 结束）："))
    if n == 0:
        break          # 结束循环
    if n < 0:
        continue       # 负数不累加
    total += n
print("总和：", total)
```

## 4. range()

range() 用来生成一段整数序列。

```python
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(2, 8)))       # [2, 3, 4, 5, 6, 7]
print(list(range(1, 10, 2)))   # [1, 3, 5, 7, 9]
print(list(range(10, 0, -2)))  # 步长可以是负数：[10, 8, 6, 4, 2]
```

`range(开始, 结束, 步长)` 注意：
- 包含开始，不包含结束，即左闭右开
- 步长为正递增，为负递减

## 5. 练习一：输出素数

素数是只能被 1 和自身整除的整数。

```python
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
```

## 6. 练习二：猜数字游戏

```python
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
```

## 7. 练习三：九九乘法表

```python
for i in range(1, 10):
    for j in range(1, i + 1):      # j 只到 i，避免重复
        print(f"{j}*{i}={i*j}\t", end="")
    print()
```

输出会是一份三角，例如前几行：

```text
1*1=1
1*2=2	2*2=4
1*3=3	2*3=6	3*3=9
```

## 8. 练习四：水仙花数

### 题目

水仙花数是三位数，且各位数字的立方和等于它本身，例如 `153 = 1³ + 5³ + 3³`。输出所有三位水仙花数。

### 参考思路

- 用 `range(100, 1000)` 遍历所有三位数
- 用 `//` 和 `%` 拆出百位、十位、个位
- 判断立方和是否等于原数

### 参考代码

```python
for num in range(100, 1000):
    hundreds = num // 100        # 百位
    tens = num // 10 % 10        # 十位
    ones = num % 10              # 个位
    if hundreds ** 3 + tens ** 3 + ones ** 3 == num:
        print(num, end=" ")
```

## 9. 学习小结

- if 用来判断条件，`elif` 可以处理多分支
- for 适合固定次数或遍历序列
- while 适合条件不确定时循环，注意避免死循环
- `break` 结束循环，`continue` 跳过本轮
- range 可以很方便地生成循环范围，步长可以是负数
- 多练习后，条件和循环会变得非常自然
