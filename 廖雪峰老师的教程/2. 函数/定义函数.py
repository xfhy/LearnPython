
import math

'''
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
'''

# 定义函数 求绝对值
def my_abs(x):
    # 数据类型检查可以用内置函数isinstance()实现：
    if not isinstance(x, (int, float)):  # 判断类型
        raise TypeError("bad operand type")  # 抛出错误
    if x > 0:
        return x
    else:
        return -x


def nop():
    pass


print(my_abs(-3))
#print(my_abs('1'))

# 返回多个值


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi/6)
r = move(100, 100, 60, math.pi/6)
print(x,y)
print(r)  # 返回的其实是元组 tuple

# 练习
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('a 类型不对')
    if not isinstance(b,(int,float)):
        raise TypeError('b 类型不对')
    if not isinstance(c,(int,float)):
        raise TypeError('c 类型不对')
    dart = b*b-4*a*c
    if dart<0:
        print("方程无解")
        return
    sqrtData = math.sqrt(dart)
    aa = 2*a
    return (-b+sqrtData)/aa,(-b-sqrtData)/aa

print(quadratic(4,-1,0))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
