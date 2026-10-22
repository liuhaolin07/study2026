# def Greet():
#     print("Hello,Python!")

# Greet()

# def power(x,n=2):
#     return x**n

# print(power(x))
# 注意：默认参数要写在普通参数的后面，否则会报错。

# def introduce(name, city, age):
#     print(f"{name}，来自{city}，{age+1}岁")

# introduce(city="上海", name="张三",age=20)   # 不按顺序也没问题

#可变参数
# def total(*args):
#     print(args)          # (1, 2, 3)
#     return sum(args)

# def show(**kwargs):
#     print(kwargs)        # {"name": "张三", "score": 90}

# print(total(1, 2, 3))
# show(name="张三", score=90)

#返回多个值，打包成元组
# def get_min_max(nums):
#     return min(nums), max(nums)
# # 等价于return (min(nums), max(nums))
# low, high = get_min_max([3, 1, 9, 5])
# #上一行可视为元组解包
# print(low, high)     # 1 9

#要在函数内修改全局变量，需要 `global` 声明
#和cpp中的
# total = 10

# def change():
#     global total
#     total = 100

# change()
# print(total)        # 100

# lambda表达式：匿名函数，只有一行，返回值就是表达式的结果
# 格式：lambda 参数: 表达式
# square = lambda x: x ** 2
# print(square(5))    # 25
# #使用场景
# # 按元组第二个元素排序
# students = [("张三", 90), ("李四", 85), ("王五", 95)]
# students.sort(key=lambda s: s[1])
# print(students)     # [('李四', 85), ('张三', 90), ('王五', 95)]

# # map：每个元素都平方
# nums = [1, 2, 3, 4]
# print(list(map(lambda x: x * x, nums)))    # [1, 4, 9, 16]
# #map方法：对可迭代对象中的每个元素应用函数
# # filter：只留下偶数
# #filter方法：对可迭代对象中的每个元素应用函数，返回值为True的元素
# print(list(filter(lambda x: x % 2 == 0, nums)))   # [2, 4]
# #list() 作用是把 map / filter 返回的迭代器对象转换成真正的列表

# #练习一：排序函数
# def sort_numbers(numbers,reverse=False):
#     return sorted(numbers,reverse=reverse)

# nums=[5, 2, 9, 1, 5, 6]
# print(sort_numbers(nums))          # [1, 2, 5, 5, 6, 9]
# print(sort_numbers(nums,reverse=True))   # [9, 6, 5, 5, 2, 1]
# # sorted(列表)：返回新列表，原列表不变
# # list.sort()：直接修改原列表

#数据统计
# def data_statistics(numbers):
#     # 处理空列表的情况
#     if not numbers:
#         return None

#     total = sum(numbers)
#     count = len(numbers)
#     average = total / count

#     return {
#         "count": count,
#         "sum": total,
#         "average": average,
#         "max": max(numbers),
#         "min": min(numbers),
#     }
# # 把所有结果打包成一个字典返回，调用方可以通过键名方便地取值。

# nums = [12, 18, 9, 25, 30]
# result = data_statistics(nums)

# #若列表为空，返回 None，调用方可以通过判断返回值是否为 None 来处理空列表的情况。
# if result:
#     print("数据个数：", result["count"])
#     print("总和：", result["sum"])
#     print("平均值：", result["average"])
#     print("最大值：", result["max"])
#     print("最小值：", result["min"])
# else:
#     print("列表为空")

def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))   # 55