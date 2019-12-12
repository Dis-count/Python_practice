#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author  :hstking
#E-mail  :hstking@hotmail.com
#Ctime   :2015/09/11
#Mtime   :
#Version :

import smtplib
import email.utils
from email.mime.text import MIMEText
import getNip


class SendMail(object):
	def __init__(self,subject,content):
		self.subject = subject
		self.content = content
		self.mailList = ['139******7@139.com','33*****@qq.com']
		self.fromMail = 'hst*****@163.com'
		self.mi = {'user':'hst****','password':'*********'}

		self.sendMail(self.subject,self.content)

	def sendMail(self,subject,content):
		for mL in self.mailList:
			msg = MIMEText(content)
			msg['To'] = email.utils.formataddr((mL[:mL.index('@')],mL))
			msg['From'] = email.utils.formataddr((self.fromMail[:self.fromMail.index('@')],self.fromMail))
			msg['Subject'] = subject
			try:
				s = smtplib.SMTP()
				s.set_debuglevel(1)
				s.connect('smtp.' + self.fromMail[self.fromMail.index('@') + 1:])
				s.login(self.mi['user'],self.mi['password'])
				s.sendmail(self.fromMail,mL,msg.as_string())
			except EOFError,e:
				print str(e)
			finally:
				s.quit


class SendMsg(object):
	def __init__(self):
		nipFile = '/home/pi/log/Nip.txt'
		with open(nipFile,'r') as fp:
			self.nip = fp.read()
		Nip = getNip.GetNip()
		if 	self.nip == Nip.Nip:
			pass
		else:
			sMsg = SendMail('IP',self.nip)


if __name__ == '__main__':
	SMSG = SendMsg()
