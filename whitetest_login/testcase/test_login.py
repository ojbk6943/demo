import unittest

from selenium.webdriver.common.by import By

from whitetest_login.common.login import Login
from whitetest_login.util.services import Services
from whitetest_login.util.utility import Utility
from parameterized import parameterized
from time import sleep
data = Utility.read_txt('..\\testdata\\login_data')
class LoginTest(unittest.TestCase):
    
    sleep(2)
    def setUp(self):
        #准备数据
        # self.data = Utility.read_txt('..\\testdata\\login_data')
        # print("a")
        self.driver=Services.get_driver('Firefox','http://192.168.2.102:8080/WoniuSales1.4/')
        sleep(2)
        self.log=Login()
        # print('11')

    @parameterized.expand(data)
    def test_do_login(self,a,b,c,expect):
        # driver=self.driver
        # print('a')
        self.log.do_login(self.driver,(a,b,c))
        if Services.is_element_present(self.driver,By.LINK_TEXT,'注销'):
            actual='login-pass'
        else:
            actual='login-fail'
        self.assertEqual(expect,actual)
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()





