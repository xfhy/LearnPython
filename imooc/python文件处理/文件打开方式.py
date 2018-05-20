import os

f = open('D:/python/test.txt','w') # 不存在则创建,存在则清空
f.writelines('插入的值')
print(type(f))
f.close()