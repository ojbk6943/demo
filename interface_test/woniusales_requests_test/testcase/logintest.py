#!/usr/bin/env python
#-*- coding:utf-8 -*-
from gui_test.woniusales_test.common.login import Login
from gui_test.woniusales_test.util.services import Services
from selenium.webdriver.common.by import By
from gui_test.woniusales_test.util.utility import Utility
import unittest
from time import sleep
class LoginTest(unittest.TestCase):
    # 准备测试数据
    @classmethod
    def setupclass(cls):
        pass
    # def setup(cls):
    #     path='..\\test_data\\login_data.txt'
    #     contents = Utility.read_txt(path)
    #     cls.login_data = []
    #     cls.login=Login()
    #     for content in contents:
    #         # 选取没有被注释掉的数据
    #         if content.startswith('#') == False:
    #             li = content.strip().split(',')
    #             dict = {'uname':li[0],'upass':li[1],'verifycode':li[2],'expect':li[3]}
    #             cls.login_data.append(dict)
    def test_login(self):
        #获取生成driver的信息
        contents = Utility.read_json('..\\config\\base_config')  # 在json中读取要生成浏览器的信息
        driver_info = {'BROWSER': contents['BROWSER'], 'URL': contents['URL']}
        # 生成driver
        driver = Services.get_driver(driver_info['BROWSER'], driver_info['URL'])  # 生成浏览器

        #获取登录数据
        path = '..\\test_data\\login_data.txt'
        contents = Utility.read_txt(path)
        # print(contents)
        login_data = []
        login = Login()
        for content in contents:
            # 选取没有被注释掉的数据
            if content.startswith('#') == False:
                li = content.strip().split(',')
                dict = {'uname': li[0], 'upass': li[1], 'verifycode': li[2], 'expect': li[3]}
                login_data.append(dict)
        print(login_data)
        for login_info in login_data:
            Login().do_login(driver, login_info)
            if Services.is_element_present(driver, By.LINK_TEXT, '注销'):
                actual = 'login-pass'
                Services.click_ele(driver, 'LINK', '注销')
                sleep(2)
            else:
                actual = 'login-fail'
                driver.refresh()
            self.assertEqual(login_info['expect'], actual)
            # flag = Services.assert_equal(login_info['expect'],actual)
            # if flag:
            #     print('login test success')
            # else:
            #     print('login test fail')
            #     Utility.get_png(driver,'..\\error_img\\')
            # self.assertEqual(login_info['expect'], actual)

if __name__=='__main__':
    unittest.main()