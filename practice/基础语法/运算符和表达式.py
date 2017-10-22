# 只要有任意一个操作数是浮点数，结果就会是浮点数。
a = 1 + 2
b = 1.0 + a
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>

# 进行除法运算时若是除不尽，结果将会是小数  这很自然?自然个毛啊,C语言可不是这样的
c = 14 / 3
print(c)  # 4.666666666666667

# 整除
d = 14 // 3
print(d)  # 4

# 取余 %


# 小栗子
days = 265
'''
# divmod(num1, num2) 返回一个元组，这个元组包含两个值，第一个是 num1 和 num2 相整除得到的值，第二个是 num1 和 num2 求余得到的值，然后我们用 * 运算符拆封这个元组，得到这两个值。
'''
print("{}月 {}日".format(*divmod(days, 30)))
print(divmod(days, 30))  # (8, 25)

# 对于逻辑 与，或，非，我们使用 and，or，not 这几个关键字。

# 类型转换
'''
类型转换函数	转换路径
float(string)	字符串 -> 浮点值
int(string)	    字符串 -> 整数值
str(integer)	整数值 -> 字符串
str(float)	    浮点值 -> 字符串
'''

# 小栗子

# 这个程序计算数列 1/x+1/(x+1)+1/(x+2)+ ... +1/n，我们设 x = 1，n = 10。

sum1 = 0
for x in range(1,10):
    sum1 += 1/x
print(x)  # 这里出了for循环也还可以访问x
print(sum1)

# 另外 Python 是强类型语言，所以必要的时候需要手动进行类型转换。