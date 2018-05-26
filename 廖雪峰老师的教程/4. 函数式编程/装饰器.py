import functools

def log(func):
    def wrapper(*args, **kw):
        # 1. 在调用函数之前打印方法名
        # __name__ 是函数名
        print('call %s():' % func.__name__)
        return func(*args, **kw)
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

print(f.__name__)  # __name__  属性   可以拿到函数的名字
print(now.__name__)
now()


# 把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)

'''
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
'''


def log2(text):
    def decorator(func):
        #返回值最终是wrapper函数,构建一个新函数执行  
        @functools.wraps(func) # 需要把原始函数的__name__等属性复制到wrapper()函数中
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('execute')
def now2():
    print('2018年5月26日23:26:51')

now2()
print(now2.__name__)

## import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可



'''
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
'''
