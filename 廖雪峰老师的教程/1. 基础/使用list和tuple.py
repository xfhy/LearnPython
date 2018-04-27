# list   可以是不同类型   还可以是另一个list
classmates = ['1', '小明', '小伞', 3.25, 45, [1, 2]]
print(classmates)

# list 注意越界异常IndexError: list index out of range
classmates.append('ss')  # 增  最后
classmates.insert(1, '小何')
print(classmates)

classmates.remove('ss')  # 删
# classmates.remove(1)  # 移除元素  当不存在需要移除的元素时 报错:ValueError: list.remove(x): x not in list
classmates.pop()   # 删 最后一个
classmates.pop(1)  # 删指定位置
print(classmates)

print('cc')
print(classmates[0])  # 查
classmates[0] = ''  # 改
print(classmates)

print(classmates[-1])  # 最后一个元素
print(classmates[-2])  # 倒数第二个元素

print(len(classmates))  # 长度
print(classmates)

# list包含list
p = [1, 2, 3]
s = [4, 5, p, 5]
print(s[2][1])


# tuple
classmates = (1,2)