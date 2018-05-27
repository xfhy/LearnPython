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


