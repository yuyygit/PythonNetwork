#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is optimized for python2.7

#
# from geopy.geocoders import Baidu
# geocoder = Baidu(
#     api_key='ulpZxZGU4e4NMw2b0lwFHLYklV1YiOfw',
#     security_key='msigW7T7wfdvFv3iQ16axF0Gwkr3pLLy',
#     timeout=200
# )
# lr=[]
# ilb=[('a',39.8694900405,116.0013866959),('b',39.8694900405,116.0013866959)]
# for _,i in enumerate(ilb):
#     # location = geocoder.reverse(i[1]+','+i[2])
#     location = geocoder.reverse(i[1]+i[2])
#     lr.append((i[0],location.raw))
# for _,i in enumerate(lr):
#     addr = i[1]['addressComponent']
#     addr['country']
#     print(addr)
#     if _ > 1:
#         from geopy.geocoders import Baidu
#
#         geocoder = Baidu(
#             api_key='ak',  # 自己修改
#             security_key='sk',  # 自己修改
#             timeout=200
#         )
#         lr = []
#         ilb = [('a', 39.8694900405, 116.0013866959), ('b', 39.8694900405, 116.0013866959)]
#         for _, i in enumerate(ilb):
#             location = geocoder.reverse(i[1] + ',' + i[2])
#             lr.append((i[0], location.raw))
#         for _, i in enumerate(lr):
#             addr = i[1]['addressComponent']
#             addr['country']
#             print(addr)
#             #     print(i)
#             if _ > 1:
#                 break
#         from geopy.geocoders import Baidu
#
#         geocoder = Baidu(
#             api_key='ak',  # 自己修改
#             security_key='sk',  # 自己修改
#             timeout=200
#         )
#         lr = []
#         ilb = [('a', 39.8694900405, 116.0013866959), ('b', 39.8694900405, 116.0013866959)]
#         for _, i in enumerate(ilb):
#             location = geocoder.reverse(i[1] + ',' + i[2])
#             lr.append((i[0], location.raw))
#         for _, i in enumerate(lr):
#             addr = i[1]['addressComponent']
#             addr['country']
#             print(addr)
#             #     print(i)
#             if _ > 1:
#                 break
#         breakfrom geopy.geocoders import Baidu
# geocoder = Baidu(
#             api_key='ulpZxZGU4e4NMw2b0lwFHLYklV1YiOfw',#自己修改
#             security_key='msigW7T7wfdvFv3iQ16axF0Gwkr3pLLy',#自己修改
#             timeout=200
#         )
# lr=[]
# ilb=[('a',39.8694900405,116.0013866959),('b',39.8694900405,116.0013866959)]
# for _,i in enumerate(ilb):
#     location= geocoder.reverse(i[1]+','+i[2])
#     lr.append((i[0],location.raw))
# for _,i in enumerate(lr):
#     addr=i[1]['addressComponent']
#     addr['country']
#     print(addr)
# 	#     print(i)
#     if _>1:
#         break



# import json
# # import urllib
# from urllib2 import urlopen, quote
# import csv
# import requests
# def getlnglat(address):
#     url = 'http://api.map.baidu.com/geocoder/v2/'
#     output = 'json'
#     ak = 'ulpZxZGU4e4NMw2b0lwFHLYklV1YiOfw'
#     add = quote(address) #由于本文地址变量为中文，为防止乱码，先用quote进行编码
#     uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
#     req = urlopen(uri)
#     res = req.read().decode('utf-8')
#     temp = json.loads(res)
#
#     # print(temp.keys())
#     # print(temp.values())
#     # print(type(temp['result']))
#
#
#     if temp['status'] == 0 :
#         lng = temp['result']['location']['lng']  # 纬度
#         lat = (temp['result']['location']['lat'])  # 经度
#         print(lat, lng)
#
#
#
#     else:
#         print(address+"没找到")
#     #
#     # with open('D:\pycharm\\test_python_csv\\island\\test111.csv', 'w+', newline='') as csvfile:
#     #     writer = csv.writer(csvfile)
#     #     try:
#     #         if temp['status'] == 0:
#     #             lng = temp['result']['location']['lng']  # 纬度
#     #             lat = (temp['result']['location']['lat'])  # 经度
#     #             writer.writerow([address, lat, lng])
#     #             print(00)
#     #         # else:
#     #         #     writer.writerow([address])
#     #         #     print(11)
#     #     except:
#     #         print(22)
#     #         writer.writerow([address])
#
#
# getlnglat('北京')
import requests
import json
import pprint

ak = 'm9umAdjKIi7WQdQ54DYR8N3yuIRB5YZ1'  # ak需要去百度地图申请
address = raw_input('请输入想要查询的地址')

url = 'http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak={}'.format(address, ak)
res = requests.get(url)
json_data = json.loads(res.text)
pprint.pprint(json_data)  # 美观打印数据结构
lat = json_data['result']['location']['lat']  # 经度
lng = json_data['result']['location']['lng']  # 纬度
print(lat, lng)

