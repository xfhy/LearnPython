# ASCII编码是1个字节，而Unicode编码通常是2个字节
# 本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

a = 'aaa' #字符串 str     Unicode编码
a = b'aaa' #bytes  每个字符都只占用一个字节


# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
b'asv'.decode('utf-8')
b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')

# 字符串长度
a = 'abc'
print(len(a))
