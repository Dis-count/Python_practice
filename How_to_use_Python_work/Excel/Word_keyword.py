import re
import zipfile
import os
def get_document(filepath):
    z = zipfile.ZipFile(filepath, "r")
    text = z.read("word/document.xml").decode("UTF-8")
    text = re.sub(r"<.*?>", "", text) #去除xml里的所有标记符
    ###如果多份简历在同一个word文件里###
    table_list = text.split("XX简历")[1:]#依据简历标题切分每一份简历信息
    return table_list

def get_field_value(text):
    value_list = []
    m = re.findall(r"姓 名(.*?)性    别", table)
    value_list.append(m)
    m = re.findall(r"性    别(.*?)学    历", table)
    value_list.append(m)
    m = re.findall(r"民 族(.*?)健康状况", table)
    value_list.append(m)
    '''
    此处省略其他字段匹配
    '''
    return value_list

cv_list = []
for i in os.listdir(os.getcwd()):
    a = os.path.splitext(os.getcwd() + "\\" + i)#获取当前目录下所有文件的文件名
    if a[1] == '.docx':#如果文件后缀
        print(os.getcwd()+"\\"+i)
        cv_list = cv_list + get_document(os.getcwd() + "\\" + i)#每份简历信息为一个列表元素

for i in cv_list:
    value_list = get_field_value(i)
    str1 = ""
    for value in value_list:
        str1 = str1 + str(value[0]) + "\t"
    str1 = str1 + "\n"
    with open("result.txt", "a+") as f:
        f.write(str1)

# 原文链接：https://blog.csdn.net/geoker/article/details/80149463
#  1、 数据抓取  导入表格
#  2、 word 文字匹配
#  3、 建立多链接的文件关系
