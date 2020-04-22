import requests
#模拟请求的库
import re
#正则匹配的库
import pymysql
#连接mySql数据库
httpUrl = 'https://pvp.qq.com/web201605/js/herolist.json'
#设置请求链接地址
resList = requests.get(httpUrl)
#通过链接地址获取英雄列表JSON数据
resList = resList.json()
print(resList)
db = pymysql.connect('localhost','root','root','pydata')
cursor = db.cursor()
for i in  range(len(resList)):
    item = resList[i]
    #print(item)
    cursor = db.cursor()
    sqlStr = 'insert into `heros` (`ename`,`cname`,`title`,new_type,hero_type,skin_name) values ("{}","{}","{}","{}","{}","{}")'
    sqlStr = sqlStr.format(item['ename'],item['cname'],item['title'],item['new_type'],item['hero_type'],item.get('skin_name'))
    print(sqlStr)
    #执行插入、更新相关操作
    cursor.execute(sqlStr)
    db.commit()
    
# httpUrl = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(ename)
# #王者荣耀英雄页面链接地址
# result = requests.get(httpUrl)
# #获取英雄页面内容
# result.encoding = 'gbk'
# #设置解析页面的编码
# print(result.text)


def getHeroInfo(ename):
    httpUrl = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(ename)
    result = requests.get(httpUrl)
    result.encoding = 'gbk'
    #print(result.text)
    #设置正则对象匹配的模式
    regObj = re.compile(r'(<div class="skill-show">.*?</div>)\s+</div>\s+</div>.*?<p class="sugg-tips">(.*?)</p>',re.S)
    #找出所有需要匹配的内容
    regRes = regObj.findall(result.text)
    skill = regRes[0][0]
    suggtips = regRes[0][1]
    #写数据库更新语句
    sqlStr = "update heros set skill='{}',`sugg-tips`='{}' where ename = '{}'".format(skill,suggtips,ename)
    print(sqlStr)
    #将获取内容写入数据库
    cursor.execute(sqlStr)
    db.commit()


httpUrl = 'https://pvp.qq.com/web201605/js/herolist.json'
resList = requests.get(httpUrl)
resList = resList.json()

for i in  range(len(resList)):
    item = resList[i]
    getHeroInfo(item['ename'])
