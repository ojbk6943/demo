#!/usr/bin/env python
#-*- coding:utf-8 -*-

import http.client

if __name__ == '__main__':

    # 创建和主机的连接
    conn = http.client.HTTPConnection('192.168.2.17',8080)
    # 向服务器发送请求
    conn.request('get','/WoniuSales/')
    # 从服务器中获得响应
    resp = conn.getresponse()
    # 从响应中获取内容(响应正文)
    # print(resp.status)
    # print(resp.reason)
    # print(resp.read().decode())
    # if resp.status == 200:
    #     print('正确响应')
    if '蜗牛进销存-首页' in resp.read().decode():
        print('获取内容正确')
    else:
        print('不正确')