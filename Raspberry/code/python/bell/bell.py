#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author  :hstking
#E-mail  :hstking@hotmail.com
#Ctime   :2015/08/30
#Mtime   :
#Version :

import RPi.GPIO as GPIO
import time
import sys
import string


####  定义Bell类
class Bell(object):
####  定义Bell类的构造函数
	def __init__(self,pin):
		self.pin = pin
		self.pins = [5,6,12,13,16,17,18,19,20,21,22,23,24,25,26,27]
		self.up_time = 1.5
		self.down_time = 0.5
		self.check_pin(pin)
		self.run()

	def run(self):
		self.setup(self.pin)
		try:
			self.loop(self.pin)
		except KeyboardInterrupt:
			self.destroy(self.pin)

####  检查端口是否符合要求
	def check_pin(self,pin):
		if pin in self.pins:
			print("%d 是有效编号"%pin)
		else:
			print("只能输入以下有效的pin编号")
			for i in self.pins:
				print i,
			exit()

####  初始化端口
	def setup(self,pin):
		#采用BCM编号
		GPIO.setmode(GPIO.BCM)
		#设置GPIO为输出状态，输入低电平
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,GPIO.LOW)

####  循环给端口输出高电平
	def loop(self,pin):
		for i in xrange(1,10):
			GPIO.output(pin,GPIO.HIGH)
			print("bell up")
			time.sleep(self.up_time)
			GPIO.output(pin,GPIO.LOW)
			print("bell down")
			time.sleep(self.down_time)

	def destroy(self,pin):
		#恢复GPIO口状态
		GPIO.output(pin,GPIO.LOW)
		GPIO.setup(pin,GPIO.IN)

if __name__ == '__main__':
	bell = Bell(18)
