#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is optimized for python2.7

from pygeocoder import Geocoder
from geopy.geocoders import Nominatim
def search_business(business_name):
    results = Geocoder.geocode(business_name)
    # for result in results:
    print results[0]
def searchBygeopy():
    geolocator = Nominatim()
    location = geolocator.geocode("Tian'anmen, Beijing")
    print location.address

if __name__ == '__main__':
    business_name = "Tian'anmen, Beijing"
    print "Searching %s" % business_name
    # search_business(business_name)
    searchBygeopy()
