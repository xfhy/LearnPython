import urllib.request

# 下载网页
response = urllib.request.urlopen('http://www.baidu.com')

print(response.getcode()) #获取状态码  200为成功
#print(response.read())  # 获取内容

print(type(response.read()))


print(response.geturl())