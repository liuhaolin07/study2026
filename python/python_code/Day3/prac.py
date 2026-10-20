# %%   列表操作

# nums=[5,3,4,2,9,1,3,7,8,6]
# print(nums)
# nums.sort()
# print(nums)
# nums.reverse()
# print(nums)
# nums.append(10) #append() 方法用于在列表末尾添加新的对象。
# print(nums)
# nums.insert(0,0) #insert() 方法用于在列表中的指定位置插入一个新的对象。
# print(nums)
# nums.pop() #pop() 方法用于删除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# nums.pop(0) #pop(0) 表示删除并返回索引为 0 的元素
# print(nums)
# c = nums.count(3)
# print(c)

# nums2=[5,3,4,2,9,1,3,7,8,6]
# print(nums2)
#
# #extend() 方法用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
# nums2.extend([10,11,12])
# print(nums2)
# nums2.insert(0,3)
#
# print(nums2)
#
# print(nums2.index(3)) #index() 方法用于从列表中找出某个值第一个匹配项的索引位置。
#
# print(nums2.count(3)) #count() 方法用于计算某个元素在列表中出现的次数。
#
# print(nums2[::3]) #切片操作，步长为3
#
# print(23 in nums2)
#
# nums3=[x for x in range(3,100) if x%3==0]
# print(nums3)

# tuple 元组：有序、不可修改
# point = (3, 5)
# print(point[0])
# print(point[1])

# nums = [1, 2, 3]
# nums.append(4)  #末尾追加元素4
# nums.insert(1, 10)   # 在下标 1 位置插入 10
# nums.remove(2)   # 删除第一个匹配的 2
# print(nums)

# nums = [10, 20, 30, 40, 50]
# print(nums[0])      # 10
# print(nums[-2])     # 40，倒数第二个
# print(nums[1:4])    # [20, 30, 40]，不包含下标4的数
# print(nums[:3])     # [10, 20, 30]，表示前3个数
# print(nums[::2])    # [10, 30, 50]，隔一个取一个

# for ch in "Python":
#     print(ch)

#猜数字
# import random
# number = random.randint(1,100)
# count=0
# while True:
#     guess=int(input("请输入1到100的整数："))
#     count+=1
#     if guess>number:
#         print("猜大了")
#     elif guess<number:
#         print("猜小了")
#     else:
#         print(f"恭喜你猜对了,你猜了{count}次")
#         break

# %%   字典操作

# dict1 = {"name": "Alice", "age": 25}
# print(dict1["name"])
# print(dict1.get("age"))
# dict1["age"] = 26
# print(dict1)

#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}\t",end="")
#     print()

# squ=[x*x for x in range(1,10)]
# print(squ)
# squ=[x*x for x in range(1,10) if x%2==0]
# print(squ)

# a = (3)       # 这是整数 3，不是元组
# b = (3,)      # 加逗号才是元组
# print(type(a), type(b))

# student = {"name": "张三", "score": 90}
# print(student["name"])      # 张三
# print(student["score"])     # 90
#
# ### 新增与修改
# student = {"name": "张三"}
# student["score"] = 90       # 新增
# student["name"] = "李四"    # 修改
# print(student)
#
# ### 遍历字典
# for key in student:
#     print(key, student[key])          # 遍历键，再取值
#
# for name in student.keys():           # 所有键
#     print(name)
# # pass 表示空操作，占位符
# for score in student.values():        # 所有值
#     print(score)
#
#
# for name, score in student.items():   # 键值对
#     print(name, score)

# # 使用大括号 {} 来创建空字典
# emptyDict = {}
#
# # 打印字典
# print(emptyDict)
#
# # 查看字典的数量
# print("Length:", len(emptyDict))
#
# # 查看类型
# print(type(emptyDict))

# tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# # str(tinydict) #str表示将字典转换为字符串
# print(tinydict)
# print(tinydict['Name'])
# print(tinydict['Age'])
# print(tinydict['Class'])

# scores=[] #list类型
# students={} #dict类型
# while True:
#     try:
#         line=input("请输入名字和成绩（用空格隔开）：")
#     except EOFError:
#         break  #这两行的作用是当输入EOFError时，退出循环
#
#     if not line:
#         break  #当输入为空时，退出循环
#
#     name,score_text=line.split() #split() 方法用于将字符串按照空格分割成两个字符串
#     score=int(score_text)
#     students[name]=score
#     scores.append(score) #给scores列表添加元素
#     print(students) #打印学生信息
#     print(scores) #打印学生成绩
#
# if scores:
#     average_score=sum(scores)/len(scores)
#     print(f"平均分是{average_score}")
#     print(f"最高分是{max(scores)}")
#     print(f"最低分是{min(scores)}")
# else:
#     print("没有输入学生成绩")


#练习二 字符统计
text=input("请输入一串字符:")
counts={} #dict用于计数

for ch in text:
    counts[ch]=counts.get(ch,0)+1
    #get() 方法用于获取指定键的值，如果键不存在于字典中，返回默认值0
    #给counts排序
for ch,count in counts.items(): #items方法返回(key,value)
    print(f"{ch}:{count}")

