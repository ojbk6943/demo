#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from interfacetest.whitebox_test.whitebox_base.test_cacl_demo1 import TestCaclDemo1
import HTMLTestRunner

def start1():
    unittest.main(verbosity=2)

def start2():
    # 创建测试套对象
    ts = unittest.TestSuite()
    # 将多个测试用例家载入测试套中
    ts.addTests([TestCaclDemo1('test_add'),TestCaclDemo1('test_sub'),
                 TestCaclDemo1('test_mul'),TestCaclDemo1('test_div')])
    # 创建运行器对象
    tr = unittest.TextTestRunner(verbosity=2)
    # 使用运行器来运行测试套
    tr.run(ts)

def start3():
    ts = unittest.TestSuite()
    ts.addTest(TestCaclDemo1('test_mul'))
    ts.addTest(TestCaclDemo1('test_div'))
    tr = unittest.TextTestRunner(verbosity=2)
    tr.run(ts)

# 加载一个模块内的测试类中的所有测试用例
def start4():
    ts = unittest.TestSuite()
    # 创建加载器对象
    loader = unittest.TestLoader()
    # 通过加载器加载某个测试模块内的某个测试类
    tests = loader.loadTestsFromName('test_cacl_demo1.TestCaclDemo1')
    # 将测试用例集合添加入测试套中
    ts.addTests(tests)
    tr = unittest.TextTestRunner(verbosity=2)
    tr.run(ts)

# 加载多个模块内的不同的测试类中的测试用例
def start5():
    ts = unittest.TestSuite()
    # 创建加载器对象
    loader = unittest.TestLoader()
    # 通过加载器加载某个测试模块内的某个测试类
    tests = loader.loadTestsFromNames(['test_cacl_demo1.TestCaclDemo1','test_cacl_demo2.TestCaclDemo02'])
    # 将测试用例集合添加入测试套中
    ts.addTests(tests)
    tr = unittest.TextTestRunner(verbosity=2)
    tr.run(ts)

# 将测试结果写入txt文件中
def start6():
    ts = unittest.TestSuite()
    loader = unittest.TestLoader()
    ts.addTests(loader.loadTestsFromNames(['test_cacl_demo1.TestCaclDemo1', 'test_cacl_demo2.TestCaclDemo02']))
    with open('result.txt','w') as file:
        # 通过流的方式将测试结果写入文件中
        tr = unittest.TextTestRunner(stream=file,verbosity=2)
        tr.run(ts)

# 生成html格式的测试报告
def start7():
    ts = unittest.TestSuite()
    loader = unittest.TestLoader()
    ts.addTests(loader.loadTestsFromNames(['test_cacl_demo1.TestCaclDemo1', 'test_cacl_demo2.TestCaclDemo02']))
    with open('report.html','w') as file:
        # 通过流的方式将测试结果写入文件中
        # tr = unittest.TextTestRunner(stream=file,verbosity=2)
        # tr.run(ts)
        htmlrunner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title='cacl test result')
        htmlrunner.run(ts)

if __name__ == '__main__':
    start7()