#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 上面是标准注释,第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

# 这是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
'a test module'

# 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
__author__ = 'xfhy'

import sys


def test():
    args=sys.argv
    if len(args)==1:
        print("hello world!")
    elif len(args)==2:
        print("hello,%s!" % args[1])
    else:
        print("Too many arguments!")

# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__=='__main__':
    test()


# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
def _private_1(name):
    return "hello,%s" % name

def _private_2(name):
    return "Hi,%s" % name

def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)
'''
我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
'''
