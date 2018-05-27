# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问


class Student(object):

    def __init__(self, name, score):
        self._name = name
        self.__score = score

    # 这个self参数必须有,调用时不用传
    def print_score(self):
        print("%s: %s" % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bad score')
        self.__score = score

std = Student('xfhy', 100)
# print(std.__name) error  无法访问

'''
py中方法名是_分隔单词,也有getter和setter嘛 哈哈
'''

std.set_name('xfhy2')
std.set_score(99)
print(std.get_name(),std.get_score())


# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
print(std._Student__name)  # 居然可以通过这种方式访问私有属性 666


'''
最后注意下面的这种错误写法：

>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'
表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：

>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
'''

class Student2(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender!='male' and gender!='female':
            raise ValueError('性别错误')
        self.__gender = gender

bart = Student2('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')