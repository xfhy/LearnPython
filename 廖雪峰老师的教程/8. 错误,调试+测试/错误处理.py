import logging
'''
try:
    r = 10/int('a')
    print('result:',r) #上面有错,这句不会执行
except ValueError as e:
    print('ValueError:',e)
    logging.exception(e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error') # 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
finally: # finally模块和java一样,不管是否有错误发生,都会被执行
    print('finally...')
print('END')
'''
# 常见错误类型:https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# 所有错误类型都继承自BaseException
# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。

# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

# Python内置的logging模块可以非常容易地记录错误信息：


# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：

class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n==0:
        # raise FooError('invalid value: %s' % s)
        raise ValueError('invalid value: %s' % s)
    return 10/n

#foo('0')

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

'''
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
'''

# 练习
from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 76')
    print('99 + 88 + 76 =', r)

main()


'''
Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。

程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。
'''