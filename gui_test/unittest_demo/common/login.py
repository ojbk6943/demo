#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Login:

    def dologin(self,uname,upass):

        if uname == 'admin' and upass == '123456':
            return True
        else:
            return False
