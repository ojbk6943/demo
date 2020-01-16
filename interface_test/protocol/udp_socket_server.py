#!/usr/bin/env python
# coding=utf8

import socket

# 建立一个UDP连接.两个参数，第一个是ipv4
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口和主机
server.bind(('localhost', 23456))
while 1:
    # 接收数据
    con, addr = server.recvfrom(1024)
    #con[0].send('连接成功。。。'.encode('GBK'))
    print(con.decode('utf8'))