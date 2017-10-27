squares = []
for x in range(10):
    squares.append(x ** 2)  # x的平方
print(squares)
print(x)
# 注意这个 for 循环中的被创建（或被重写）的名为 x 的变量在循环完毕后依然存在。使用如下方法，我们可以计算 squares 的值而不会产生任何的副作用：。
squares = list(map(lambda a: a ** 2, range(10)))
print(squares)
# 等价于下面的列表推导式。
squares = [c ** 2 for c in range(10)]
print(squares)

# 列表推导式由包含一个表达式的中括号组成，表达式后面跟随一个 for 子句，之后可以有零或多个 for 或 if 子句。结果是一个列表，由表达式依据其后面的 for 和 if 子句上下文计算而来的结果构成。
c = [(x, y) for x in [1, 2, 3] for y in [2, 3, 1] if x != y]
print(c)

# 值得注意的是在上面两个方法中的 for 和 if 语句的顺序。

# 列表推导式也可以嵌套。
a = [1, 2, 3]
z = [x + 1 for x in [x**2 for x in a]]
print(z)
