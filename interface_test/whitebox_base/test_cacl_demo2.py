#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from interfacetest.whitebox_test.whitebox_base.cacl import Cacl

class TestCaclDemo02(unittest.TestCase):

    def test_add1(self):
        result = Cacl(100,200).add()
        self.assertEqual(result,300)

    def test_mul(self):
        result = Cacl(10,20).mul()
        self.assertEqual(result,2000)