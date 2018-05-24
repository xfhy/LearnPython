# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):  # *args 接收多个参数
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
print(f)
print(f())
# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。





# 闭包

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
    
fun1,fun2,fun3 = count()  #返回3个函数
print(fun1()) # 9
print(fun2()) # 9
print(fun3()) # 9
# 在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。

# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是： 9 9 9 

# 重点:返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    i=0
    def counter():
        nonlocal i
        i = i + 1
        return i
    return counter

# nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。

# nonlocal用于声明，修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


'''
小结

一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
'''