# for line in open("1.txt"):
#     print line,
import re

read = open('1.txt', 'r')
write = open('2.txt', 'w')

lines = read.readlines()
for temp in lines:
    temp = ' '.join(filter(lambda x: x, temp.split(' ')))
    print(temp)
    write.writelines(temp)


read.close
write.close
