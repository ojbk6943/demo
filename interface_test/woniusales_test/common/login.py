#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from gui_test.woniusales_test.util.services import Services
class Login:

    def input_uname(self,driver,content):
        Services.input(driver,'ID','username',content)

    def input_upass(self,driver,content):
        Services.input(driver, 'ID', 'password', content)

    def input_verifycode(self,driver,content):
        Services.input(driver, 'ID', 'verifycode', content)

    def click_login(self,driver):
        Services.click_ele(driver,'SELECTOR','button.form-control')

    def do_login(self,driver,login_info):
        self.input_uname(driver,login_info['uname'])
        self.input_upass(driver,login_info['upass'])
        self.input_verifycode(driver,login_info['verifycode'])
        self.click_login(driver)

if __name__ == '__main__':
    pass
    # driver = Services.get_driver('Firefox','http://192.168.2.17:8080/WoniuSales')
    # login_data = [{'uname':'admin','upass':'admin','verifycode':'0000'},{'uname':'admin','upass':'admin1','verifycode':'0000'}]
    # for login_info in login_data:
    #     Login().do_login(driver,login_info)
    #     if Services.is_element_present(driver,By.LINK_TEXT,'注销'):
    #         actual = 'login-pass'
    #         Services.click_ele(driver,'LINK','注销')
    #     else:
    #         actual = 'login-fail'
    #         driver.refresh()


