#!/usr/bin/env python
#-*- coding:utf-8 -*-


import requests,json

class WoniuSalesTest:

    def __init__(self):

        self.host = '192.168.2.17'
        self.port = 8080
        self.program = '/WoniuSales'
        self.base_url = 'http://' + self.host +':'+ str(self.port)  + self.program
        self.session = requests.session()

    def open_homepage(self):

        open_homepage_resp = self.session.get(self.base_url)

        if '蜗牛进销存-首页' in open_homepage_resp.text:
            print('open homepage success')
        else:
            print('open homepage fail')

    def login(self):

        login_data = {'username': 'admin', 'password': 'admin', 'verifycode': '0000'}
        login_url =  '/user/login'
        login_url = self.base_url + login_url
        login_resp = self.session.post(login_url,login_data)
        if login_resp.text == 'login-pass' :
            print('login success')
        else:
            print('login fail')

    def add_customer(self):

        add_customer_data = {'customername': '未和', 'customerphone': '4664331215', 'childsex': '男',
                        'childdate':'2019-11-06','creditkids':'0','creditcloth':'0'}
        add_customer_url = '/customer/add'
        add_customer_url = self.base_url + add_customer_url
        add_customer_resp = self.session.post(add_customer_url, add_customer_data)
        print(add_customer_resp.text)
        if add_customer_resp.text == 'already-added':
            print('add customer again')
        elif add_customer_resp.text == 'add-successful':
            print('add customer success')
        else:
            print('add customer fail')

    def query_customer(self):

        query_customer_data = {'customerphone': '4664331215','page':'1'}
        query_customer_url = '/customer/search/'
        query_customer_url = self.base_url + query_customer_url

        query_cusotmer_resp = self.session.post(query_customer_url,query_customer_data)
        # 使用pyton的json的loads方法，可以将字符串转化为python的原始数据类型
        # result = json.loads(query_cusotmer_resp.text)
        # print(type(result))
        result = query_cusotmer_resp.json()
        if result[0]['childsex'] == '男' and '2019-11-06' == result[0]['childdate'] and \
                0 == result[0]['credittotal']:
            print('ok')
        else:
            print('fail')

    # 上传文件
    def upload_batch(self):
        upload_batch_url = '/goods/upload'
        upload_batch_url = self.base_url + upload_batch_url
        upload_batch_data = {'batchname':'GB20191101'}
        upload_batch_file = {"batchfile":('t1.png',open('H:\\test1.png','rb'))}
        upload_batch_resp = self.session.post(upload_batch_url,upload_batch_data,files=upload_batch_file)
        print(upload_batch_resp.text)


if __name__ == '__main__':

    wst = WoniuSalesTest()
    # wst.test_open_homepage()
    wst.login()
    # wst.customer()
    # wst.query_customer()
    wst.upload_batch()