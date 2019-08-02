#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# This program is optimized for python2.7
import urllib
import hashlib

ak = 'ulpZxZGU4e4NMw2b0lwFHLYklV1YiOfw'
sk = 'msigW7T7wfdvFv3iQ16axF0Gwkr3pLLy'

# 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
queryStr = '/geocoder/v2/?address=北京&output=json&ak=' + ak

# 对queryStr进行转码，safe内的保留字符不转换
encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

# 在最后直接追加上yoursk
rawStr = encodedStr + sk

# md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
# 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
print hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()

address = "北京"
url = 'http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak={}'.format(address, ak)
queryStr2 = url[24:]
encodedStr2 = urllib.quote(queryStr2, safe="/:=&?#+!$,;'@()*[]")
rawStr2 = encodedStr2 + sk
sn = hashlib.md5(urllib.quote_plus(rawStr2)).hexdigest()
print sn
