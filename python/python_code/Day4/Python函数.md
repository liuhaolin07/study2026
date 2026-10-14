# Python函数

## 1. 函数定义

函数就是把一段经常要用的代码封装起来，后面可以反复调用。

### 基本结构

```python
def greet():
    print("你好，Python")

greet()
```

### 作用

- 提高代码复用率
- 让程序更清晰
- 方便后期维护

## 2. 参数

参数可以让函数接收外部传入的数据。

### 位置参数

```python
def add(a, b):
    print(a + b)

add(3, 5)
```

### 默认参数

```python
def power(x, n=2):
    return x ** n

print(power(3))     # 9
print(power(3, 3))  # 27
```

注意：默认参数要写在普通参数的后面，否则会报错。

### 关键字参数

调用时用 `参数名=值`，可以不按顺序传：

```python
def introduce(name, city, age=18):
    print(f"{name}，来自{city}，{age}岁")

introduce(city="上海", name="张三")   # 不按顺序也没问题
```

### 可变参数

不确定会传几个参数时，用 `*args`（元组）和 `**kwargs`（字典）：

```python
def total(*args):
    print(args)          # (1, 2, 3)
    return sum(args)

def show(**kwargs):
    print(kwargs)        # {"name": "张三", "score": 90}

print(total(1, 2, 3))
show(name="张三", score=90)
```

### 常见理解

- 形参：函数定义时写在括号里的变量
- 实参：函数调用时传进去的具体值

## 3. 返回值

return 用来把函数执行结果返回给外部。

### 示例

```python
def max_value(a, b):
    if a > b:
        return a
    return b

result = max_value(8, 12)
print(result)
```

### 注意

- 写了 return 后，函数会立刻结束，后面的代码不再执行
- 没有 return 时，默认返回 None

### 返回多个值

返回多个值时，Python 会自动打包成元组：

```python
def get_min_max(nums):
    return min(nums), max(nums)

low, high = get_min_max([3, 1, 9, 5])
print(low, high)     # 1 9
```

## 4. 局部变量与全局变量

函数内部定义的变量是局部变量，函数外定义的变量是全局变量：

```python
total = 10          # 全局变量

def add_one():
    total = 100     # 这是新的局部变量，不影响全局
    return total

print(add_one())    # 100
print(total)        # 10，全局变量没变
```

要在函数内修改全局变量，需要 `global` 声明（一般较少用到）：

```python
total = 10

def change():
    global total
    total = 100

change()
print(total)        # 100
```

## 5. lambda

lambda 是一种匿名函数，适合写简单的函数。

### 结构

```python
lambda 参数: 表达式
```

### 示例

```python
square = lambda x: x * x
print(square(4))     # 16
```

等价于：

```python
def square(x):
    return x * x
```

### 常见场景

- 配合 `sorted()` 使用
- 配合 `map()`、`filter()` 使用

```python
# 按元组第二个元素排序
students = [("张三", 90), ("李四", 85), ("王五", 95)]
students.sort(key=lambda s: s[1])
print(students)     # [('李四', 85), ('张三', 90), ('王五', 95)]

# map：每个元素都平方
nums = [1, 2, 3, 4]
print(list(map(lambda x: x * x, nums)))    # [1, 4, 9, 16]

# filter：只留下偶数
print(list(filter(lambda x: x % 2 == 0, nums)))   # [2, 4]
```

## 6. 递归

函数调用自己，就是递归。必须要有终止条件，否则会无限调用直到报错。

```python
def factorial(n):
    if n == 1:          # 终止条件
        return 1
    return n * factorial(n - 1)

print(factorial(5))     # 5 * 4 * 3 * 2 * 1 = 120
```

### 注意

- 递归思路清晰，但太深容易栈溢出，日常优先用循环
- 每个递归都要问自己：终止条件是什么？

## 7. 练习一：排序函数

### 题目

写一个排序函数，输入一个列表，输出从小到大排序后的结果。

### 参考思路

- 先复制列表，避免修改原数据
- 使用 `sorted()` 完成排序
- 可以增加 `reverse` 参数支持降序

### 参考代码

```python
def sort_numbers(numbers, reverse=False):
    return sorted(numbers, reverse=reverse)


nums = [8, 3, 5, 1, 9, 2]
print("原列表：", nums)
print("升序：", sort_numbers(nums))
print("降序：", sort_numbers(nums, reverse=True))
```

## 8. 练习二：数据统计函数

### 题目

写一个数据统计函数，输入一个数字列表，输出以下内容：

- 数据个数
- 总和
- 平均值
- 最大值
- 最小值

### 参考思路

- 用 `len()` 求个数
- 用 `sum()` 求总和
- 用 `max()` 和 `min()` 求最大最小值
- 用字典返回结果更方便

### 参考代码

```python
def data_statistics(numbers):
    if not numbers:
        return None

    total = sum(numbers)
    count = len(numbers)
    average = total / count

    return {
        "count": count,
        "sum": total,
        "average": average,
        "max": max(numbers),
        "min": min(numbers),
    }


nums = [12, 18, 9, 25, 30]
result = data_statistics(nums)

if result:
    print("数据个数：", result["count"])
    print("总和：", result["sum"])
    print("平均值：", result["average"])
    print("最大值：", result["max"])
    print("最小值：", result["min"])
else:
    print("列表为空")
```

## 9. 练习三：斐波那契数列

### 题目

斐波那契数列：每一项等于前两项之和，`1, 1, 2, 3, 5, 8, 13 ...`。写一个函数返回第 n 项。

### 参考思路

- 第 1、2 项都是 1，作为终止条件
- 其余项 `fib(n) = fib(n-1) + fib(n-2)`

### 参考代码

```python
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(1, 11):
    print(fib(i), end=" ")     # 1 1 2 3 5 8 13 21 34 55
```

## 10. 学习小结

- 函数可以把重复代码封装起来
- 参数让函数更灵活，`*args` / `**kwargs` 可以接收任意数量参数
- return 用来返回计算结果，多个返回值自动打包成元组
- 函数内部的局部变量不会影响外部全局变量
- lambda 适合简单场景，常配合排序和过滤使用
- 递归要记得写终止条件
- 写函数时，先想清楚「输入是什么，输出是什么」
