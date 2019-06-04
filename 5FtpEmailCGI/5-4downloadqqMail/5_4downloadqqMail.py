# encoding: utf-8
# This program is optimized for python2.7
import argparse
import getpass
import poplib

QQ_POP3_SERVER = 'pop.qq.com'
PASSWORD = 'ezfhzbvetsbqbhhi'
def down_load_email(usernamed):
    mailbox = poplib.POP3_SSL(QQ_POP3_SERVER)
    mailbox.user(usernamed)
    # password = getpass.getpass(prompt="Enter your QQ password:")
    password = PASSWORD
    mailbox.pass_(password)
    num_message = len(mailbox.list()[1])
    print "Total emails: %s" % num_message
    print "Getting last message"
    for msg in mailbox.retr(num_message)[1]:
        print msg
    mailbox.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'Email Download Example')
    parser.add_argument('--username', action="store", dest="username",
                        default= getpass.getuser())
    given_args = parser.parse_args()
    username = given_args.username
    down_load_email(username)
