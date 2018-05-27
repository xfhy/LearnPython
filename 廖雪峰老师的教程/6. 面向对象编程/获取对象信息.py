# 获取对象的类型
print(type(123))
print(type(abs))

print(type(123) == type(456))  # True   可以比较两个边路的type类型是否相同

import types


def fn():
    pass


# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。我们回顾上次的例子，如果继承关系是：
# object -> Animal -> Dog -> Husky

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：

print(isinstance([], (list, tuple)))
print(isinstance((), (list, tuple)))

#  总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

'''
使用dir()
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
'''
print(dir('ABC'))

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x*self.x

obj = MyObject()
# 有'x'属性吗
print(hasattr(obj,'x'))

setattr(obj,'y',19) # 设置一个属性y
print(obj.y)
print(hasattr(obj,'y')) # true
print(getattr(obj,'y')) # 获取属性'y'

# getattr(obj, 'z') # 获取属性'z' 如果试图获取不存在的属性，会抛出AttributeError的错误：

getattr(obj,'z',404) # 可以传入一个default参数，如果属性不存在，就返回默认值：

# 也可以获取对象的方法 是否存在
print(hasattr(obj,'power'))

# 获取方法'power'并赋值到变量fn  
fn = getattr(obj,'power')
print(fn())

# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。

'''
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
'''