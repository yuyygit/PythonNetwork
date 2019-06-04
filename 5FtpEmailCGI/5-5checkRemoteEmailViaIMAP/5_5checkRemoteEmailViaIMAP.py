# encoding: utf-8
# This program is optimized for python2.7
import argparse
import getpass
import imaplib
import email

QQ_IMAP_SERVER = 'imap.qq.com'
PASSWORD = 'ezfhzbvetsbqbhhi'

def check_email(username):
    mailbox = imaplib.IMAP4_SSL(QQ_IMAP_SERVER,993)
    # password = getpass.getpass(prompt= "Enter your qq email password:")
    password = PASSWORD
    mailbox.login(username,password)
    mailbox.select('Inbox')
    typ, data = mailbox.search(None, 'ALL')
    # for num in data[0].split():
    msglist = data[0].split()
    num = msglist[len(msglist) - 1]
    typ, data = mailbox.fetch(num, '(RFC822)')
    # typ, data = mailbox.fetch(num, '(RFC822.SIZE BODY[HEADER.FIELDS (SUBJECT)])')

    msg = email.message_from_string(data[0][1])
    # content = msg.get_payload(decode=True)
    print 'Message %s \n%s\n' % (num, msg)
    print '*' * 40
    # print content
    # break
    mailbox.close()
    mailbox.logout()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Email Download Example')
    parser.add_argument('--username', action="store", dest= "username",
                        default=getpass.getuser())
    given_args = parser.parse_args()
    username = given_args.username
    check_email(username)