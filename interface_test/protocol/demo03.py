#!/usr/bin/env python
#-*- coding:utf-8 -*-

import http.client

if __name__ == '__main__':
    conn = http.client.HTTPConnection('192.168.2.17', 8080)
    customer_data = 'customername=未和&customerphone=4564335213&childsex=男&childdate=2019-11-06&creditkids=0&creditcloth=0'
    header = {"Content-Type": "application/x-www-form-urlencoded",
              "Cookie":" JSESSIONID=C37F88E9CFFA32F16BD5472F21A9D649;"
                       " _jfinal_captcha=60a3224492164b19b1fcc52526d81789;"
                       " username=admin; password=admin"}
    conn.request('POST', '/WoniuSales/customer/add', body=customer_data.encode('utf-8'), headers=header)
    resp = conn.getresponse()
    # print(resp.read().decode())
    print( resp.getheaders())