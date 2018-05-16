# 切片  可以取出某几个元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 下面2个是一样的意思
print(L[:3])
print(L[0:3])

# 倒数第一个元素是-1
print(L[-2:])
print(L[-2:-1])


L = list(range(100))  # 生成一个列表 0-99
print(L)
print(L[:10:2])  # 前10个数  每2个取一个
print(L[::5])  # 所有数   每5个取一个

print(L[:])  # 复制一个list


# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple

t = tuple(range(1000))
print(t[::100])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
s = 'abcdefghijk'
print(s[:5])  # 前5个
print(s[::2])

# 练习 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：


def trim(s):
    if not isinstance(s, (str)):
        raise TypeError('类型错误')
    length = len(s)
    if length == 0:
        return ''
    x, y = 0, 0  # 前后下标

    for a in s:
        if(a != ' '):
            break
        x = x+1

    y = length-1
    for a in s[::-1]:   # 逆序循环
        if(a != ' '):
            break
        y = y-1

    # 可能字符串全是空格
    if x == y:
        return ''
    return s[x:y+1]


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
