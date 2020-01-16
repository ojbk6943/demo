#!/usr/bin/env python
#-*- coding:utf-8 -*-

def mydec(func):
    def temp_fun(*args,**kwargs):
        print('这是装饰器增强的功能')
        func(*args,**kwargs)
    return temp_fun

@mydec
def fun1():
    print('hello')

if __name__ == '__main__':
    fun1()