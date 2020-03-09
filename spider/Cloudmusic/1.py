def urlBS(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    return soup

## 网易云批量下载

# 首先找到你要下载的歌曲，用网页版打开，复制链接中的歌曲ID，如：http://music.163.com/#/song?id=476592630 这个链接ID就是 476592630
# 然后将ID替换到链接 http://music.163.com/song/media/outer/url?id=ID.mp3 中的ID位置即可获得歌曲的外链：http://music.163.com/song/media/outer/url?id=476592630.mp3


import requests # 用于获取网页内容的模块
from bs4 import BeautifulSoup   # 用于解析网页源代码的模块
header={	# 伪造浏览器头部，不然获取不到网易云音乐的页面源代码
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit
