
f = open('D:/python/test.txt')

#f.read()   #读取全部
#f.read(2)  读取2个字符 

#print(f.readline())   读取一行内容
#print(f.readline(10))  读取10个字符
# print(f.readline(2))  # 读取2个字符  里面是汉字时,会读取2个汉字

#print(f.readlines())

# 迭代器(推荐)  不消耗大量内存  使用next()动态计算下一次的值   不会把内容全部读取到内存中
iter_f = iter(f)
for line in iter_f:
    print(line)
