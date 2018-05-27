# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
class Student(object):
    pass

bart = Student()
print(bart) #输出实例内存地址

# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
bart.name = 'xfhy'
print(bart.name)

class Student2(object):

    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
    # 有点像java的构造方法,self类似于java的this
    # 注意：特殊方法“__init__”前后分别有两个下划线！！！
    # 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
    # 这个self参数必须有,调用时不用传
    def print_score(self):
        print("%s: %s" % (self.name,self.score))
    
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'

# 现在必须传参数了
st2 = Student2('xfhy',100)
print(st2.name,st2.score)
st2.print_score()
print(st2.get_grade())

'''
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
'''