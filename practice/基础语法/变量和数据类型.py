# 在 python 中 我们不需要为变量指定数据类型。所以你可以直接写出 abc = 1 ，这样变量 abc 就是整数类型。如果你写出 abc = 1.0 ，那么变量 abc 就是浮点类型。

# python 也能操作字符串，它们用单引号或双引号括起来，就像下面这样。
abc = 1
b = 1.3
c = 'a'
e = "da"
的 = 'ada'
h = 'dadasdasdasdsadas'

print(type(e))

number = 5  # int(input("请输入一个整数:"))
if number < 200:
    print("%d < 200" % number)
else:
    print("%d >= 200" % number)

inrate = 1
value = 12.13545
# 字符串格式化，大括号和其中的字符会被替换成传入 str.format() 的参数，也即 year 和 value。其中 {:.2f} 的意思是替换为 2 位精度的浮点数。
print("year {} haha {:.2f}".format(inrate, value))
# 更多字符串格式化内容:https://docs.python.org/3/library/string.html#formatstrings

# 求n个数的平均值
sum = 0
for num in range(1, 100):
    sum += num
print("{:.2f}".format(sum / 100))

# 温度转换
fahrenheit = 0
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8  # 转换为摄氏度
    # {:5d} 的意思是替换为 5 个字符宽度的整数，宽度不足则使用空格填充。
    print("{:5d} {:7.2f}".format(fahrenheit, celsius))
    fahrenheit += 25

# 单行定义多个变量和赋值

aa, bb = 12, 45
print(aa)
print(bb)

# 交换2个数的值
aa, bb = bb, aa
print(aa)
print(bb)

# 元组
# 元组封装
data = {"aaaaa", "bbbbb", "ccccc"}
# 元组拆封  这里拆封的时候,赋值是无序的   比如name可能是aaaaa,也可能是bbbbb,也可能是ccccc
name, coun, langt = data
print(name)
print(coun)
print(langt)
