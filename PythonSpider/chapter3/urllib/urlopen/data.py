import urllib.request
import urllib.parse

# 有了data参数就不是GET请求了,而是POST请求
# data就是入参
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='UTF-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

# 运行结果   可以看到我们传递的参数在form字段中这表明了是模拟了表单的提交方式,以POST的方式传输数据
'''
{
    "args":{

    },
    "data":"",
    "files":{

    },
    "form":{
        "word":"hello"
    },
    "headers":{
        "Accept-Encoding":"identity",
        "Connection":"close",
        "Content-Length":"10",
        "Content-Type":"application/x-www-form-urlencoded",
        "Host":"httpbin.org",
        "User-Agent":"Python-urllib/3.6"
    },
    "json":null,
    "origin":"171.213.29.85",
    "url":"http://httpbin.org/post"
}
'''
