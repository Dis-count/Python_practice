#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author  :hstking
#E-mail  :hstking@hotmail.com
#Ctime   :2015/08/27
#Mtime   :
#Version :

import urllib2
import re
import os


####  定义GetNip类
class GetNip():
####  定义构造函数，可以用于定义类变量
	def __init__(self):
		self.logPath = os.path.expanduser('~') + os.sep + 'log'
		self.nipFile = self.logPath + os.sep + 'Nip.txt'
		self.Nip = None

		self.getNip()
		self.writeNip()

####  从网络取得本地的公网IP
	def getNip(self):
		urls = 'http://1111.ip138.com/ic.asp'
		if urllib2.urlopen(urls).geturl() == urls:
			rawString = urllib2.urlopen(urls).read()
			self.Nip = re.search(b'\d+\.\d+\.\d+\.\d+',rawString).group()
			print("Nip = %s"%self.Nip)
		else:
			print("未取得本机NIP")

####  将取得的公网IP写入指定文件中
	def writeNip(self):
		if os.path.isdir(self.logPath):
			pass
		else:
			os.makedirs(self.logPath)
		with open(self.nipFile,'w') as FP:
			FP.write(self.Nip)


####  以下是脚本的主程序
if __name__ == '__main__':
	nip = GetNip()
