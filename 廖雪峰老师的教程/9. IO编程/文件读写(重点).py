
# 读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。

# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

try:
    f = open('D:/python/test.txt','r',encoding='UTF-8')
    print(f.read())
finally:
    if f:
        f.close()

# 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

with open('D:/python/test.txt','r',encoding='UTF-8') as f:
    # print(f.read(10)) # 一次读10个字节
    print(f.read())
# 调用read()会一次性读取文件的全部内容
# readline()一次读取一行内容
# readlines()一次读取所有内容并按行返回list


# 重点:如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

with open('D:/python/test.txt','r',encoding='UTF-8') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的`\n`删掉

# 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

with open('D:/python/a.xlsx','rb') as f:
    print(f.read())

# 字符编码
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
with open('D:/python/test.txt','r',encoding='gbk',errors='ignore') as f:
    print(f.read())

# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

with open('D:/python/test2.txt','w') as f:
    f.write('hello world!')

# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。

fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)


# 重点:在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。