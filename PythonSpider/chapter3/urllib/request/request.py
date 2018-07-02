import urllib.request
import urllib.parse

# Request可以配置灵活的参数
'''
构造方法如下所示  可以传入参data,header方法,method等

data必须是bytes类型的,如果它是字典,则可以先用urllib.parse模块里的urlencode()编码

header是一个字典,它是请求头.最常用的是修改User--Agent来伪装浏览器,默认的是Python-urllib.比如伪装火狐浏览器:Mozilla/5.0 (X11; U; Linux i686) 
Gecko/20071127 Firefox/2.0.0.11



def __init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False,
                 method=None)
'''
url = 'https://python.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Window NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(urllib.parse.urlencode(dict), encoding='UTF-8')
request = urllib.request.Request(url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(request)
print(response.read().decode('UTF-8'))
