#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from gui_test.unittest_demo.common.login import Login

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login = Login()

    def test_dologin(self):

        # flag = self.login.dologin('admin','123456')
        # self.assertEqual(flag,True)
        print("aaaaaaaaaa")
