# 方法 title() 返回字符串的标题版本，即单词首字母大写其余字母小写。
s = 'shi yan lOu'
print(s.title())
print(s.upper())  # 大写
print(s.lower())  # 小写
print(s.swapcase()) # 大->小  小->大写

s = 'dhasj 43143vs'
print(s.isalnum())  # 判断是否是 字母或者数字  False  这里包含了空格

s = '45235432'
print(s.isalpha()) # 方法 isalpha() 检查字符串之中是否只有字母。
print(s.isdigit()) # 检查字符串是否所有字符为数字

# 我们可以使用 split() 分割任意字符串，split() 允许有一个参数，用来指定字符串以什么字符分隔（默认为 " "），它返回一个包含所有分割后的字符串的列表。
s = 'dada dada fdsfdsf'
print(s.split(" "))

# 相反的，方法 join() 使用指定字符连接多个字符串，它需要一个包含字符串元素的列表作为输入然后连接列表内的字符串元素。
a = '-'
b = 'dada dada fdsfsd'
c = a.join(b.split(" "))
print(c)
