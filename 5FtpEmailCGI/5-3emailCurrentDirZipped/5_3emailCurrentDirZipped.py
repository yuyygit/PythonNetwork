# encoding: utf-8
# This program is optimized for python2.7
import os
import argparse
import smtplib
import zipfile
import tempfile
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_user = '361719439@qq.com'
mail_pass = 'gckqrcukttzgbhga'
receivers = ['1307271447@qq.com']
def email_dir_zipped(sender, recipient):
    zf = tempfile.TemporaryFile(prefix= 'mail', suffix= '.zip')
    zip = zipfile.ZipFile(zf, 'w')
    print "Zipping current dir: %s" % os.getcwd()
    for file_name in os.listdir(os.getcwd()):
        zip.write(file_name)
    zip.close()
    zf.seek(0)

    #Create the message
    print "Creating email message..."
    email_msg = MIMEMultipart()
    email_msg['Subject'] = Header('File from path %s ' % os.getcwd(), 'utf-8')
    email_msg['To'] = ', '.join(recipient)
    email_msg['From'] = sender
    email_msg.preamble = "Testing email from Python. \n"
    msg = MIMEBase('application', 'zip')
    msg.set_payload(zf.read())
    encoders.encode_base64(msg)
    msg.add_header('Content-Disposition', 'attachment',
                   filename=os.getcwd()[-1] + '.zip')
    email_msg.attach(msg)
    email_msg = email_msg.as_string()

    #send the message
    print "Sending email message..."
    try:
        # smtp = smtplib.SMTP('localhost')
        smtp_obj = smtplib.SMTP_SSL("smtp.qq.com", 465)

        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(mail_user, receivers, msg.as_string())
        # smtp.set_debuglevel(1)
        # smtp.sendmail(sender, recipient, email_msg)
    except Exception as e:
        print "Error: %s" % str(e)
    finally:
        smtp_obj.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'Email Example')
    parser.add_argument('--sender', action="store", dest= 'sender',
                        default="yy@yy.com")
    parser.add_argument('--recipient', action="store", dest="recipient")
    given_args = parser.parse_args()
    email_dir_zipped(given_args.sender, given_args.recipient)

