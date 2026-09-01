# Python基础语法

## 1. Python安装

### 安装方式
- 去 Python 官网下载安装包
- 安装时勾选 Add Python to PATH
- 安装完成后在命令行检查版本：

```bash
python --version
```

### 常见工具
- VS Code：轻量，适合写代码和调试
- PyCharm：功能完整，适合系统学习和项目开发

### VS Code 使用建议
- 安装 Python 插件
- 选择正确的解释器
- 使用终端运行 `.py` 文件

## 2. 变量

### 特点
- 变量用于保存数据
- Python 不需要提前声明类型
- 变量名要有意义，建议用小写字母和下划线

### 示例

```python
name = "Alice"
age = 18
score = 95.5
```

### 命名规则
- 只能包含字母、数字、下划线
- 不能以数字开头
- 不能使用关键字
- 尽量避免中文和特殊符号

## 3. 数据类型

### 常见类型
- `int`：整数
- `float`：小数
- `str`：字符串
- `bool`：布尔值

### 示例

```python
x = 10
pi = 3.14
msg = "hello"
flag = True
```

### 类型查看

```python
print(type(x))
print(type(pi))
print(type(msg))
print(type(flag))
```

### 类型转换

```python
a = int("42")      # 字符串 → 整数
b = float("3.5")   # 字符串 → 小数
c = str(100)       # 整数 → 字符串
d = int(3.9)       # 小数 → 整数（直接截断，不是四舍五入）
print(a, b, c, d)
```

注意：
- `int("abc")` 会报错，不是所有字符串都能转成数字
- 计算前通常先把 `input()` 的结果转成数字

## 4. 字符串格式化

### f-string（推荐）
## version3.6+
在字符串前加 `f`，用 `{}` 直接嵌入变量：

```python
name = "张三"
score = 95
print(f"{name}考了{score}分")
print(f"保留两位小数：{3.14159:.2f}")
```

### 其他旧写法

```python
name = "李四"
print("姓名：%s" % name)          # % 占位
print("姓名：{}".format(name))    # format()
```

## 5. 输入输出

### 输出

```python
print("Hello, Python")
print("a =", 10)
```

### 输入

```python
name = input("请输入你的名字：")
print("你好，", name)
```

### 输入转换

`input()` 返回的一定是字符串，做计算前要先转成数字：

```python
age = int(input("请输入年龄："))
height = float(input("请输入身高："))
print("明年", age + 1, "岁")
```

### print 的参数

```python
print("a", "b", "c")            # 多个值默认用空格隔开
print("a", "b", sep="-")        # sep 指定分隔符
print("等待", end="...")        # end 指定结尾（默认换行）
```

## 6. 运算符

### 算术运算符
- `+` 加
- `-` 减
- `*` 乘
- `/` 除（结果是小数）
- `//` 整除（向下取整）
- `%` 取余
- `**` 幂运算

### 示例

```python
print(7 + 3)
print(7 / 2)     # 3.5
print(7 // 2)    # 3
print(7 % 2)     # 1
print(2 ** 3)    # 8
```

### 赋值运算符

```python
x = 10
x += 5    # 相当于 x = x + 5
x -= 3    # 相当于 x = x - 3
x *= 2    # 相当于 x = x * 2
x /= 4    # 相当于 x = x / 4
x //= 2   # 相当于 x = x // 2
x %= 3    # 相当于 x = x % 3
print(x)
```

### 字符串运算

```python
a = "abc" + "def"    # 拼接 → "abcdef"
b = "ha" * 3         # 重复 → "hahaha"
print(a, b)
```

### 比较运算符
- `==` 等于
- `!=` 不等于
- `>` 大于
- `<` 小于
- `>=` 大于等于
- `<=` 小于等于

### 逻辑运算符
- `and` 并且
- `or` 或者
- `not` 取反

```python
age = 20
print(age > 18 and age < 30)    # True
print(age < 18 or age > 60)     # False
print(not age > 18)             # False
```

### 运算符优先级

从高到低大致为：

```text
**      幂运算
+ -     正负号
* / // %   乘除取余
+ -     加减
< > <= >=   比较
== !=   相等
not     取反
and     并且
or      或者
```

记不住时，用括号让意图更清晰：

```python
result = (2 + 3) * 4    # 20
```

## 7. 注释

注释不参与运行，用来解释代码，给人和自己看。

```python
# 单行注释：井号开头
name = "张三"

"""
多行注释：
用三个引号包起来，
可以写多行说明。
"""
```

## 8. 练习题

### 练习 1：温度转换程序

题目：输入摄氏度，输出华氏度。

公式：

```text
F = C * 9 / 5 + 32
```

参考代码：

```python
celsius = float(input("请输入摄氏度："))
fahrenheit = celsius * 9 / 5 + 32
print("华氏度：", fahrenheit)
```

### 练习 2：简单计算器

题目：输入两个数和一个运算符，完成加减乘除。

参考代码：

```python
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
```

### 练习 3：交换两个变量

题目：输入两个数，交换它们的值并输出。

参考代码：

```python
a = int(input("请输入 a："))
b = int(input("请输入 b："))

a, b = b, a   # Python 一行交换

print("交换后 a =", a)
print("交换后 b =", b)
```

## 9. 学习小结

- 先掌握安装环境和运行方式
- 熟悉变量、类型、输入输出和运算符
- `input()` 返回的是字符串，计算前记得用 `int()` / `float()` 转换
- 字符串拼接建议优先用 f-string
- 多写练习题，重点练输入转换和条件判断
- 建议把每个知识点都自己手写一遍
