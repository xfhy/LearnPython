import urllib.request


response = urllib.request.urlopen('https://www.baidu.com')
# print(response.read().decode('UTF-8'))
print(type(response))  #<class 'http.client.HTTPResponse'>
print(response.status) # 状态码  正常则是200   404是未找到网页
print(response.getheaders()) # 获取所有header 
print(response.getheader('Server')) # 获取某个header的值

# urlopen()是可以传很多参数的