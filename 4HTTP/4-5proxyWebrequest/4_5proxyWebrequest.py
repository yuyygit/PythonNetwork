# encoding: utf-8
# This program is optimized for python2.7
import urllib

URL = 'http://www.baidu.com/'
PROXY_ADDRESS = '112.85.131.247:9999'
#By Googling free proxy server

if __name__ == '__main__':
    resp = urllib.urlopen(URL, proxies= {'https' : PROXY_ADDRESS})
    print "Proxy server returns response headers: %s" % resp.headers

    print "**" * 40
    print "Proxy server returns content: %s" % resp.read()
