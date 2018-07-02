import urllib.request
from bs4 import BeautifulSoup
from urllib import error

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/63.0.3239.84 Safari/537.36'}
novel_url = "http://www.biqukan.com/1_1496/"  # 小说页面地址
base_url = "http://www.biqukan.com"  # 根地址，用于拼接
save_dir = 'D:/python/'

# 创建代理处理器，ProxyHandler参数是一个字典{类型:代理ip:端口}
proxy_support = urllib.request.ProxyHandler({'https': '125.120.201.168:6666'})
opener = urllib.request.build_opener(proxy_support)
# 安装opener
urllib.request.install_opener(opener)


# 获取所有章节


def get_chapter_url():
    chapter_req = urllib.request.Request(novel_url, headers=headers)
    chapter_resp = urllib.request.urlopen(chapter_req)
    chapter_content = chapter_resp.read()

    # find_all返回一个bs4.element.ResultSet 对象，for循环遍历一波
    # 这个对象，(迭代对象的类型是：bs4.element.Tag)
    chapter_soup = BeautifulSoup(chapter_content, 'html.parser')

    # 取出章节部分
    listmain = chapter_soup.find_all(attrs={'class': 'listmain'})

    # with open("D:/python/小说抓取.txt", 'w+') as f:
    a_list = []
    for i in listmain:
        if 'a' not in str(i):
            continue
        for d in i.find_all('a'):  # 寻找a标签
            a_list.append(d)

    # 前面的12行是最新章节  无用的
    return a_list[12:]
    # with open("D:/python/小说抓取.txt", 'w') as f:
    #     f.writelines(str(a_list[12:]))


# 传入对象为bs4.element.Tag


def get_chapter_content(chapter):
    # 拼接url
    chapter_url = base_url + chapter.attrs.get('href')  # 获取url
    # chapter_name = chapter.string  # 获取章节名称
    chapter_req = urllib.request.Request(chapter_url, headers=headers)
    chapter_resp = urllib.request.urlopen(chapter_req, timeout=20)
    chapter_content = chapter_resp.read()
    chapter_soup = BeautifulSoup(chapter_content, 'html.parser')

    # 查找章节部分内容
    show_txt = chapter_soup.find_all(attrs={'class': 'showtxt'})
    for txt in show_txt:
        save_chapter(txt, chapter.string, save_dir + '小说抓取.txt')


# 存储章节内容
def save_chapter(txt, chapter_name, file_path):
    try:
        with open(file_path, 'a+', encoding="utf-8") as f:
            f.writelines("\n\n")
            f.writelines("----" + chapter_name + "----\n")  # 标题
            f.write(txt.get_text(strip=True))
            f.writelines("\n\n")
    except (error.HTTPError, OSError) as reason:
        print(str(reason))
    else:  # 没出问题就调用这里
        print('下载完成:' + chapter_name)


if __name__ == '__main__':
    novel_list = get_chapter_url()
    for chapter in novel_list:
        get_chapter_content(chapter)
