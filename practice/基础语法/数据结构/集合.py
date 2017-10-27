# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。集合对象还支持 union（联合），intersection（交），difference（差）和 symmetric difference（对称差集）等数学运算。

# 大括号或 set() 函数可以用来创建集合。注意：想要创建空集合，你必须使用 set() 而不是 {}。后者用于创建空字典，我们在下一节中介绍的一种数据结构。

# 下面是集合的常见操作：
basket = {'a', 'b', 'c', 'd', 'e', 'f'}
print(basket)  # 集合是无序的

# 判断元素是否在集合中
if 'aa' in basket:
    print('aa' in basket)
else:
    print('aa' in basket)

# 用set函数创建集合  集合会自动去掉重复元素
a = set('adadafasfas')
print(a)  # {'f', 's', 'a', 'd'}  # a 去重后的字母
b = set('dadasd')
print(a - b)  # a 有而 b 没有的字母
print(a | b)  # 存在于a或者b的字母
print(a & b)  # a和b公有的部分字母
print(a ^ b)  # 存在于a或b但不同时存在的字母

# 从集合a中弹出元素  注意:是随机的
print(a.pop())
print(a)
a.add('g')  # 添加元素到集合  注意:也是随机的
print(a)
