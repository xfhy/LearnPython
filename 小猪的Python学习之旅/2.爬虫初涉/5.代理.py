'''
对应限制ip访问速度的情况我们可以使用延迟提交数据的做法， 
但是有些是限制访问次数的，同一个ip只能在一段时间里访问 
多少次这样，而且休眠这种方法效率也是挺低的。更好的方案是 
使用代理，通过代理ip轮换去访问目标网址。 
'''

import urllib.request

# 使用ip代理
ip_query_url = "https://www.baidu.com/"
# 1.创建代理处理器，ProxyHandler参数是一个字典{类型:代理ip:端口}
proxy_support = urllib.request.ProxyHandler({'http':'118.114.245.44:8080'})

# 2.定制，创建一个opener
opener = urllib.request.build_opener(proxy_support)

# 3. 安装opener
urllib.request.install_opener(opener)

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (X11; Linux x86_64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.84 Safari/537.36',
    'Host': 'https://www.baidu.com/'
}
MAX_NUM = 10    # 有时网络堵塞，会报URLError错误，所以加一个循环
request = urllib.request.Request(ip_query_url,headers=headers)

for i in range(MAX_NUM):
    try:
        response = urllib.request.urlopen(request,timeout=20)
        html = response.read()
        with open("D:/python/"+i+".txt") as f:
            f.write(html.decode('utf-8'))
    except:
        if i < MAX_NUM-1:
            continue
        else:
            print("urllib.error.URLError: <urlopen error timed out>")
    
'''
如图代理成功，这里的网站是用于查询请求ip的，另外，我们一般会弄一个 
代理ip的列表，然后每次随机的从里面取出一个来使用。
'''