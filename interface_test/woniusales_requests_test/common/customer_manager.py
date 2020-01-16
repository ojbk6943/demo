#!/usr/bin/env python
#-*- coding:utf-8 -*-

class CustomerManager:

    def add(self,session,url,data):
        return  session.post(url,data)

    def edit(self,session,url,data):
        return  session.post(url,data)

    def query(self,session,url,data):
        return  session.post(url,data)







