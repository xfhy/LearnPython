
def log(func):
    def wrapper(*args,**kw):
        # 1. 在调用函数之前打印方法名
        print('call %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper

# 2. 在方法前面加上
@log
def now():
    print('2015-3-26')

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
'''
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper
'''

f = now

print(f.__name__)  #__name__  属性   可以拿到函数的名字  
print(now.__name__)
now()


# 把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)

'''
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
'''