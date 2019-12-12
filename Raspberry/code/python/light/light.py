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


####  定义Light类
class Light(object):
####  定义Light类的构造函数
	def __init__(self,pin):
		self.pin = pin
####  self.pins是可以使用的端口列表
		self.pins = [5,6,12,13,16,17,18,19,20,21,22,23,24,25,26,27]
		self.up_time = 0.5
		self.down_time = 0.5
		self.check_pin(pin)
		self.run()

	def run(self):
		self.setup(self.pin)
		try:
			self.loop(self.pin)
		except KeyboardInterrupt:
			self.destroy(self.pin)

####  check_pin函数负责检测输入的端口是否符合要求
	def check_pin(self,pin):
		if pin in self.pins:
			print("%d 是有效编号"%pin)
		else:
			print("只能输入以下有效的pin编号")
			for i in self.pins:
				print i,
			exit()

####  setup函数将端口初始化
	def setup(self,pin):
		#初始化GPIO口
		#采用BCM编号
		GPIO.setmode(GPIO.BCM)
		#设置GPIO为输出状态，输入低电平
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,GPIO.LOW)

####  loop函数将led灯循环点亮
	def loop(self,pin):
		for i in xrange(1,10):
			GPIO.output(pin,GPIO.HIGH)
			print("light up")
			time.sleep(self.up_time)
			GPIO.output(pin,GPIO.LOW)
			print("light down")
			time.sleep(self.down_time)


####  恢复GPIO口状态
	def destroy(self,pin):
		GPIO.output(pin,GPIO.LOW)
		GPIO.setup(pin,GPIO.IN)

if __name__ == '__main__':
	light = Light(12)
