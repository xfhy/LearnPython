# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性

class Student(object):
    pass

s = Student()

# 绑定属性
s.name = 'xfhy'
print(s.name)


# 绑定方法
def set_name(self,name):
    self.name = name

from types import MethodType
s.set_name = MethodType(set_name,s) #给实例绑定一个方法
s.set_name('xfhy666')
print(s.name)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：

s2 = Student()
print(hasattr(s2,'set_name')) #False

# 为了给所有实例都绑定方法，可以给class绑定方法： 
# 给class绑定方法后，所有实例均可调用：
def set_score(self,score):
    self.score= score

Student.set_score = set_score

s2.set_score(4)
print(s2.score)

# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

class Student2(object):
    __slots__ = ('name','age') # 用tuple定义允许绑定的属性名称

s = Student2()
s.name = 'xfhy' #绑定一个属性
print(s.name)
s.age = 18
# s.score = 80  这里无法进行绑定   AttributeError

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class GraduateStudent(Student2):
    pass

g = GraduateStudent()
g.score = 100
print(g.score)

# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。