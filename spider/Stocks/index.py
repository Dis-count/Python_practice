from pyquery import PyQuery as pq
import pymysql
def newsUrl():
    url = 'https://stock.cngold.org/rumen/'
    #通过链接和编码获取页面内容
    doc = pq(url,encoding="utf-8")
    #通过css选择器获取所有的链接标签
    lista = doc('.news_list li a')
    print(lista)
    for i,item in  enumerate(lista):
        #通过yield关键词将newsUrl变成生成器，可进行循环迭代
        yield doc(item).attr('href')

#newsUrl()

def parsePage(url):
    doc = pq(url,encoding="utf-8")
    #获取标题
    titleDom = doc('body > div.main.w1000 > div.heading1.w1000.mt20.clearfix > h1')
    title = titleDom.text()
    #获取简介
    summary = doc('body > div.main.w1000 > div.article.clearfix > div.main_left.fl > div.summary > p').text()
    tempDom = doc('body > div.main.w1000 > div.article.clearfix > div.main_left.fl > div.article_con')
    tempDom.remove('script')
    #删除内容中的script标签
    #通过获取下一页标签，获取下一页新闻内容
    content = tempDom.html()
    nextPageUrl = doc('.listPage a:contains("下一页")').attr('href')
    while nextPageUrl:
        tempDoc = pq(nextPageUrl,encoding="utf-8")
        tempDom = tempDoc('body > div.main.w1000 > div.article.clearfix > div.main_left.fl > div.article_con')
        tempDom.remove('script')
        content += tempDom.html()
        nextPageUrl = tempDoc('.listPage a:contains("下一页")').attr('href')
    #设置数据库插入语句
    sqlStr = "insert into stocknews (title,summary,content) values ('{}','{}','{}')".format(title,summary,content)
    #插入到数据库
    cursor.execute(sqlStr)
    db.commit()
    print(title)
#parsePage('https://stock.cngold.org/rumen/c6694940.html')


if __name__ == "__main__":
    #连接数据库
    db = pymysql.connect('localhost','root','root','pydata')
    #获取游标
    cursor = db.cursor()
    newsListUrl = newsUrl()
    for url in newsListUrl:
        print(url)
        parsePage(url)
    db.close()
