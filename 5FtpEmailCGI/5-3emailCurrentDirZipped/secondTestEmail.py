# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_user = '361719439@qq.com'
mail_pass = 'gckqrcukttzgbhga'

def send(content, receivers, sender, receiver):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = Header(sender, 'utf-8')
    msg['To'] = Header(receiver, 'utf-8')
    msg['Subject']  = Header("Download Test", 'utf-8')

    try:
        smtp_obj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(mail_user, receivers, msg.as_string())
        print "sucess"
        result = True
    except smtplib.SMTPException as e:
        result = False
        print "failed"
    return result

if __name__ == '__main__':
    send("20190531--hello download", '1307271447@qq.com',"789","012")
