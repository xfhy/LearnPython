'''
有些网站为了避免别人使用爬虫恶意采取信息会进行一些反爬虫的操作， 
比如通过请求头里的User-Agent，检查访问来源是否为正常的访问途径， 
我们可以修改请求头来进行模拟正常的访问。Request中有个headers参数， 
有两种方法进行设置： 
1.把请求头都塞到字典里，实例化Request对象的时候传入 
2.通过Request对象的add_header()方法一个个添加
'''

import urllib.request

novel_url = "http://www.biqukan.com/1_1496/"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/63.0.3239.84 Safari/537.36',
           'Referer': 'http://www.baidu.com',
           'Connection': 'keep-alive'}
novel_req = urllib.request.Request(novel_url,headers=headers)
# urlopen函数时添加timeout参数，单位是秒
novel_resq = urllib.request.urlopen(novel_req,timeout=20)

with open("D:/python/biqukan.txt",'w') as f:
    f.write(novel_resq.read().decode('gbk'))

'''
 延迟提交数据
一般服务器会对请求的IP进行记录，如果单位时间里访问的次数达到一个阀值， 
会认为该IP地址是爬虫，会弹出验证码验证或者直接对IP进行封禁。一个最简单 
的方法就是延迟每次提交的时间，直接用time模块的sleep(秒) 函数休眠下。
'''