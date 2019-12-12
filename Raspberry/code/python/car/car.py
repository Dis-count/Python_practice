#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author  :hstking
#E-mail  :hstking@hotmail.com
#Ctime   :2015/09/21
#Mtime   :
#Version :


import RPi.GPIO as GPIO
import time
import sys


####  定义Car类
class Car(object):
	def __init__(self):
		self.enab_pin = [5,6,13,19]
####  self.enab_pin是使能端的pin
		self.inx_pin = [21,22,23,24]
####  self.inx_pin是控制端in的pin
		self.RightAhead_pin = self.inx_pin[0]
		self.RightBack_pin = self.inx_pin[1]
		self.LeftAhead_pin = self.inx_pin[2]
		self.LeftBack_pin = self.inx_pin[3]
####  分别是右轮前进，右轮退后，左轮前进，左轮退后的pin
		self.setup()

####  setup函数初始化端口
	def setup(self):
		print "begin setup ena enb pin"
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		for pin in self.enab_pin: 
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin,GPIO.HIGH)
####  初始化使能端pin，设置成高电平
		pin = None
		for pin in self.inx_pin:
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin,GPIO.LOW)
####  初始化控制端pin，设置成低电平
		print "setup ena enb pin over"

####  fornt函数，小车前进
	def front(self):
		self.setup()
		GPIO.output(self.RightAhead_pin,GPIO.HIGH)
		GPIO.output(self.LeftAhead_pin,GPIO.HIGH)

####  leftFront函数，小车左拐弯
	def leftFront(self):
		self.setup()
		GPIO.output(self.RightAhead_pin,GPIO.HIGH)

####  rightFront函数，小车右拐弯
	def rightFront(self):
		self.setup()
		GPIO.output(self.LeftAhead_pin,GPIO.HIGH)

####  rear函数，小车后退
	def rear(self):
		self.setup()
		GPIO.output(self.RightBack_pin,GPIO.HIGH)
		GPIO.output(self.LeftBack_pin,GPIO.HIGH)

####  leftRear函数，小车左退
	def leftRear(self):
		self.setup()
		GPIO.output(self.RightBack_pin,GPIO.HIGH)

####  rightRear函数，小车右退
	def rightRear(self):
		self.setup()
		GPIO.output(self.LeftBack_pin,GPIO.HIGH)

####  定义main主函数
def main(status):
	car = Car()
	if status == "front":
		car.front()
	elif status == "leftFront":
		car.leftFront()
	elif status == "rightFront":
		car.rightFront()
	elif status == "rear":
		car.rear()
	elif status == "leftRear":
		car.leftRear()
	elif status == "rightRear":
		car.rightRear()
	elif status == "stop":
		car.setup()
			

if __name__ == '__main__':
	main(sys.argv[1])
