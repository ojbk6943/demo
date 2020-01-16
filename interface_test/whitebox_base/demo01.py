#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Demo01:

    def get_reuslt(self,x,y,z):

        if x > 0 or y > 0:
            result = 1
            if z >= 10:
                result = 2
        else:
            result = 3

        return result