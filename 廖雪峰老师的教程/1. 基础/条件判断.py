# 一般形式
age = 5

if age > 10:
    print("age=", age)
elif age > 6:
    print("age=", age)
else:
    pass

# 简写
# 只要x是非零数值、非空字符串、非空list等，就判断为True
a = -5
if a:
    print("a=", a)

# input
# input输入的东西数据类型是str
str = input("输入数字")
birth = int(str)  # 这里如果不是数字时会报错
print(birth)