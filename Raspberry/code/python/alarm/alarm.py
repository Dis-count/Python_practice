#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author  :hstking
#E-mail  :hstking@hotmail.com
#Ctime   :2015/09/15
#Mtime   :
#Version :

import RPi.GPIO as GPIO
import time
import sys
import string
mylogPath = '/home/pi/code/python/mylog'
if not mylogPath in sys.path:
	sys.path.append(mylogPath)
import mylog
####  mylog模块是通过mylog目录下的__init__.py将目录模块化后导入的
import sendMsg
####  sendMsg模块是将sendMsg.py直接拷贝到本地文件夹下直接导入的


####  定义Bell类
class Bell(object):
####  Bell类的构造函数
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

####  检查输入的端口是否合法
	def check_pin(self,pin):
		if pin in self.pins:
			print("%d 是有效编号"%pin)
		else:
			print("只能输入以下有效的pin编号")
			for i in self.pins:
				print i,
			exit()


####  初始化GPIO口
	def setup(self,pin):
		#采用BCM编号
		GPIO.setmode(GPIO.BCM)
		#设置GPIO为输出状态，输入低电平
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,GPIO.LOW)

	def loop(self,pin):
		for i in xrange(1,10):
			GPIO.output(pin,GPIO.HIGH)
			print("bell up")
			time.sleep(self.up_time)
			GPIO.output(pin,GPIO.LOW)
			print("bell down")
			time.sleep(self.down_time)

	def destroy(self,pin):
####  恢复GPIO口状态
		GPIO.output(pin,GPIO.LOW)
		GPIO.setup(pin,GPIO.IN)

####  定义了Light类
class Light(object):
####  Light类的构造函数
	def __init__(self,pin):
		self.pin = pin
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

	def check_pin(self,pin):
		if pin in self.pins:
			print("%d 是有效编号"%pin)
		else:
			print("只能输入以下有效的pin编号")
			for i in self.pins:
				print i,
			exit()


####  初始化GPIO口
	def setup(self,pin):
####  采用BCM编号
		GPIO.setmode(GPIO.BCM)
####  设置GPIO为输出状态，输入低电平
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,GPIO.LOW)

	def loop(self,pin):
		for i in xrange(1,10):
			GPIO.output(pin,GPIO.HIGH)
			print("light up")
			time.sleep(self.up_time)
			GPIO.output(pin,GPIO.LOW)
			print("light down")
			time.sleep(self.down_time)

	def destroy(self,pin):
####  恢复GPIO口状态
		GPIO.output(pin,GPIO.LOW)
		GPIO.setup(pin,GPIO.IN)

####  定义Ultrasonic类
class Ultrasonic(object):
	def __init__(self,trig_pin,echo_pin):
		self.trig_pin = trig_pin
		self.echo_pin = echo_pin
		self.pins = [5,6,12,13,16,17,18,19,20,21,22,23,24,25,26,27]
		self.check_pin(self.trig_pin,self.echo_pin)
		self.run(self.trig_pin,self.echo_pin)

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


####  初始化GPIO口
	def setup(self,trig_pin,echo_pin):
####  采用BCM编号
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
####  设置GPIO为输出状态，输入低电平
		GPIO.setup(self.trig_pin,GPIO.OUT,initial=GPIO.LOW)
		GPIO.setup(self.echo_pin,GPIO.IN)

	def run(self,trig_pin,echo_pin):
		self.setup(self.trig_pin,self.echo_pin)
####  发出触发信号
		GPIO.output(self.trig_pin,GPIO.HIGH)
####  保持15us
		time.sleep(0.000015)
		GPIO.output(self.trig_pin,GPIO.LOW)
		while not GPIO.input(self.echo_pin):
			pass
####  echo端口发现高电平，开始计时
		t1 = time.time()
		while GPIO.input(self.echo_pin):
			pass
####  echo端口高电平停止，结束计时
		t2 = time.time()
		length = (t2-t1)*340/2
		print("测试距离为 %0.2f m"%length)
		return length

####  定义Alarm类
class Alarm(object):
	def __init__(self):
		self.ptime = 5
		self.tolerance = 0.05
		self.mlog = mylog.MyLog()
		self.run()

####  通过超生波模块2次测距，如果测距的距离在可容忍的误差内则Pass
####  如果明显测距距离不一样，则说明门被打开,点亮报警灯，打开蜂鸣器报警
	def run(self):
		while True:
			ul = Ultrasonic(23,24)
			len1 = ul.run(23,24)
			time.sleep(self.ptime)
			len2 = ul.run(23,24)
			if len1 > (len2 - 0.5) or len1 < (len2 + 0.5) :
				self.mlog.info("初始位置 %f" %len1)
				self.mlog.info("目前位置 %f" %len2)
				self.echo()
			else:
				pass

	def echo(self):
####  点亮报警灯
		light = Light(12)
####  打开报警器
		bell = Bell(18)
####  发送短信到手机
		sendM = sendMsg.SendMail('警告','门已开')

if __name__ == '__main__':
	al = Alarm()
