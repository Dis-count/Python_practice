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

class Light():
	def __init__(self):
		self.pins = [5,6,12,13,16,17,18,19,20,21,22,23,24,25,26,27]
		self.args = self.input_arg()
		self.pin = self.args[0]
		self.up_time = self.args[1]
		self.down_time = self.args[2]
		self.run()

	def input_arg(self):
		print("输入light占用的GPIO口编号")
		print("只能从以下的编号中选择")
		for i in self.pins:
			print i,
		print
		try:
			pin = int(raw_input("GPIO口编号:"))
		except ValueError:
			print("请按要求输入，谢谢")
			exit()
		self.check_pin(pin)
		print("输入light亮灯时间[0.5--2]")
		try:
			up_time = string.atof(raw_input("light亮灯时间:"))
		except ValueError:
			print("请按要求输入，谢谢")
			exit()
		self.check_time(up_time)
		print("输入light关灯时间[0.5--2]")
		try:
			down_time = string.atof(raw_input("light关灯时间:"))
		except ValueError:
			print("请按要求输入，谢谢")
			exit()
		self.check_time(down_time)
		args = []
		args.append(pin)
		args.append(up_time)
		args.append(down_time)
		return args

	def run(self):
		self.setup(self.pin)
		try:
			self.loop(self.pin,self.up_time,self.down_time)
		except KeyboardInterrupt:
			self.destroy(self.pin)

	def check_pin(self,pin):
		if pin in self.pins:
			print("%d 是有效编号"%pin)
		else:
			print("只能输入以下有效的pin编号")
			for i in self.pins:
				print i,
			exit()

	def check_time(self,time):
		if (time > 2):
			print("时间太长了,重新输入")
			exit()
		elif (time < 0.5):
			print("时间太短了，重新输入")
			exit()
		else:
			print("这个时间刚刚好")
			
	def setup(self,pin):
		#初始化GPIO口
		#采用BCM编号
		GPIO.setmode(GPIO.BCM)
		#设置GPIO为输出状态，输入低电平
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,GPIO.LOW)

	def loop(self,pin,up_time,down_time):
		while True:
			#循环点亮
			GPIO.output(pin,GPIO.HIGH)
			print("light up")
			time.sleep(up_time)
			
			GPIO.output(pin,GPIO.LOW)
			print("light down")
			time.sleep(down_time)

	def destroy(self,pin):
		#恢复GPIO口状态
		GPIO.output(pin,GPIO.LOW)
		GPIO.setup(pin,GPIO.IN)

if __name__ == '__main__':
	light = Light()
