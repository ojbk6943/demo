#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from interface_test.woniusales_test.testcase.customer_test import CustomerTest
# class Driven:
#
#     def __init__(self):
#         from interface_test.woniusales_test.testcase.customer_test import CustomerTest
#
#
#
#     # def start(self):

def start2():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromName("interface_test.woniusales_test.testcase.customer_test.CustomerTest")
    suite.addTests(tests)
    # suite.addTests([CustomerTest("test_add_customer")])
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    # start2()
    import requests
    img_url = "http://192.168.2.18:8080/WoniuSales/image/logo.png"
    result = requests.get(img_url)
    with open('1.png','wb') as file:
        file.write(result.content)