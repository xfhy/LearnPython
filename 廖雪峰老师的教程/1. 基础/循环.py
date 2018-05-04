
# for..in 循环
names = ['dada', '小米', '小明']
for name in names:
    print(name)

# 计算1+2+3+4
    # 方式1
sum = 0
for x in [1, 2, 3, 4]:
    sum += x
print(sum)

# 方式2
# range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数(0,1,2,3,4)：
sum = 0
for x in range(101):
    sum += x
print(sum)

# while

# 计算100以内所有奇数之和

sum = 0
x = 0
while x <= 100:
    if x % 2 != 0:
        sum += x
    x += 1
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("hello,", name)

# break
n=1
while n<=100:
    print(n)
    if n>10:
        break
    n+=1


# continue 和java一样的

for i in [1,2,3]:
    if i==2:
        continue
    print(i)



