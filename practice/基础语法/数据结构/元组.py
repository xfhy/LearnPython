a = 1, 2.3, 4.1, "sadas"
print(a)

print(a[1])
for x in a:
    print(x)

x, y = divmod(15, 2)  # 商,余数
print(x, y)
# 元组是不可变类型，这意味着你不能在元组内删除或添加或编辑任何值。
# a[1] = 1 # TypeError: 'tuple' object does not support item assignment

# 要创建只含有一个元素的元组，在值后面跟一个逗号。
b = (12,)
print(type(b)) # <class 'tuple'>
