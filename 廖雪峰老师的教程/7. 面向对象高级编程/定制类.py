
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。


class Student(object):
    def __init__(self, name, count):
        self.name = name
        self.count = count

    # 有点类似于java的toString()方法
    def __str__(self):
        return "Student name is {} ,count is {}".format(self.name, self.count)

    # 假设该类的"长度"为2
    def __len__(self):
        return 2

    def __iter__(self):
        return self

    def __next__(self):
        self.count = self.count+1  # 计算下一个值
        if self.count > 1000:  # 退出循环的条件
            raise StopIteration()
        return self.count  # 返回下一个值
    
    # 取第n个元素
    def __getitem__(self,n):
        if isinstance(n,int): #n是索引
            return n
        if isinstance(n,slice): #n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            count=1
            L = []
            for x in range(stop):
                if x>=start:
                    L.append(count)
                count = count+1
            return L
    
    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
    def __getattr__(self,attr):
        if attr=='age':
            return 18 # 返回数值  属性
        if attr=='score':
            return lambda:25 # 返回函数:不管传什么参数都返回25


print(Student('xfhy', 1))

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

for n in Student('name', 1):
    print(n)

s = Student('xfhy',1)
print(s[5])
print(s[1:5])
print(s.score()) # 25  当前是无score属性的