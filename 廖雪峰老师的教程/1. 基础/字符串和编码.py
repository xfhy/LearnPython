# ASCII编码是1个字节，而Unicode编码通常是2个字节
# 本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

a = 'aaa'  # 字符串 str     Unicode编码
a = b'aaa'  # bytes  每个字符都只占用一个字节


# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
b'asv'.decode('utf-8')
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')) #中

# 字符串长度
a = 'abc'
print(len(a))

# 格式化   占位符  和C语言一样,
# %d %f %s %x(16进制)
# %s可以把任何数据转换为字符串
print('Hi, %s, you have $%d. 我可以借$%.2f吗?' %
      ('小明', 100, 1.3))  # Hi, 小明, you have $100. 我可以借$1.30吗?

print('%2d   %02d' % (2, 3))  # 2  03

# format格式化    保留小数时是四舍五入
print('Hello ,{0} 成绩提升了{1:.1f}'.format('小明',15.56))    #Hello ,小明 成绩提升了15.6

print('%.20f' % 3.1415926)  

'''
Python 3的字符串使用Unicode，直接支持多语言。

当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。Python当然也支持其他编码方式，比如把Unicode编码成GB2312：

>>> '中文'.encode('gb2312')
b'\xd6\xd0\xce\xc4'
但这种方式纯属自找麻烦，如果没有特殊业务要求，请牢记仅使用UTF-8编码。

格式化字符串的时候，可以用Python的交互式环境测试，方便快捷。
'''