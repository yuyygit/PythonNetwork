# encoding: utf-8
# This program is optimized for python2.7
import requests
import urllib
import urllib2

ID_USERNAME = 'LoginNam'
ID_EMAIL = 'LoginName'
ID_PASSWORD = 'Password'

EMAIL = 'you＠@email.com'
USERNAME = 'ew233'
PASSWORD = '2925909647yu.'
SINGUP_URL = 'https://account.cnblogs.com/signin?returnUrl=https%3a%2f%2fwww.cnblogs.com%2f'
ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

def submit_form():
    """ Submit a form"""
    payload = {ID_USERNAME : USERNAME,
               ID_PASSWORD : PASSWORD}

    #make a request
    resp = requests.get(SINGUP_URL, headers= ua_header)
    print "Response to GET request: %s" % resp.content
    print "*" * 40
    #send a POST request
    resp = requests.post(SINGUP_URL, payload,headers= ua_header)
    print "Headers from a POST request response: %s" % resp.headers
    print "Response to POST request: %s" % resp.content

if __name__ == '__main__':
    submit_form()