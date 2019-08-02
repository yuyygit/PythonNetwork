#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is optimized for python2.7

import requests
import json
import pprint
import urllib
import hashlib
ak = 'ulpZxZGU4e4NMw2b0lwFHLYklV1YiOfw'
sk = 'msigW7T7wfdvFv3iQ16axF0Gwkr3pLLy'

address = raw_input('请输入想要查询的地址')
# address = "北京"

url = 'http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak={}'.format(address, ak)

queryStr = url[24:]
encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
rawStr = encodedStr + sk
sn = hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()
print (sn)
url += '&sn=' + sn
res = requests.get(url)
json_data = json.loads(res.text)
pprint.pprint(json_data)  # 美观打印数据结构
lat = json_data['result']['location']['lat']  # 经度
lng = json_data['result']['location']['lng']  # 纬度
print(lat, lng)


