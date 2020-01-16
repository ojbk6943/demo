#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket

if __name__ == '__main__':

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost',8806))
    # listen(lenth)等待队列的长度
    server.listen(5)
    while 1:
        # 阻塞接收
        con = server.accept()
        print(con)
        msg = con[0].recv(1024).decode()
        print(msg)