# Python数据结构

## 1. list

### 特点
- 有序
- 可修改
- 可以存放多个数据

### 常用操作

```python
nums = [1, 2, 3]
nums.append(4)
nums.insert(1, 10)
nums.remove(2)
print(nums)
```

### 常见方法
- `append()`：末尾追加元素
- `insert()`：指定位置插入元素
- `remove()`：删除指定元素（第一个匹配项）
- `pop()`：弹出元素，不传下标默认弹出最后一个
- `sort()`：原地排序
- `extend()`：把另一个列表追加到末尾
- `count()`：统计元素出现次数
- `index()`：查找元素第一次出现的位置

### 下标与切片

下标从 0 开始，负数表示从尾部倒数：

```python
nums = [10, 20, 30, 40, 50]
print(nums[0])      # 10
print(nums[-1])     # 50，最后一个
print(nums[1:3])    # [20, 30]，不包含下标 3
print(nums[:2])     # [10, 20]
print(nums[::2])    # [10, 30, 50]，隔一个取一个
```

### 判断元素是否存在

```python
nums = [10, 20, 30]
print(20 in nums)     # True
print(99 in nums)     # False
```

### 列表推导式

用一行代码生成列表，比 for 循环更简洁：

```python
squares = [x * x for x in range(1, 6)]        # [1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

## 2. tuple

### 特点
- 有序
- 不可修改
- 适合保存不希望被修改的数据

### 示例

```python
point = (3, 5)
print(point[0])     # 3
```

### 注意：单元素元组

```python
a = (3)       # 这是整数 3，不是元组
b = (3,)      # 加逗号才是元组
print(type(a), type(b))
```

### 元组解包

```python
point = (3, 5)
x, y = point        # 一次性取出所有元素
print(x, y)         # 3 5

# 交换变量本质就是元组解包
a, b = b, a
```

## 3. dict

### 特点
- 以键值对方式存储数据
- 通过键快速查找值
- 键不能重复

### 示例

```python
student = {"name": "张三", "score": 90}
print(student["name"])      # 张三
print(student["score"])     # 90
```

### 新增与修改

键存在就修改，不存在就新增：

```python
student = {"name": "张三"}
student["score"] = 90       # 新增
student["name"] = "李四"    # 修改
print(student)
```

### 遍历字典

```python
for key in student:
    print(key, student[key])          # 遍历键，再取值

for name in student.keys():           # 所有键
    pass

for score in student.values():        # 所有值
    pass

for name, score in student.items():   # 键值对
    print(name, score)
```

### 常见方法
- `keys()`：获取所有键
- `values()`：获取所有值
- `items()`：获取键值对
- `get()`：安全获取值，键不存在返回 `None`（可以指定默认值）
- `update()`：批量更新
- `pop()`：删除指定键并返回它的值

```python
student = {"name": "张三", "score": 90}
print(student.get("age"))            # None，不会报错
print(student.get("age", 18))        # 18，指定默认值
student.update({"city": "北京", "score": 95})
student.pop("city")
print(student)
```

### 判断键是否存在

```python
print("name" in student)     # True
```

## 4. set

### 特点
- 无序
- 不重复
- 常用于去重

### 示例

```python
nums = {1, 2, 2, 3}
print(nums)     # {1, 2, 3}，重复的 2 自动去掉
```

### 集合运算

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)     # 并集：{1, 2, 3, 4, 5, 6}
print(a & b)     # 交集：{3, 4}
print(a - b)     # 差集：{1, 2}
```

### 去重用法

把 list 转成 set 再去重，再转回 list：

```python
nums = [1, 2, 2, 3, 3, 3]
unique = list(set(nums))
print(unique)     # [1, 2, 3]
```

### 常见用途
- 数据去重
- 判断元素是否存在（比 list 更快）
- 集合运算

## 5. 通用操作

这些操作对 list、tuple、字符串都适用：

```python
nums = [3, 1, 4, 1, 5]
print(len(nums))       # 长度：5
print(max(nums))       # 最大值：5
print(min(nums))       # 最小值：1
print(sum(nums))       # 求和：14
print(sorted(nums))    # 排序后返回新列表（不修改原列表）
```

## 6. 练习一：学生成绩统计

### 题目
输入学生姓名和成绩，例如：

```text
张三 90
李四 85
```

输出：
- 平均分
- 最高分

### 参考思路
- 用 list 保存成绩
- 用 dict 保存姓名和成绩
- 最后用 `sum()` 和 `max()` 统计

### 参考代码

```python
scores = []
students = {}

while True:
    try:
        line = input("请输入姓名和成绩（直接回车结束）：").strip()
    except EOFError:
        break

    if not line:
        break

    name, score_text = line.split()
    score = int(score_text)
    students[name] = score
    scores.append(score)

if scores:
    average_score = sum(scores) / len(scores)
    highest_score = max(scores)
    print("平均分：", average_score)
    print("最高分：", highest_score)
else:
    print("没有输入任何成绩")
```

## 7. 练习二：字符统计

### 题目

输入一段字符串，统计每个字符出现的次数。

### 参考思路

- 用 dict 保存「字符 → 次数」
- 遍历字符串，字符第一次出现记为 1，否则加 1
- 可以用 `get(字符, 0) + 1` 简化写法

### 参考代码

```python
text = input("请输入一段文字：")
counts = {}

for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

for ch, count in counts.items():
    print(f"{ch}: {count}")
```

## 8. 学习小结

- list 适合保存可变的有序数据
- tuple 适合保存固定不变的数据
- dict 适合用姓名、编号这类键来查找内容
- set 适合去重和集合运算
- 这四种数据结构在数据分析和程序设计里都非常常用
