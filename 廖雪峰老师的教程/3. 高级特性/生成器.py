# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 外层是()
g = (x*x for x in range(1, 11))
print(next(g))  # 1

for n in g:
    print(n)

# 斐波拉契序列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1
    return 'done'

# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
g = fib(6)

# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

for n in g:
    print(n)

'''
# 获取generator函数返回值
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break
'''

# 练习
def triangles(max):
    n = 0
    L = []
    while True:
        yield L
        if n > max:
            break
                    # 2项之和
        L = [1]+[L[i]+L[i+1] for i in range(n)]+[1]
        n = n + 1
    return 'done'  


for i in triangles(10):
    print(i)

'''
generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。

要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

请注意区分普通函数和generator函数，普通函数调用直接返回结果：
 r = abs(6)
 r
6
generator函数的“调用”实际返回一个generator对象：

 g = fib(6)
 g
<generator object fib at 0x1022ef948>
'''