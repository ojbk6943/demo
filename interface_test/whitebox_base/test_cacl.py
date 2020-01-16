#!/usr/bin/env python
#-*- coding:utf-8 -*-
from interfacetest.whitebox_test.whitebox_base.cacl import Cacl
class TestCacl:

    def __init__(self,x,y):
        self.c = Cacl(x,y)

    def test_add(self,expect):
        result = self.c.add()
        if result == expect:
            print('add test pass')
        else:
            print('add test fail')

    def test_sub(self,expect):
        result = self.c.sub()
        if result == expect:
            print('sub test pass')
        else:
            print('sub test fail')

    def test_mul(self,expect):
        result = self.c.mul()
        if result == expect:
            print('mul test pass')
        else:
            print('mul test fail')

    def test_div(self,expect):
        result = self.c.div()
        if result == expect:
            print('div test pass')
        else:
            print('div test fail')

if __name__ == '__main__':
    TestCacl(10,20).test_div(2)
    TestCacl(10, 'xyz').test_div('必须是数字')
    TestCacl(0, 10).test_div('被0除')
    # cacl.test_add(20)
    # cacl.test_mul(0)
    # cacl.test_sub(-20)
    # cacl.test_div(0.5)