# encoding: utf-8
# This program is optimized for python2.7

import urllib2

BROWSER = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
URL = 'http://www.python.org'

def spoot_IE():
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', BROWSER)]
    result = opener.open(URL)
    print "Reponse headers:"
    for header in result.headers.headers:
        print "\t", header

if __name__ == '__main__':
    spoot_IE()