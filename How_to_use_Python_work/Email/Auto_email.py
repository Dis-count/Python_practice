# 导入我们需要用到的包

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib

msg = MIMEMultipart()

# 在邮件中插入正文：

##在邮件中插入文本信息
df_text='''<html>
                  <body>
                  <p>   Hi all ，</p>
                  <p>   这是一个测试邮件，详情请参考附件 </p>
                  <p>   情况如下图： </p>
                 </body></html>'''
msgtext = MIMEText(df_text, 'html', 'utf-8')
msg.attach(msgtext)

#如果你需要插入图片，利用同样的方法，在邮件中插入图片：

##在邮件中插入图片信息
image = open('temp.jpg','rb')
msgimage = MIMEImage(image.read())
msg.attach(msgimage)


##在邮件添加附件:

msgfile = MIMEText(open('temp.xlsx', 'rb').read(), 'base64', 'utf-8')
msgfile["Content-Disposition"] = 'attachment; filename="temp.xlsx"'
msg.attach(msgfile)

#剩下的就是设置一些邮件参数来发送邮件：

#设置邮件信息常量
email_host= ''  # 服务器地址
sender = '' # 发件人
password ='' # 密码，如果是授权码就填授权码
receiver = '' # 收件人

# 发送邮件：

try:
    smtp = smtplib.SMTP(host=email_host)
    smtp.connect(email_host)
    smtp.starttls()
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver.split(',') , msg.as_string())
    smtp.quit()
    print('发送成功')
except Exception:
     print('发送失败')
