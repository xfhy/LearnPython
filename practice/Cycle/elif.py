# count = input()
# print(count)
#
# a = input()  # Read a string from standard input.  The trailing newline is stripped.
# a += 1     # 不能输入英文 TypeError: Can't convert 'int' object to str implicitly
# python input()输入的是str类型
# print(type(a))

count = int(input("请输入一个数字:"))

if count < 0:
    print("%d<0" % count)
elif count == 0:
    print("%d==0" % count)
else:
    print("%d>0" % count)
