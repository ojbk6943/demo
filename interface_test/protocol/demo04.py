#!/usr/bin/env python
#-*- coding:utf-8 -*-

import http.client

class WoniuSalesTest:

    def __init__(self):

        self.host = '192.168.2.17'
        self.port = 8080
        self.conn = http.client.HTTPConnection(self.host, self.port)
        self.cookie = ''

    def login(self):
        self.conn = http.client.HTTPConnection(self.host, self.port)
        login_data = 'username=admin&password=admin&verifycode=0000'
        header = {"Content-Type":"application/x-www-form-urlencoded"}
        login_url = '/WoniuSales/user/login/'

        self.conn.request('POST',login_url,login_data,header)
        resp = self.conn.getresponse()
        data = resp.getheaders()
        print(data)
        for info in data:
            if info[0] == 'Set-Cookie' :
                self.cookie += info[1].split(';')[0]+';'

        print(self.cookie)

    def add_customer(self):
        self.conn = http.client.HTTPConnection(self.host, self.port)
        customer_data = 'customername=未和&customerphone=4664331213&childsex=男&childdate=2019-11-06&creditkids=0&creditcloth=0'
        header = {"Content-Type": "application/x-www-form-urlencoded",'Cookie':self.cookie}
        self.conn.request('POST', '/WoniuSales/customer/add', body=customer_data.encode('utf-8'), headers=header)
        resp = self.conn.getresponse()
        print(resp.read().decode())

if __name__ == '__main__':
    wst = WoniuSalesTest()
    wst.login()
    # wst.add_customer()