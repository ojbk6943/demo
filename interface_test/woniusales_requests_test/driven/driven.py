#!/usr/bin/env python
#-*- coding:utf-8 -*-
from gui_test.woniusales_test.testcase.customer_manager_test import Customer_Manager_Test
from gui_test.woniusales_test.testcase.customer_test import CustomerTest
from gui_test.woniusales_test.testcase.logintest import LoginTest
from gui_test.woniusales_test.util.services import Services
from gui_test.woniusales_test.util.utility import Utility
from gui_test.woniusales_test.testcase.customer_manager_test import Customer_Manager_Test
from interface_test.woniusales_requests_test.testcase.customer_manager_test import Customer_Manager_case
import unittest

def start1():
    #创建测试用例套件
    suite=unittest.TestSuite()
    #加载器
    loader=unittest.TestLoader()
    tests=loader.loadTestsFromNames(['gui_test.woniusales_test.testcase.logintest.LoginTest',
                                   'gui_test.woniusales_test.testcase.customer_manager_test.Customer_Manager_Test'])


    # suite.addTest(LoginTest('test_login'))
    suite.addTest(tests)
    #运行器
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

def start2():
    suite = unittest.TestSuite()
    # 加载器
    # loader = unittest.TestLoader()
    suite.addTest(Customer_Manager_case('test_add_customer'))

    # suite.addTest(LoginTest('test_login'))
    # suite.addTest(test)
    # 运行器
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
def start3():
    suite = unittest.TestSuite()
    # 加载器
    loader = unittest.TestLoader()
    test=loader.loadTestsFromTestCase(Customer_Manager_case)

    suite.addTest(test)

    # suite.addTest(LoginTest('test_login'))
    # suite.addTest(test)
    # 运行器
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
if __name__=='__main__':
    # do_testcase_testlogin()
    # Driven().do_testcase_testlogin()
    # Driven().do_testcase_customermanager()
    start3()
