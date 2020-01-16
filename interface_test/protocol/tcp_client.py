#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 服务端的Ip和应用的端口
    client.connect(('127.0.0.1',8806))
    client.send("hello".encode())