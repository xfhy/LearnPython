# 字典是是无序的键值对（key:value）集合，同一个字典内的键必须是互不相同的。一对大括号 {} 创建一个空字典。初始化字典时，在大括号内放置一组逗号分隔的键：值对，这也是字典输出的方式。我们使用键来检索存储在字典中的数据。

data = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd'}
print(data)

# 添加键值对到字典中
data['e'] = 'e'
print(data)

# 使用 del 关键字删除任意指定的键值对：
del data['a']

# 使用 in 关键字查询指定的键是否存在于字典中。
print('a' in data)

# 必须知道的是，字典中的键必须是不可变类型，比如你不能使用列表作为键。
# dict() 可以从包含键值对的元组中创建字典。
print(dict((('Indian', 'Delhi'), ('Bangladesh', 'Dhaka'))))

# 如果你想要遍历一个字典，使用字典的 items() 方法。
print(data.items())
for x in data.items():
    print(x, end=' ')
for x, y in data.items():
    print("{} uses {}".format(x, y))

# 许多时候我们需要往字典中的元素添加数据，我们首先要判断这个元素是否存在，不存在则创建一个默认值。如果在循环里执行这个操作，每次迭代都需要判断一次，降低程序性能。
# 我们可以使用 dict.setdefault(key, default) 更有效率的完成这个事情。
data2 = {}
data2.setdefault('name', []).append('Python')
print(data2)

# 试图索引一个不存在的键将会抛出一个 keyError 错误。我们可以使用 dict.get(key, default) 来索引键，如果键不存在，那么返回指定的 default 值。
print(data2.get('a', 'default'))

# 如果你想要在遍历列表（或任何序列类型）的同时获得元素索引值，你可以使用 enumerate()。
for i, j in enumerate(['a', 'b', 'c']):
    print(i, j)

# 你也许需要同时遍历两个序列类型，你可以使用 zip() 函数。
a = ['a', 'aa']
b = ['b', 'bb']
for x, y in zip(a, b):
    print("{} .. {}".format(x,y))

