n = 0
# 非0为真
while n < 11:
    # print(n)
    n += 1

# 斐波那契（Fibonacci）数列
a, b = 0, 1
while b < 100:
    # 这里先执行a+b赋值给b,再执行b赋值给a
    # print(b, end=' ')
    a, b = b, a + b

# 我们来写一个程序计算幂级数：e^x = 1 + x + x^2 / 2! + x^3 / 3! + ... + x^n / n! （0 < x < 1）。
x = 0.5
n = term = num = 1
result = 1.0
while n < 100:
    num *= n  # 阶乘
    term *= x  # x的n次方
    result += term / num
    n += 1
    if term < 0.0001:
        break
print(result)

# 打印10以内的乘法表
print("-" * 50)
for i in range(1, 10):  # 这里的区间是[1,10)
    for j in range(1, 10):
        print("{:4d}".format(i * j), end=' ')
    print()
print("-" * 50)

n = 5
while n >= 0:
    print("*" * n)
    n -= 1
