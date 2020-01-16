#!/usr/bin/env python
#-*- coding:utf-8 -*-

from gui_test.unittest_demo.testcases.cacl_test import CaclTest
from gui_test.unittest_demo.testcases.login_test import LoginTest
import unittest

def start1():
    unittest.main(verbosity=2)
# 创建测试套，将测试用例加入到测试套中，执行测试套
def start2():
    # 创建测试套
    suite = unittest.TestSuite()
    # suite.addTests([CaclTest('test_sub'),CaclTest('test_div'),LoginTest('test_dologin')])
    suite.addTest(CaclTest('test_sub'))
    # 创建运行器对象
    runner = unittest.TextTestRunner(verbosity=2)
    # 使用运行器执行测试套
    runner.run(suite)

# 通过加载器加载测试用例
def start3():
    suite = unittest.TestSuite()
    # 创建加载器对象
    loader = unittest.TestLoader()
    # 加载一个模块内的一个测试类中的所有的测试用例
    # tests = loader.loadTestsFromName('gui_test.unittest_demo.testcases.cacl_test.CaclTest')
    tests = loader.loadTestsFromNames(['gui_test.unittest_demo.testcases.cacl_test.CaclTest',
                                       'gui_test.unittest_demo.testcases.login_test.LoginTest'])
    # 将测试集添加至测试套中
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

# 将测试结果写入文件中
def start4():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # tests = loader.loadTestsFromName('gui_test.unittest_demo.testcases.cacl_test.CaclTest')
    tests = loader.loadTestsFromNames(['gui_test.unittest_demo.testcases.cacl_test.CaclTest',
                                       'gui_test.unittest_demo.testcases.login_test.LoginTest'])
    # 将测试集添加至测试套中
    suite.addTests(tests)
    with open('..\\result\\test_result02.txt','w') as file:
        # 以流的方式写入文本文件
        runner = unittest.TextTestRunner(stream=file,verbosity=2)
        runner.run(tests)
# 将测试结果写入html文件中
def start5():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # tests = loader.loadTestsFromName('gui_test.unittest_demo.testcases.cacl_test.CaclTest')
    tests = loader.loadTestsFromNames(['gui_test.unittest_demo.testcases.cacl_test.CaclTest',
                                       'gui_test.unittest_demo.testcases.login_test.LoginTest'])
    # 将测试集添加至测试套中
    suite.addTests(tests)
    import HTMLTestRunner
    with open('..\\result\\test_report01.html','w') as file:
        html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title='report1')
        html_runner.run(suite)

if __name__ == '__main__':
    start2()
