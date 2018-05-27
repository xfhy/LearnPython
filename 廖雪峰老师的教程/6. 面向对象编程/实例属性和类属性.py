# py是动态语言   根据类创建的实例可以任意绑定属性。

# 给实例绑定属性的方法是通过实例变量，或者通过self变量


class Student(object):

    age = 12  # 类属性  这个属性归类所有  有点类似于java的static变量,可以直接用类名访问的,不用创建对象   这是所有对象公用的
    count = 0

    def __init__(self, name):
        # 练习:增加一个实例 则count+1
        Student.count = Student.count + 1
        self.name = name

'''
s = Student('xfhy')
s.score = 45  # 新增一个属性  而且还赋值了
print(s.score)

print('age=', Student.age)

del s.name  # 还可以删除属性
print(hasattr(s, 'name'))  # False

# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

print(Student.count)
'''

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


'''
小结
实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''