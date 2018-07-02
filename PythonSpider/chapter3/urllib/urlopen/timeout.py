# timeout是设置超时时间的 超时则会抛异常

import urllib.request
import urllib.error
import socket

# 技巧 :有时一个网页很长时间未响应,则跳过该网页的抓取
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('time out')

print(response.read())
