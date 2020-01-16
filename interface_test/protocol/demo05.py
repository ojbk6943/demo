#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests

if __name__ == '__main__':

    # openpage_resp = requests.get('http://192.168.2.17:8080/WoniuSales')
    # # print(openpage_resp.content.decode())
    # # print(openpage_resp.status_code)
    # # print(openpage_resp.reason)
    # # # print(openpage_resp.headers)
    # # print(openpage_resp.cookies)
    # login_data = {'username':'admin','password':'admin','verifycode':'0000'}
    # login_resp = requests.post('http://192.168.2.17:8080/WoniuSales/user/login',login_data)
    # print(login_resp.headers)
    # # print(login_resp.text)
    # add_customer_data = {'customername':'未和','customerphone':'4664331215','childsex':'男',
    #                     'childdate':'2019-11-06','creditkids':'0','creditcloth':'0'}
    # add_customer_url = 'http://192.168.2.17:8080/WoniuSales/customer/add'
    # add_customer_resp = requests.post(add_customer_url,add_customer_data)
    # print(add_customer_resp.text)

    # 获取session对象
    session = requests.session()
    session.get('http://192.168.2.17:8080/WoniuSales')
    login_data = {'username': 'admin', 'password': 'admin', 'verifycode': '0000'}
    # session会自动记录cookie信息
    session.post('http://192.168.2.17:8080/WoniuSales/user/login',login_data)
    add_customer_data = {'customername': '未和', 'customerphone': '4664331215', 'childsex': '男',
                        'childdate':'2019-11-06','creditkids':'0','creditcloth':'0'}
    add_customer_url = 'http://192.168.2.17:8080/WoniuSales/customer/add'
    add_customer_resp = session.post(add_customer_url,add_customer_data)
    print(add_customer_resp.text)
