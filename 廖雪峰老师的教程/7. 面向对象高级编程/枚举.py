from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

Month.Jan

# 枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, "=>", member, ",", member.value)

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：


@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sum的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 访问这些枚举类型可以有若干种方法：
day1 = Weekday.Mon
print(day1)  # Weekday.Mon
print(Weekday['Tue'])
print(Weekday.Tue.value) #2
print(day1==Weekday.Mon)
# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

