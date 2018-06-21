#下载图片

import urllib.request

pic_url = "http://static.zybuluo.com/coder-pig/agr9d5uow8r5ug8iafnl6dlz/1.jpg"
pic_resp = urllib.request.urlopen(pic_url)
pic = pic_resp.read()

#将内容写入文件
with open("D:/python/LeiMu.jpg",'wb') as f:
    f.write(pic)

# 也可以直接调用urlretrieve下载，比如下载音频
music_url = "http://7xl4pr.com2.z0.glb.qiniucdn.com/" \
            "%E4%B8%83%E7%94%B0%E7%9C%9F%E4%B8%93%E5%8C%BA%2F%E4%" \
            "B8%AD%E6%96%87%E8%AF%BE%2F%E6%83%B3%E8%" \
            "B1%A1%E7%82%B9%E5%8D%A1%2F%2B6.mp3"
urllib.request.urlretrieve(music_url, "儿歌.mp3")