# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。


def f(x):
    return x*x


r = map(f, [1, 2, 3, 4])

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(r))

# 转字符串
print(list(map(str, [1, 2, 3, 4])))


'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''

# 比方说对一个序列求和，就可以用reduce实现：

from functools import reduce


def add(x, y):
    return x+y


# 求和
print(reduce(add, [1, 3, 5, 7]))
print(sum([1, 3, 5, 7]))


def fn(x, y):
    return x*10+y


print(reduce(fn, [1, 3, 5, 7, 9]))  # 13579

# 这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：

# 字符转数字


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


#先用map将'13579'字符转为[1,3,5,7,9]数字,再用reduce配合fn函数组合成数字13579
print(reduce(fn, map(char2num, '13579')))

# 整理成一个str2int的函数就是：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))

# 还可以用lambda函数进一步简化成：
def str2intX(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

# 练习

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
def normalize(name):
    return str.capitalize(name) #首字母大写,其余字母小写

m = map(normalize,['adam', 'LISA', 'barT'])
for name in m:
    print(name)

# 练习2 Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def listMul(x,y):
    return x*y
def prod(L):
    return reduce(listMul,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 练习3  利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def str2float(s):
    x = s.index('.')
    n = len(s)-x-1
    s = list(s)
    del s[x]
    ans = reduce(lambda x,y:x*10+y,map(char2num,s))
    return ans*(0.1**n)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')