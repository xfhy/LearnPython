'''
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数
'''
def power(x, n=2):   # 默认参数
    s = 1
    while n > 0:
        s = s * x
        n = n-1
    return s


print(power(2, 3))
print(power(2))

#  定义默认参数要牢记一点：默认参数必须指向不变对象！


def add_end(L=[]):
    L.append("END")
    return L


print(add_end())
print(add_end())
print(add_end())


def add_end2(L=None):
    if L is None:
        L = []
    L.append("END")
    return L


print(add_end2())
print(add_end2())
print(add_end2())

# 可变参数


def calc(*numbers):  # 在函数内部，参数numbers接收到的是一个tuple
    sum = 0
    for num in numbers:
        sum = sum+num*num
    return sum


print(calc(1, 2, 3))
a = [1, 2, 3]
print(calc(*a))

# 关键字参数  函数的调用者可以传入任意不受限制的关键字参数


def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name', name, 'age', age, 'other', kw)


person('michael', 30, city="beijing")
person('michael', 30, city="beijing", job='Engineer')
extra = {'city': 'beijing', 'job': 'Engineer'}
person('michael', 30, **extra)

# 命名关键字参数


def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('Jack', 24, city='Beijing', job='Engineer')


# 练习 可接收一个或多个数并计算乘积
def product(*x):
    if len(x)==0:
        raise TypeError('不能为空')
    sum = 1
    for num in x:
        sum = sum*num
    return sum


print(product(1, 2, 3, 2))
print(product(3))
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
