# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

# 导入os模块，模块的概念后面讲到
import os

print(list(range(1, 11)))  # 1..10

# 平方
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print([x*x for x in range(1, 11)])

# 还可以使用两层循环   [ad,ae,af,bd...]
print([m+n for m in 'abc' for n in 'def'])

# os.listdir可以列出文件和目录
print([d for d in os.listdir('.')])

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'a': 'a', 'b': 'b', 'c': 'c'}
for k, v in d.items():
    print(k, v)

 # 转小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
