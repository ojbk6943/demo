#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket

class SecServer:

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('localhost', 8806))

    def decrypt(self,sec_msg):

        real_msg = ""
        for s in sec_msg:
            real_msg += chr(ord(s) - 10)

        return real_msg

    def recv_msg(self):
        self.server.listen(5)
        while 1:
            # 阻塞接收
            con = self.server.accept()
            msg = con[0].recv(1024).decode()
            if msg.startswith('sec@'):
                real_msg = self.decrypt(msg[4:])
                print(real_msg)
            else:
                print(msg)

if __name__ == '__main__':
    SecServer().recv_msg()
