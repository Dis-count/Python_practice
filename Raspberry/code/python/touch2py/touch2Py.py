#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import time


####  定义creatFile函数
def creatFile(name):
	f = open(name,'w')
	for head in pyHead:
		f.write(head)
		f.write('\n')
	f.write('\n')
	f.close()

####  下面是主程序
if __name__ == '__main__':
	global pyHead
####  定义字符串列表
	pyHead = [
'#!/usr/bin/env python',
'# -*- coding:utf-8 -*-',
'#Author  :hstking',
'#E-mail  :hstking@hotmail.com',
'#Ctime   :' + time.strftime("%Y/%m/%d"),
'#Mtime   :',
'#Version :',
'\n\n\n\n',
"if __name__ == '__main__':"
]
	
	if len(sys.argv) == 1: 
		print '请输入文件名\n'

	fileNames = sys.argv[1:]
	for name in fileNames:
		if (os.path.isfile(name) or os.path.isdir(name) or os.path.islink(name)):
			print name,"已经存在"
		else:
			creatFile(name)
