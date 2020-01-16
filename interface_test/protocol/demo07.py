#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json

if __name__ == '__main__':

    # d1 = '[{"a":"x"},{"b":"y"},{"c":"z"}]'
    d1 = '[{"a":[1,2,3],"b":[4,5,6]}]'
    nd1 = json.loads(d1)
    print(type(nd1))
    print(nd1[0])