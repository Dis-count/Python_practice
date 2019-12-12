#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author  :hstking
#E-mail  :hstking@hotmail.com
#Ctime   :2015/09/09
#Mtime   :
#Version :

import logging
import os
import telnetlib
import urllib2
import re
import time


####  定义GetNip类
class GetNip():
####  GetNip类的构造函数
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
			print("Nip = %s" %self.Nip)
		else:
			print("未取得本机NIP")

####  将取得的公网IP写入文件
	def writeNip(self):
		if os.path.isdir(self.logPath):
			pass
		else:
			os.makedirs(self.logPath)
		with open(self.nipFile,'w') as FP:
			FP.write(self.Nip)


####  定义PortMap类
class PortMap(object):
####  PortMap类的构造函数
	def __init__(self):
		self.tn = None
		self.gn = GetNip()
		self.nip = self.gn.Nip
		self.ml = MyLog()
####  定义本地的环境变量
		self.dict1 = {
				'modemIp':'192.168.1.1',
				'mapIp':'192.168.1.90',
				'user':b'root',
				'password':b'root',
				'finish':b'/ # '}
####  iptables命令列表，清除iptables环境，以便于而后的设置
		self.portmap_clear = [
				'iptables -t nat -F myPREROUTING',
				'iptables -t nat -D PREROUTING -j myPREROUTING',
				'iptables -t nat -X myPREROUTING',
				'iptables -t nat -F myPREROUTING',
				'iptables -t nat -F myPOSTROUTING',
				'iptables -t nat -D POSTROUTING -j myPOSTROUTING',
				'iptables -t nat -X myPOSTROUTING']
####  iptables命令列表，设置iptables，将Route上的8080端口映射到Modem的8080端口上
		self.portmap_set = [
				'iptables -t nat -N myPREROUTING',
				'iptables -t nat -A myPREROUTING -d ' + self.nip + ' -p tcp -m tcp --dport 8080 -j DNAT --to-destination ' + self.dict1['mapIp'] + ':8080',
				'iptables -t nat -A PREROUTING -j myPREROUTING',
				'iptables -t nat -N myPOSTROUTING',
				'iptables -t nat -A myPOSTROUTING -d ' + self.dict1['mapIp'] + ' -p tcp -m tcp --dport 8080 -j SNAT --to-source ' + self.dict1['modemIp'],
				'iptables -t nat -A POSTROUTING -j myPOSTROUTING']
		self.set_iptables()

####  该函数用于设置iptables
	def set_iptables(self):
		self.ml.info(u'开始设置 iptables ......')
		self.conn_telnet()
		cmd = None
		for cmd in self.portmap_clear:
			self.tn.write('%s \n' %cmd)
			self.ml.info('Run command : "%s" successfull' %cmd)
			time.sleep(2)
		self.ml.info(u'iptables 清除完毕')
		cmd = None
		for cmd in self.portmap_set:
			self.tn.write('%s \n' %cmd)
			self.ml.info('Run command : "%s" successfull' %cmd)
			time.sleep(2)
		self.ml.info(u'iptables 设置完毕 ......')
		self.disconn_telnet()

####  该函数用于连接Modem上的telnet服务
	def conn_telnet(self):
		self.tn = telnetlib.Telnet(self.dict1['modemIp'])
		self.tn.read_until(b'Login: ')
		self.tn.write(self.dict1['user'] + b'\n')
		self.tn.read_until(b'Password: ')
		self.tn.write(self.dict1['password'] + b'\n')
		self.tn.read_until(self.dict1['finish'])
		self.ml.info(u"telnet 连接成功")

####  该函数用于断开Modem上的telnet服务
	def disconn_telnet(self):
		self.tn.close()
		self.ml.info(u"telnet 断开")


####  定义一个MyLog类
class MyLog(object):
	def __init__(self):
		self.logger = logging.getLogger('pi')
		self.logFile = '/home/pi/log/' + os.path.basename(__file__)[0:-3] + '.log'
		self.logger.setLevel(logging.DEBUG)
		self.formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

		self.logHand = logging.FileHandler(self.logFile)
		self.logHand.setLevel(logging.DEBUG)
		self.logHand.setFormatter(self.formatter)

		self.logHandSt = logging.StreamHandler()
		self.logHandSt.setLevel(logging.DEBUG)
		self.logHandSt.setFormatter(self.formatter)
		

		self.logger.addHandler(self.logHand)
		self.logger.addHandler(self.logHandSt)

####  这里只定义了一个info，实际上还可以有bug,error……
	def info(self,msg):
		self.logger.info(msg)


if __name__ == '__main__':
	portMap = PortMap()
