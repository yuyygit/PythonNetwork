# encoding: utf-8
# This program is optimized for python2.7
import ftplib

FTP_SERVER_URL = 'ftp.sjtu.edu.cn'

def test_ftp_connection(path, username, email):
    #Open ftp connection
    ftp = ftplib.FTP(path, username, email)

    #List the files in the /pub directory
    ftp.cwd("/pub")
    print "File list at %s: " % path
    files = ftp.dir()
    print files

    ftp.quit()

if __name__ == '__main__':
    test_ftp_connection(path= FTP_SERVER_URL, username='anonymous', email= 'nobody@nourl.com')