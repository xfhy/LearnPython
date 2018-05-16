def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


# print(fact(1000))  # Traceback   栈溢出


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


move(3, 'a', 'b', 'c')


L = []
n = 1
while n < 99:
    L.append(n)
    n = n+1

print(L)
