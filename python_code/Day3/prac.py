nums=[5,3,4,2,9,1,3,7,8,6]
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums.append(10) #append() 方法用于在列表末尾添加新的对象。
print(nums)
nums.insert(0,0) #insert() 方法用于在列表中的指定位置插入一个新的对象。
print(nums)
nums.pop() #pop() 方法用于删除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
nums.pop(0) #pop(0) 表示删除并返回索引为 0 的元素
print(nums)
c = nums.count(3)
print(c)
