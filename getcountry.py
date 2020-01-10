#!/usr/bin/env  python3

import requests
import re
import sys

def country(host,*,key='none'):
    if key == 'none':
        print ('Pass valid api key to use the module')
        sys.exit(1)
    if  not re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",host):
        print("Invalid IP Format")
        sys.exit(1)

    url = 'http://api.ipstack.com/{}?access_key={}'.format(host,key)
    country = requests.get(url).json()['country_name']
    return country
