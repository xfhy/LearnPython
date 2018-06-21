'''
PS：下面用到的json模块：用于将Python原始类型与json类型相互转换,使用 
如果是读取文件可以用：dump()和load()方法，字符串的话用下述两个：

dumps()编码 [Python -> Json] 
dict => object      list, tuple => array      str => string      True => true 
int, float, int- & float-derived Enums => number      False => false     None => null

loads()解码 [Json -> Python] 
object => dict     array => list     string => str     number (int) => int 
number(real) => float     true =>True     false => False     null => None
'''

import urllib.request
import json

# 模拟get
get_url = "http://gank.io/api/data/" + urllib.request.quote('福利')+"/1/1"
get_resq = urllib.request.urlopen(get_url)

# 解码   转成json
get_result = json.loads(get_resq.read().decode('utf-8'))
# print(get_result)
print(type(get_result))  #<class 'dict'>

# 编码
get_result_format = json.dumps(get_result, indent=2, sort_keys=True, ensure_ascii=False)
print(type(get_result_format))  #str
# print(get_result_format)


# 模拟Post
post_url = "http://xxx.xxx.login"
phone = "13555555555"
password = "111111"
values = {
    'phone': phone,
    'password': password
}
data = urllib.parse.urlencode(values).encode(encoding='utf-8')
req = urllib.request.Request(post_url, data)
resp = urllib.request.urlopen(req)
result = json.loads(resp.read())    # Byte结果转Json
print(json.dumps(result, sort_keys=True, 
                 indent=2, ensure_ascii=False)) # 格式化输出Json