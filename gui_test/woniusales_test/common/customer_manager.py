#!/usr/bin/env python
#-*- coding:utf-8 -*-
from gui_test.woniusales_test.util.services import Services

class CustomerManager:

    def input_phone(self,driver,customer_phone):
        Services.input(driver, 'ID', 'customerphone', customer_phone)

    def input_name(self,driver,customer_name):
        Services.input(driver,'ID','customername', customer_name)

    def select_sex(self,driver):
        Services.select_random_option(driver,'ID','childsex')

    def input_date(self,driver,date):
        Services.input_date(driver,'ID','childdate',date)

    def input_creditkids(self,driver,creditkids):
        Services.input(driver,'ID','creditkids',creditkids)

    def input_creditcloth(self,driver,creditcloth):
        Services.input(driver,'ID','creditcloth',creditcloth)

    def click_add_customer(self,driver):
        Services.click_ele(driver,'SELECTOR','button.form-control:nth-child(1)')

    def click_edit_customer(self,driver):
        Services.click_ele(driver,'ID','editBtn')

    def click_query_customer(self,driver):
        Services.click_ele(driver,'SELECTOR','button.form-control:nth-child(3)')



    def query_customer(self,driver,phone):
        self.input_phone(driver, customer_info['customerphone'])
        self.click_query_customer(driver)


    def add_customer(self,driver,customer_info):
        self.input_phone(driver,customer_info['customerphone'])
        self.input_name(driver,customer_info['customername'])
        self.select_sex(driver)
        self.input_date(driver,customer_info['childdate'])
        self.input_creditkids(driver,customer_info['creditkids'])
        self.input_creditcloth(driver,customer_info['creditcloth'])
        self.click_add_customer(driver)
    def edit_customer(self,driver,contents,old_phone):

        Services.input(driver, 'ID', 'customerphone',old_phone)  #随机输入一个会员的电话
        Services.click_ele(driver, 'SELECTOR', 'button.form-control:nth-child(3)') #点击查询
        Services.click_ele(driver, 'XPATH', '//tbody[@id="customerlist"]/tr[1]/td[11]/a') #点击第一条数据后的修改
        Services.input(driver, 'ID', 'customerphone', contents["phone"])
        Services.input(driver, 'ID', 'customername', contents["name"])
        Services.input(driver, 'ID', 'creditkids', contents["credit_kids"])
        Services.input(driver, 'ID', 'creditcloth', contents['credit_cloth'])
        Services.click_ele(driver, 'ID', 'editBtn')

if __name__ == '__main__':
    driver = Services.get_driver('Firefox','http://192.168.2.104:8080/WoniuSales1.4/')
    customer_data = Services.get_data_from_case(3,4)
    Services.add_woniusales_cookie(driver,'http://192.168.2.104:8080/WoniuSales1.4/')
    print('a')
    Services.click_ele(driver,'LINK','会员管理')
    for customer_info in customer_data:
        CustomerManager().add_customer(driver, customer_info)
        driver.refresh()
