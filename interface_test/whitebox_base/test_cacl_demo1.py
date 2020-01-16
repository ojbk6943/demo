#!/usr/bin/env python
#-*- coding:utf-8 -*-
from interfacetest.whitebox_test.whitebox_base.cacl import Cacl
from parameterized import parameterized
from interfacetest.whitebox_test.whitebox_base.getdata import GetData
import unittest,sys
sys.path.append('D:\PycharmProjects\WNXA19')

# 从文件中获取规定格式的数据
param = GetData().get_data_from_txt('data\\cacl_data')

class TestCaclDemo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # 对每一条测试用例都执行收尾工作
    # def tearDown(self):
    #     print('tearDown')
    #     # pass

    # 对每一条测试用例都进行初始化（准备工作）
    # def setUp(self):
    #     print('setUp')
    #     # pass

    # 测试用例必须以test开始
    def test_add(self):
        result = Cacl(3,5).add()
        print('test add')
        # 在测试用例中必须要有断言
        self.assertEqual(8,result)

    @unittest.skip('该方法未完成')
    def test_sub(self):
        result = Cacl(9,2).sub()
        print('test sub')
        self.assertEqual(result,5)

    # 不会执行非test开头的普通方法
    @unittest.skipIf(5>3)
    def test_fun(self):
        print('a')

    def test_mul(self):
        result = Cacl(3, 2).mul()
        print('test mul')
        self.assertEqual(result, 6)

    # def test_div(self):
    #     try:
    #         result = Cacl(6, 0).div()
    #     except:
    #         print('报错')
    #     finally:
    #         print('test div')
    #         self.assertEqual(result, 3)

    # def test_div(self):
    #     div_data = [(10,2,5),(9,0,2),(100,10,5),(0,8,0)]
    #     for data in div_data:
    #         a,b,expect = data
    #         actual = Cacl(a,b).div()
    #         self.assertEqual(actual,expect)

    # def test_div(self):
    #     errors = []
    #     div_data = [(10, 2, 5), (9, 0, 2), (100, 10, 5), (0, 0, 0)]
    #     for data in div_data:
    #         a, b, expect = data
    #         try:
    #             actual = Cacl(a, b).div()
    #             self.assertEqual(actual, expect)
    #         except Exception as e:
    #             errors.append(e)
    #     raise AssertionError(errors)

    @parameterized.expand(param)
    def test_div(self,a,b,expect):
        actual = Cacl(int(a), int(b)).div()
        self.assertEqual(actual,int(expect))





if __name__ == '__main__':
    # verbosity = 0代表没有信息，1代表默认信息（少）,2代表详细信息，显示哪一个测试用例的结果
    # unittest.main(verbosity=2)
    # unittest.main(verbosity=2)
    get_data()