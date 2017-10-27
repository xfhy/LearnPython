a = [12, 312, 312, 312, 41, 234523]
print(a)

# 追加在最后
a.append(1)
print(a)

# 插入到指定位置
a.insert(0, "插入到指定位置")
a.insert(133, "卧槽,我看看会不会报错")  # 当插入的位置超出的时候,则会插入到列表末尾
a.insert(-3456, "-3")
print(a)

# 清空列表
a.clear()
print(a)

a = [12, 312, 312, 312, 41, 234523, 12]
# 计算12在列表中出现的次数
print("出现次数{:d}".format(a.count(12)))

# 移除元素  只会移除第一个12
a.remove(12)
print(a)

# 反转
a.reverse()
print(a)

# b列表中所有元素添加到a列表
b = [3, 3, 3, 33]
a.extend(b)
print(a)

# 列表排序,排序的前提是列表的元素是可比较的。
# a.append("dadasd")  # TypeError: '<' not supported between instances of 'str' and 'int'    不能比较则报错
a.sort()
print(a)

# 删除指定位置上的列表元素   我擦,居然有这种关键字
del a[0]
print(a)


