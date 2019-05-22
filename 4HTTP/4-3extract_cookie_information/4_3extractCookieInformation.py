# encoding: utf-8
# This program is optimized for python2.7
import cookielib
import urllib
import urllib2
from urllib2_modify import urllib2_modify


ID_USERNAME = 'id_username'
ID_PASSWORD = 'id_password'
USERNAME = 'you@email.com'
PASSWORD = 'mypassword'
LOGIN_URL = 'https://bitbucket.org/account/signin/?next=/'
NORMAL_URL = 'https://bitbucket.org/'
BAIDU_URL = 'https://www.baidu.com/'
BAIDUBAR_URL = 'https://tieba.baidu.com/index.html?traceid='
ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
ua_header2 = [("User-agent" , "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;")]

def extract_cookie_info():
    """ Fake login to a site with cookie"""
    #setup cookie jar
    cj = cookielib.CookieJar()
    login_data = urllib.urlencode({ID_USERNAME : USERNAME,
                                   ID_PASSWORD : PASSWORD})
    # create url opener
    # opener = urllib2_modify.build_opener(ua_header,urllib2_modify.HTTPCookieProcessor(cj))
    opener = urllib2_modify.build_opener(ua_header2, urllib2_modify.HTTPCookieProcessor(cj))
    # resp = opener.open(LOGIN_URL, login_data)
    #send login info
    # for cookie in cj:
    #     print "----First time cookie: %s --> %s" % (cookie.name, cookie.value)
    #
    # print "Headers: %s" % resp.headers

    #now access without any login info
    # resp = opener.open(NORMAL_URL)
    resp = opener.open(BAIDUBAR_URL)
    for cookie in cj:
        print "++++Second time cookie: %s --> %s" % (cookie.name, cookie.value)

    print "Headers: %s" % resp.headers

if __name__ == '__main__':
    extract_cookie_info()
