#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author  :hstking
#E-mail  :hstking@hotmail.com
#Ctime   :2015/08/07
#Mtime   :
#Version :

import RPi.GPIO as GPIO
import time
import sys

#BCM GPIO编号
pins = [5,6,12,13,16,17,18,19,20,21,22,23,24.25,26,27]

def setup(pin):
	#采用BCM编号
	GPIO.setmode(GPIO.BCM)
	#设置GPIO为输出状态，且输出低电平
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.LOW)

def loop(pin):
	while True:
		#循环点亮
		GPIO.output(pin,GPIO.HIGH)
		print("light up")
		time.sleep(0.5)
		GPIO.output(pin,GPIO.LOW)
		print("light down")
		time.sleep(0.5)

def destroy(pin):
	for pinNu in pins:
		GPIO.output(pin,GPIO.LOW)
		GPIO.setup(pin,GPIO.IN)


def tip():
	print("usage: light 可使用的pin脚编号")
	print("只需要一个参数，必须是可用的pin脚编号")
	print("只能用以下的几个编号，请对照输入")
	for i in pins:
		print i,
	exit()
	
def check_parameter():
	if pin in pins:
		print("输入的pin编码符合要求")
		print("pin = %d"%pin)
		return		
	else:
		print("输入的pin编号不符合要求，只能用以下的几个编号，请对照输入")
		for i in pins:
			print i,
		exit()

if __name__ == '__main__':
	argc = len(sys.argv) - 1
	try:
		pin = int(sys.argv[1])
	except IndexError:
		tip()
	except ValueError:
		print("只能输入有效的pin编号")
		for i in pins:
			print i,
		exit()

	if argc > 1:
		tip()
	else:
		check_parameter()
	#初始化GPIO
	setup(pin)
	try:
		loop(pin)
	except KeyboardInterrupt:
		#恢复GPIO口状态
		destroy(pin)
