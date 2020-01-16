#!/usr/bin/env python
#-*- coding:utf-8 -*-
from gui_test.woniusales_test.util.utility import Utility
class Services:

    # 获取driver
    @classmethod
    def get_driver(cls,BROWSER,URL):
        from selenium import webdriver
        if BROWSER == 'Chrome':
            cls.driver = webdriver.Chrome()
        elif BROWSER == 'Firefox':
            cls.driver = webdriver.Firefox()
        elif BROWSER == 'Ie':
            cls.driver = webdriver.Ie()
        else:
            cls.driver = webdriver.Firefox()

        cls.driver.get(URL)
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

        return cls.driver

    # 找到需要的元素
    @classmethod
    def find_ele(cls,driver,type,value):
        from selenium import webdriver

        if type == 'ID':
            ele = driver.find_element_by_id(value)
        elif type == 'NAME':
            ele = driver.find_element_by_name(value)
        elif type == 'CLASSNAME':
            ele = driver.find_element_by_class_name(value)
        elif type == 'LINK':
            ele = driver.find_element_by_link_text(value)
        elif type == 'SELECTOR':
            ele = driver.find_element_by_css_selector(value)
        elif type == 'XPATH':
            ele = driver.find_element_by_xpath(value)
        else:
            pass

        return ele

    # 单击某个元素
    @classmethod
    def click_ele(cls,driver,type,value):
        ele = cls.find_ele(driver,type,value)
        ele.click()
        return ele

    @classmethod
    # 给页面中的元素赋值
    def input(cls,driver,type,value,content):
        ele = cls.click_ele(driver,type,value)
        ele.clear()
        ele.send_keys(content)

    # 判断页面元素是否存在
    @classmethod
    def is_element_present(cls,driver,how, what):
        from selenium.common.exceptions import NoSuchElementException
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True



    # 断言相等
    @classmethod
    def assert_equal(cls,expect,actual):
        if expect == actual:
            return True
        else:
            return False

    # 随机选择下拉选项
    @classmethod
    def select_random_option(cls,driver,type,value):
        from selenium.webdriver.support.select import Select
        ele = cls.find_ele(driver,type,value)
        ele_options = Select(ele).options
        random_index = Utility.get_random(len(ele_options)-1)
        Select(ele).select_by_index(random_index)

    # 向不可写的日期控件中输入日期
    @classmethod
    def input_date(cls,driver,type,value,date):
        ele = cls.find_ele(driver, type, value)
        driver.execute_script('document.getElementById("%s").readOnly=false;' %(value))
        cls.input(driver,type,value,date)

    # 添加cookie
    @classmethod
    def add_woniusales_cookie(cls,driver,URL):
        contents = Utility.read_json('..\\config\\cookie_config')
        for content in contents:
            driver.add_cookie(content)
        driver.get(URL)


    # 从测试用例中读取测试数据,j代表测试数据列，k代表预期结果列
    @classmethod
    def get_data_from_case(cls,j,k):
        result = Utility.read_xls('..\\test_data\\woniusales_test_cases.xlsx', 'customermanager')
        customer_data = []
        for i in range(1, result.nrows):  #result.nrows 读取sheet页的行数
            temp1 = result.cell(i, j).value   #获取数据列的值
            temp2 = result.cell(i, k).value   #获取期望列的值
            # print(temp2)
            li = temp1.split('\n')
            dict = {}
            for info in li:
                t = info.split('=')
                dict[t[0]] = t[1]
            dict['expect'] = temp2
            customer_data.append(dict)

        return customer_data

    @classmethod
    def query_customer(cls, param):
        pass


if __name__ == '__main__':
    print(Services.get_data_from_case(3,4))
