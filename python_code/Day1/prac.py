name="haolin"
age=20
score=99.99

if (age<score):
    print(name)

print(type(name))
print(age)
## int("abc")会报错

print(f"{name} is {age} years old")
##加f告知：{}会被求值后替换

print(b"{name} is {age} years old")
## b是转码来着，不太懂
print(1,2,3)
print("a=",20)

# name=input("输入你的名字：")

# age=int(input("请输入年龄："))
## int与c里的（int）类似，直接截取整数部分

print("a", "b", "c")            # 多个值默认用空格隔开
print("a", "b", sep="-")        # sep 指定分隔符
print("等待", end="...")        # end 指定结尾（默认换行）

print(20//3)
print(3**2)


print(age > 18 and age < 30)    # True
print(age < 18 or age > 60)     # False
print(not age > 18)             # False

"""
多
行
注
释
"""

#练习一
c=float(input("输入摄氏度："))
f=c*9/5+32
print(f"华氏度：{f}")

#练习二

num1=float(input("number1:"))
op=input("运算符：")
num2=float(input("number2:"))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("error")

#练习三
a=int(input("a="))  #一定要套壳子，input返回字符串
b=int(input("b="))

a,b=b,a

print("交换后 a =", a)
print("交换后 b =", b)

a,b=b,a

print("交换后 a =", a)
print("交换后 b =", b)