import os

print(os.name) # 操作系统类型 #nt
print(os.environ) #系统的环境变量

# 获取某个环境变量的值
print(os.environ.get('PATH'))

# 操作文件和目录

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录
# 1.首先把新目录的完整路径表示出来
os.path.join('D:/python','testdir')
# 2.然后创建一个目录  如果已经存在该文件夹,则创建失败
# os.mkdir('D:/python/testdir')  

# 删除一个目录  删除时如果找不到会报错
# os.rmdir('D:/python/testdir')

# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('/Users/michael/testdir/file.txt')) # ('/Users/michael/testdir', 'file.txt')

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('/path/to/file.txt')) # ('/path/to/file', '.txt')

# 文件重命名
# os.rename('D:/test.txt','test.py')

# 删除文件
# os.remove('D:/test.txt')

# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
print([x for x in os.listdir('.') if os.path.isdir(x)]) # generator 表达式

# 要列出所有的.py文件，也只需一行代码：
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。


'''
练习

编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
'''
def searchFiles(direct,filename):
    try:
        files = os.listdir(direct)  # 列出direct目录的所有文件夹
        for file in files:
            fullfile = os.path.join(direct,file)
            if os.path.isdir(fullfile):
                searchFiles(fullfile,filename)
            if os.path.isfile(fullfile) and filename in file:
                print(os.path.abspath(fullfile))
    except Exception as e:
        print(e)

searchFiles('d:/','test.py')