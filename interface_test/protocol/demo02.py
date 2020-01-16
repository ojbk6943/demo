#!/usr/bin/env python
#-*- coding:utf-8 -*-

import http.client

if __name__ == '__main__':

    conn = http.client.HTTPConnection('192.168.2.17',8080)
    login_data = 'username=admin&password=admin&verifycode=0000'
    header = {"Content-Type":"application/x-www-form-urlencoded"}
    conn.request('POST','/WoniuSales/user/login',body=login_data,headers=header)
    resp = conn.getresponse()
    print(resp.read().decode())
