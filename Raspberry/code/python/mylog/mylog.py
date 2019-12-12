#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author  :hstking
#E-mail  :hstking@hotmail.com
#Ctime   :2015/09/15
#Mtime   :
#Version :

import logging
import getpass
import os
import sys


#### 定义MyLog类
class MyLog(object):
#### 类MyLog的构造函数
	def __init__(self):
		self.user = getpass.getuser()
		self.logger = logging.getLogger(self.user)
		self.logger.setLevel(logging.DEBUG)
####  日志目录
		self.logPath = '/home/pi/log'
####  日志文件名
		self.logFile = self.logPath + os.sep + sys.argv[0][0:-3] + '.log'
		self.formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

####  日志显示到屏幕上并输出到日志文件内
		self.logHand = logging.FileHandler(self.logFile)
		self.logHand.setFormatter(self.formatter)

		self.logHandSt = logging.StreamHandler()
		self.logHandSt.setFormatter(self.formatter)

		self.logger.addHandler(self.logHand)
		self.logger.addHandler(self.logHandSt)

####  日志的5个级别对应以下的5个函数
	def debug(self,msg):
		self.logger.debug(msg)

	def info(self,msg):
		self.logger.info(msg)

	def warn(self,msg):
		self.logger.warn(msg)

	def error(self,msg):
		self.logger.error(msg)

	def critical(self,msg):
		self.logger.critical(msg)

if __name__ == '__main__':
	mylog = MyLog()
	mylog.debug("I'm debug")
	mylog.info("I'm info")
	mylog.warn("I'm warn")
	mylog.error("I'm error")
	mylog.critical("I'm critical")
