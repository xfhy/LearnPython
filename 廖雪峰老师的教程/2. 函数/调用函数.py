print(abs(-10.3))

print(max(1,0,13,32,-45,0))  # 取最大值
print(min(1,0,13,32,-45,0))  # 取最小值

# 数据类型转换
 
# print(int("dasd"))  # ValueError: invalid literal for int() with base 10: 'dasd'
print(int(1)) # 转int
print(str("12dasdas"))    # 转str
print(float('2.3'))   # 转float
print(bool(1))   #转bool
print(bool(0))    
print(bool(-1))  
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(456546))

print(str(hex(255)))
print(hex(255))
print(str(hex(1000)))
print(type(str(hex(255))))