#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author  :hstking
#E-mail  :hstking@hotmail.com
#Ctime   :2015/08/07
#Mtime   :
#Version :

import RPi.GPIO as GPIO
import time

#BCM GPIO编号
pins = [4,17,26,12,16,18,23,24,25]

def setup():
	#采用BCM编号
	GPIO.setmode(GPIO.BCM)
	#设置所有GPIO为输出状态，且输出低电平
	for pin in pins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,GPIO.LOW)

def loop():
	while True:
		#循环点亮
		for pin in pins:
			GPIO.output(pin,GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(pin,GPIO.LOW)
			time.sleep(0.5)

def destroy():
	for pin in pins:
		GPIO.output(pin,GPIO.LOW)
		GPIO.setup(pin,GPIO.IN)


if __name__ == '__main__':
	#初始化GPIO
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		#恢复GPIO口状态
		destroy()
