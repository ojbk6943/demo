#测试结果写入html文件中
from whitetest_login.testcase.test_login import LoginTest
import unittest
def start1():
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('test_do_login'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
def start2():
    suite = unittest.TestSuite()
    loader=unittest.TestLoader()
    test=loader.loadTestsFromTestCase(LoginTest)
    suite.addTest(test)
    # runner = unittest.TextTestRunner(verbosity=2)
    # 使用运行器执行测试套
    # runner.run(suite)
    import HTMLTestRunner
    with open('..\\result\\test_report01.html','w') as file:
        html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title='report1')
        html_runner.run(suite)

def start3():
    unittest.main()

if __name__ == '__main__':
       start1()
