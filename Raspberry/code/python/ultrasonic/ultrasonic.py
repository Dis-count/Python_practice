#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author  :hstking
#E-mail  :hstking@hotmail.com
#Ctime   :2015/08/30
#Mtime   :
#Version :

import RPi.GPIO as GPIO
import time


####  定义类Ultrasonic
class Ultrasonic(object):
####  类Ultrasonic的构造函数
	def __init__(self,trig_pin,echo_pin):
		self.trig_pin = trig_pin
		self.echo_pin = echo_pin
		self.pins = [5,6,12,13,16,17,18,19,20,21,22,23,24,25,26,27]
		self.check_pin(self.trig_pin,self.echo_pin)
		self.run(self.trig_pin,self.echo_pin)

####  check_pin函数检测输入的端口是否可用
	def check_pin(self,trig_pin,echo_pin):
		if trig_pin in self.pins:
			print("%d 是有效编号"%trig_pin)
		else:
			print("只能输入以下有效的pin编号")
			for i in self.pins:
				print i,
			exit()
		if echo_pin in self.pins:
			print("%d 是有效编号"%echo_pin)
		else:
			print("只能输入以下有效的pin编号")
			for i in self.pins:
				print i,
			exit()

####  setup函数初始化GPIO口
	def setup(self,trig_pin,echo_pin):
		#采用BCM编号
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		#设置GPIO为输出状态，输入低电平
		GPIO.setup(self.trig_pin,GPIO.OUT,initial=GPIO.LOW)
		GPIO.setup(self.echo_pin,GPIO.IN)

####  run函数测距
	def run(self,trig_pin,echo_pin):
		self.setup(self.trig_pin,self.echo_pin)
		#发出触发信号
		GPIO.output(self.trig_pin,GPIO.HIGH)
		#保持10us以上
		time.sleep(0.000015)
		GPIO.output(self.trig_pin,GPIO.LOW)
		while not GPIO.input(self.echo_pin):
			pass
		#echo端口发现高电平，开始计时
		t1 = time.time()
		while GPIO.input(self.echo_pin):
			pass
		#echo端口高电平停止，结束计时
		t2 = time.time()
		length = (t2-t1)*340/2
		print("测试距离为 %0.2f m"%length)
		return length


if __name__ == '__main__':
	ul = Ultrasonic(23,24)
