#!/usr/bin/pyhton
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "localhost"
content = "Hello email!"

msg = MIMEText(content, 'plain', 'utf-8')

msg['From'] = Header("Masako", 'utf-8')
msg['To'] = Header("cnblog",'utf-8')
msg['Subject'] = Header("Email greetings", 'utf-8')

sender = 'masako@cnblgs.com'
receivers = ['361719439@qq.com']

try:
    smtObj =  smtplib.SMTP()
    smtObj.connect(mail_host, 25)
    smtObj.sendmail(sender, receivers, msg.as_string())
    print "sucess"
except smtplib.SMTPException:
    print "failed"
