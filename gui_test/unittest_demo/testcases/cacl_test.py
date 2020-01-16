#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from parameterized import parameterized
from gui_test.unittest_demo.common.cacl import Cacl
parm = [(10,2,5),(10,1,1),(10,0,1)]

class CaclTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cacl = Cacl()
    #会在每一条测试用例执行前执行的方法
    def setUp(self):
        pass

    def test_add(self):
        result = self.cacl.add(10,20)
        self.assertEqual(30,result)

    def test_sub(self):
        result = self.cacl.sub(20, 30)
        self.assertEqual(10, result)

    def test_mul(self):
        result = self.cacl.mul(20, 50)
        self.assertEqual(1000, result)

    @parameterized.expand(parm)
    def test_div(self,x,y,expect):
        result = self.cacl.div(x,y)
        self.assertEqual(expect, result)

    # 每次执行完成一条测试用例后都会执行一次teardown
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')





