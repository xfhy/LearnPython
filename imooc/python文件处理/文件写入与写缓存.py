f = open("D:/python/text.txt",'w')

f.writelines('aab')
f.writelines(('a','b','c'))
f.writelines(['a','b','c'])

f.flush()  # 缓存同步到磁盘

f.close()  # 这一步也会同步内容到磁盘

# 写入数据量大于或者等于写缓存,写缓存会同步到磁盘