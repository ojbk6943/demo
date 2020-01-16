from gui_test.unittest_demo.testcases.cacl_test import CaclTest
import unittest
def start1():
    unittest.main(verbosity=2)
def start2():
    #创建一个测试套
    suite=unittest.TestSuite()
    #给测试套添加用例
    suite.addTests([CaclTest('test_div'),CaclTest('test_sub')])
    #创建一个运行器对象
    runner=unittest.TextTestRunner(verbosity=2)
    #运行测试套
    runner.run(suite)
def start3():
    # 创建一个测试套
    suite = unittest.TestSuite()
    # 给测试套添加用例
    test=[(CaclTest('test_div')),CaclTest('test_sub')]
    suite.addTests(test)
    # 创建一个运行器对象
    runner = unittest.TextTestRunner(verbosity=2)
    # 运行测试套
    runner.run(test)

#通过加载器给测试套子中加载测试用例
def start4():
    # 创建一个测试套
    suite=unittest.TestSuite()
    #创建一个加载器
    loader=unittest.TestLoader()
    # test=loader.loadTestsFromTestCase(CaclTest)
    test=loader.loadTestsFromNames(['gui_test.unittest_demo.testcases.cacl_test.CaclTest',
                                       'gui_test.unittest_demo.testcases.login_test.LoginTest'])
    unittest.TextTestRunner.run(test)











if __name__=='__main__':
    # start1()
    # start2()
    # start3()
    start4()



