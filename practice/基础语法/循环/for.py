# 通过 for 语句我们可以使用 for 循环。Python 里的 for 循环与 C 语言中的不同。这里的 for 循环遍历任何序列（比如列表和字符串）中的每一个元素。下面给出示例：
a = [21, "is", "dada", 2.3, 2, 3, 4, 5, 56, 5, 6, 7]
for x in a:
    print(x, end=' ')
print()
for x in a[::2]:
    print(x, end=' ')

# range() 函数
# 如果你需要一个数值序列，内置函数 range() 会很方便，它生成一个等差数列（并不是列表）
for i in range(1, 4):  # 输出 1-3
    print(i)

# 我们可以在循环后面使用可选的 else 语句。它将会在循环完毕后执行，除非有 break 语句终止了循环。
# python 中 for 循环的 else 子句给我们提供了检测循环是否顺利执行完毕的一种优雅方法
# 如果在for循环中出现异常,那么else不会被调用
for i in range(0, 4):
    print(i)
    # 3/0 # ZeroDivisionError: division by zero
else:
    print("else")
