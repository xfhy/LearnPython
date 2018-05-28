
class Student(object):
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def set_score(self, score):
        if not isinstance(score, int):
            raise TypeError('类型错误')
        if 0 <= score <= 100:
            self.score = score
        else:
            raise ValueError('超出范围')


s = Student(100)
# s.set_score('da')
# s.set_score(-9)

# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值


class Student2(object):
    # getter
    @property
    def score(self):
        return self._score

    # setter
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise TypeError('类型错误')
        if value < 0 or value > 100:
            raise ValueError('超出范围')
        self._score = value

    # 只有getter 那么就是只读
    @property
    def birth(self):
        return self._birth


s2 = Student2()
s2.score = 99
print(s2.score)

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。


# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('类型错误')
        if value < 0:
            raise ValueError('参数错误')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('参数错误')
        if value < 0:
            raise ValueError('参数错误')
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
