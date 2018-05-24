from collections import Iterable
# Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上

L = [1, 2, 3]

for a in L:
    print(a)

# dict
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
a = {'1': 1, 'b': 'b', 4: '3'}

for key in a:
    print(key)

for c in 'abc':
    print(c)

# 判断是否可迭代
if isinstance('abs', Iterable):
    print('true')

# 整数不可以迭代

# 带下标的遍历
for i, value in enumerate('abcd'):
    print(i, "=", value)

for x, y in [(1, 1), (2, 3), (3, 9)]:
    print(x, y)

# 练习 请使用迭代查找一个list中最小和最大值，并返回一个tuple：


def findMinAndMax(L):
    if not isinstance(L, (list)):
        return TypeError('类型错误')
    length = len(L)
    if length == 0:
        return (None, None)
    if length == 1:
        return (L[0], L[0])
        
    min, max = L[0], L[0]
    for value in L:
        if(value < min):
            min = value
        if(value > max):
            max = value
    return (min, max)


if findMinAndMax([]) != (None, None):
    print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('3测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4测试失败!')
else:
    print('测试成功!')
