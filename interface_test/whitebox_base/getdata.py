#!/usr/bin/env python
#-*- coding:utf-8 -*-

class GetData:

    def get_data_from_txt(self,path):
        params = []
        with open(path) as file:
            contents = file.readlines()
        for content in contents:
            l = content.strip().split(',')
            t = tuple(l)
            params.append(t)
        return params

    def get_data_from_excel(self,url):
        pass
