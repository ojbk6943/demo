#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
from selenium.webdriver.common.by import By
from webdriver_base.util import Utility
from random import randint
from selenium.webdriver.support.select import Select

class WoniuSalesTest:

    def __init__(self,browser,url):
        from selenium import webdriver
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'Ie':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Firefox()
        self.db_info = ('192.168.2.104', 'root', '123456', 'woniusales')
        self.driver.implicitly_wait(20)
        self.driver.get(url)
        self.driver.maximize_window()


    def is_element_present(self, how, what):
        from selenium.common.exceptions import NoSuchElementException
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def assert_equal(self,expect,actual):
        if expect == actual:
            print('test success!')
        else:
            print('test fail!')

    def add_woniusales_cookie(self):
        self.driver.add_cookie({'name': 'username', 'value': 'admin'})
        self.driver.add_cookie({'name': 'password', 'value': '123456'})
        self.driver.get('http://192.168.2.104:8080/WoniuSales1.4/')


    def login(self,login_info):

        driver = self.driver
        uname = driver.find_element_by_id('username')
        uname.click()
        uname.clear()
        uname.send_keys(login_info[0])

        upass = driver.find_element_by_id('password')
        upass.click()
        upass.clear()
        upass.send_keys(login_info[1])

        driver.find_element_by_id('verifycode').send_keys('0000')

        driver.find_element_by_css_selector('button.form-control').click()

    def test_login(self):
        login_data = [('admin','admin','login-pass'),('admin','admin1','login-fail'),
                 ('admin1','admin','login-fail'),('','admin','login-fail'),('admin','','login-fail')]


        for login_info in login_data:
            self.login(login_info)
            if self.is_element_present(By.LINK_TEXT,'注销'):
                actual = 'login-pass'
                self.driver.find_element_by_partial_link_text('注销').click()
            else:
                actual = 'login-fail'
                time.sleep(2)
                self.driver.refresh()

            self.assert_equal(login_info[2],actual)
    #新增用户
    def add_customer(self,customer_info):

        driver = self.driver
        self.add_woniusales_cookie()
        driver.find_element_by_partial_link_text('会员管理').click()
    #电话
        customer_phone = driver.find_element_by_id('customerphone')
        customer_phone.click()
        customer_phone.clear()
        customer_phone.send_keys(customer_info[0])
    #姓名
        customer_name = driver.find_element_by_id('customername')
        customer_name.click()
        customer_name.clear()
        customer_name.send_keys(customer_info[1])

    #性别
        child_sex = driver.find_element_by_id('childsex')
        all_sex = Select(child_sex).options

        Select(child_sex).select_by_index(randint(0,len(all_sex)-1))
    #出生日期
        child_date = driver.find_element_by_id('childdate')
        driver.execute_script('document.getElementById("childdate").readOnly=false;')
        child_date.clear()
        child_date.send_keys(customer_info[2])
    #母婴积分
        credit_kids = driver.find_element_by_id('creditkids')
        credit_kids.click()
        credit_kids.clear()
        credit_kids.send_keys(customer_info[3])
    #童装积分
        credit_cloth = driver.find_element_by_id('creditcloth')
        credit_cloth.click()
        credit_cloth.clear()
        credit_cloth.send_keys(customer_info[4])
    #点击新增
        driver.find_element_by_css_selector('button.form-control:nth-child(1)').click()

    def test_add_customer(self):
        customer_data = [('18000004', '小明', '2005-03-01', '100', '200', 'add-customer-success')]
        print('添加客户测试结果：')
        for customer_info in customer_data:
            self.add_customer(customer_info)
            if self.is_element_present(By.CSS_SELECTOR,'.modal-sm > div:nth-child(1) > div:nth-child(1) > h4:nth-child(2)'):
                actual = 'add-customer-fail'
                self.driver.refresh()
            else:
                info = self.query_customer(customer_info[0])
                if info is not None:
                    if info[1] == customer_info[1] and info[2] == customer_info[2] and \
                        info[3] == customer_info[3] and info[4] == customer_info[4] :

                        actual = 'add-customer-success'
                        sql = 'delete from customer where customerphone="%s"' % (customer_info[0])

                        if Utility.update_db(self.db_info, sql):
                            print('数据已清空')
                        else:
                            print('数据清空失败')

                else:
                    actual = 'add-customer-fail'

            self.assert_equal(customer_info[5],actual)
    #查询会员信息
    def query_customer(self,phone):
        driver = self.driver
        customer_phone = driver.find_element_by_id('customerphone')
        customer_phone.click()
        customer_phone.clear()
        customer_phone.send_keys(phone)
        driver.find_element_by_css_selector('button.form-control:nth-child(3)').click()
        # query_result = ()
        # customer_phone_list = driver.find_elements_by_xpath('//tbody[@id="customerlist"]/tr/td[2]')
        time.sleep(3)
        if self.is_element_present(By.LINK_TEXT,'修改'):
            customer_phone = driver.find_element_by_xpath('//tbody[@id="customerlist"]/tr/td[2]').text
            customer_name = driver.find_element_by_xpath('//tbody[@id="customerlist"]/tr/td[3]').text
            customer_data = driver.find_element_by_xpath('//tbody[@id="customerlist"]/tr/td[5]').text
            credit_kids =  driver.find_element_by_xpath('//tbody[@id="customerlist"]/tr/td[6]').text
            credit_cloth = driver.find_element_by_xpath('//tbody[@id="customerlist"]/tr/td[7]').text
            return (customer_phone,customer_name,customer_data,credit_kids,credit_cloth)
        else:
            return None

    # 在数据库中随机查询一条电话号码
    def get_phone_from_db(self):
        sql = 'select customerphone from customer'
        phones = Utility.query_all(self.db_info, sql)
        random_phone_index = randint(0, len(phones) - 1)
        return phones[random_phone_index][0]

    def edit_customer(self,edit_info):
        driver = self.driver
        self.add_woniusales_cookie()
        driver.find_element_by_partial_link_text('会员管理').click()

        # 从数据库查询一条随机的电话号码
        random_phone = self.get_phone_from_db()
        self.query_customer(random_phone)

        # 修改客户信息
        time.sleep(2)
        driver.find_element_by_xpath('//tbody[@id="customerlist"]/tr[1]/td[11]/a').click() #点查询
        customer_phone = driver.find_element_by_id('customerphone')
        customer_phone.click()
        customer_phone.clear()
        customer_phone.send_keys(edit_info[0])

        customer_name = driver.find_element_by_id('customername')
        customer_name.click()
        customer_name.clear()
        customer_name.send_keys(edit_info[1])

        credit_kids = driver.find_element_by_id('creditkids')
        credit_kids.click()
        credit_kids.clear()
        credit_kids.send_keys(edit_info[2])

        credit_cloth = driver.find_element_by_id('creditcloth')
        credit_cloth.click()
        credit_cloth.clear()
        credit_cloth.send_keys(edit_info[3])

        driver.find_element_by_id('editBtn').click()

    def test_edit_customer(self):
        edit_customer_data = [('18112121324','','120','2000','edit-pass'),
                              ('1811212sdfa24','','120111111111111','2000','edit-fail'),('18112121212','小明','2000','','edit-fail')]
        print('编辑客户信息测试结果：')
        for edit_info in edit_customer_data:
            self.edit_customer(edit_info)
            if self.is_element_present(By.CSS_SELECTOR,'.modal-sm > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)'):
                actual = 'edit-pass'
            else:
                actual = 'edit-fail'

            self.assert_equal(edit_info[-1],actual)

    # 输入商品条码
    def input_barcode(self,barcode):
        driver = self.driver
        self.add_woniusales_cookie()
        driver.find_element_by_partial_link_text('销售出库').click()

        barcode_ele = driver.find_element_by_id('barcode')
        barcode_ele.click()
        barcode_ele.clear()
        barcode_ele.send_keys(barcode)

        driver.find_element_by_css_selector('div.container:nth-child(6) > '
                                            'div:nth-child(1) > div:nth-child(1) > '
                                            'div:nth-child(1) > form:nth-child(1) > button:nth-child(3)').click()


    def test_input_barcode(self):

        barcode_data = [('11111111','barcode-pass'),('12345','barcode-fail'),('','barcode-fail')]
        print('查找条码测试结果：')
        for barcode in barcode_data:
            self.input_barcode(barcode[0])
            if self.is_element_present(By.LINK_TEXT,'移除') :
                actual = 'barcode-pass'
            else:
                actual = 'barcode-fail'
                self.driver.refresh()

            self.assert_equal(barcode[1],actual)

    def get_random_customer_info(self,random_phone):
        driver = self.driver
        self.add_woniusales_cookie()
        driver.find_element_by_partial_link_text('销售出库').click()
        customer_phone = driver.find_element_by_id('customerphone')
        customer_phone.click()
        customer_phone.clear()
        customer_phone.send_keys(random_phone)
        driver.find_element_by_css_selector('#vipsell > '
                                            'div:nth-child(1) > form:nth-child(1) > '
                                            'div:nth-child(2) > button:nth-child(3)').click()
    #
    def test_customer_info(self):
        random_phone = self.get_phone_from_db()
        self.get_random_customer_info(random_phone)
        sql = 'select credittotal from customer where customerphone="%s"'%(random_phone)
        credittotal = Utility.query_one(self.db_info,sql)
        time.sleep(2)
        print(self.driver.find_element_by_id('oldcredit').get_attribute('value'))
        print(credittotal[0])
        if self.driver.find_element_by_id('oldcredit').get_attribute('value') == str(credittotal[0]) :
            actual = 'phone-pass'
        else:
            actual = 'phone-fail'
        print('测试积分是否正确')
        self.assert_equal('phone-pass',actual)

    def confirm_money(self,money_info):
        driver = self.driver

        self.input_barcode(money_info[0])
        customer_phone = driver.find_element_by_id('customerphone')

        customer_phone.click()
        customer_phone.clear()
        customer_phone.send_keys(money_info[1])
        driver.find_element_by_css_selector('#vipsell > '
                                            'div:nth-child(1) > form:nth-child(1) > '
                                            'div:nth-child(2) > button:nth-child(3)').click()

        paymethod = driver.find_element_by_id('paymethod')
        paymethod_list = Select(paymethod).options
        Select(paymethod).select_by_index(randint(0,len(paymethod_list)-1))

        creditratio = driver.find_element_by_id('creditratio')
        creditratio.click()
        creditratio.clear()
        creditratio.send_keys(money_info[2])

        # tickettype = driver.find_element_by_id('tickettype')
        # tickettype.click()
        # tickettype.clear()
        # tickettype.send_keys(money_info[3])

        ticketsum = driver.find_element_by_id('ticketsum')
        ticketsum.click()
        ticketsum.clear()
        ticketsum.send_keys(money_info[4])

        driver.find_element_by_id('submit').click()


    def test_confirm_money(self):
        self.add_woniusales_cookie()
        self.driver.find_element_by_partial_link_text('销售出库').click()
        random_phone = self.get_phone_from_db()
        confirm_money_data = [('11111111', '888777', '1.5','1000', '10', 'get_money-pass'),
                              ('1111222', random_phone, '0', '2000', '-10', 'get_money-pass')]
        print('销售出库测试结果为：')
        for money_info in confirm_money_data:
            sql = 'select count(sellid) from sell'
            old_result = Utility.query_one(self.db_info,sql)
            self.confirm_money(money_info)

            self.driver.switch_to.alert.accept()
            if money_info[1] == '':
                time.sleep(2)
                self.driver.switch_to.alert.accept()

            new_result = Utility.query_one(self.db_info,sql)
            if new_result[0] - old_result[0] == 1 :
                actual = 'get_money-pass'
            else:
                actual = 'get_money-fail'

            self.assert_equal(money_info[5],actual)


if __name__ == '__main__':
    wst = WoniuSalesTest('Firefox','http://192.168.2.17:8080/WoniuSales/')
    # wst.test_login()
    # wst.test_add_customer()
    # wst.test_edit_customer()
    # wst.edit_customer(('18112121212','小明','120','2000'))
    # wst.test_input_barcode()
    # wst.test_customer_info()
    wst.test_confirm_money()





