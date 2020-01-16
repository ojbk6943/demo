#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from gui_test.woniusales_test.common.customer_manager import CustomerManager
from gui_test.woniusales_test.util.services import Services
from gui_test.woniusales_test.util.utility import Utility


class CustomerTest:

    def __init__(self,testcase_path,json_path):
        self.customer_data = Services.\
             get_data_from_case(testcase_path,'customermanager',3,4)
        self.config_info = Utility.read_json(json_path)


    def test_add_customer(self,driver):

        Services.add_woniusales_cookie(driver,self.config_info['URL'])
        Services.click_ele(driver,'LINK','会员管理')

        for customer_info in self.customer_data:
            import time
            sql = 'select count(customerid) from customer'
            old_customer_count = Utility.query_one(sql)
            CustomerManager().add_customer(driver, customer_info)
            time.sleep(3)
            new_customer_count = Utility.query_one(sql)
            if int(new_customer_count[0]) - int(old_customer_count[0]) == 1:
                actual = 'add-successful'
            else:
                if Services.is_element_present(driver,By.XPATH,'/html/body/div[7]/div/div/div[2]/div'):
                    alert_ele = Services.find_ele(driver,'XPATH','/html/body/div[7]/div/div/div[2]/div')
                    if alert_ele.text == '该客户信息已经存在，请勿重复添加.':
                        actual = 'already-added'
                    elif alert_ele.text == '请输入客户的电话号码.':
                        actual = 'add-failed'
                    else:
                        pass
                    driver.refresh()
                else:
                    actual = 'add-failed'

            flag = Services.assert_equal(customer_info['expect'],actual)
            if flag :
                print('添加用户测试成功')
            else:
                print('添加用户测试失败')
                Utility.get_png(driver, '..\\error_img\\')
        driver.close()

    def test_edit_customer():
            pass