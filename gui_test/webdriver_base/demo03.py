#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
from gui_test.webdriver_base.util import Utility
from random import randint

class AgileoneTest:

    # 准备
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

    # 登录操作
    def login(self,username,password):

        driver = self.driver

        uname = driver.find_element_by_id('username')
        uname.click()
        uname.clear()
        uname.send_keys(username)

        upass = driver.find_element_by_id('password')
        upass.click()
        upass.clear()
        upass.send_keys(password)

        driver.find_element_by_id('savelogin').click()

        driver.find_element_by_id('login_manager').click()

    # 登录结果验证
    def verify_login(self,username,password):

        from selenium.webdriver.common.by import By
        self.login(username,password)
        if self.is_element_present(By.PARTIAL_LINK_TEXT,'注销'):
            print('登录成功')
        elif '出错啦' in self.driver.find_element_by_id('msg').text:
            print('登录失败')
        else:
            pass

    # 添加公告操作
    def add_notice(self,notice_headline,notice_content):
        driver = self.driver
        # 1.调用登录方法 2.使用cookie
        self.login('admin','admin')
        driver.find_element_by_partial_link_text('公告管理').click()

        headline = driver.find_element_by_id('headline')
        headline.click()
        headline.clear()
        headline.send_keys(notice_headline)

        driver.find_element_by_class_name('ke-iframe').send_keys(notice_content)
        driver.find_element_by_id('add').click()
        time.sleep(3)
    # 添加公告结果验证
    def verify_add_notice(self,notice_headline,notice_content,db_info):
        driver = self.driver
        self.login('admin','admin')
        driver.find_element_by_partial_link_text('公告管理').click()
        old_total = driver.find_element_by_id('totalRecord').text
        sql = 'select count(noticeid) from notice'
        old_result = Utility.query_one(db_info, sql)
        self.logout()
        self.add_notice(notice_headline,notice_content)

        info_flag = False
        if '成功'  in driver.find_element_by_id('msg').text :
            print('添加公告成功信息正确')
            info_flag = True
        else:
            print('添加公告成功信息不正确')

        driver.refresh()

        new_total = driver.find_element_by_id('totalRecord').text
        if int(new_total) != int(old_total) :
            print('列表中增加了公告')
        else:
            print('列表中没有增加公告')

        new_result = Utility.query_one(db_info,sql)
        if new_result[0] - old_result[0] == 1:
            print('数据库中添加了新的公告信息')
        else:
            print('数据库中没有添加公告信息')

    # 编辑公告操作
    def edit_notice(self):
        driver = self.driver
        self.login('admin', 'admin')
        driver.find_element_by_partial_link_text('公告管理').click()
        notice_total = driver.find_element_by_id('totalRecord').text
        driver.find_element_by_xpath('//tbody[@id="dataPanel"]/tr[%d]/td[5]/label[1]'
                                     %(randint(1,int(notice_total)))).click()
        time.sleep(2)
        old_notice_headline = driver.find_element_by_id('headline').get_attribute('value')
        new_notice_headline = Utility.get_time() + old_notice_headline
        driver.switch_to.frame(driver.find_element_by_class_name('ke-iframe'))
        old_notice_content = driver.find_element_by_xpath('/html/body').text

        new_notice_content = Utility.get_time() + old_notice_content
        driver.find_element_by_xpath('/html/body').click()
        driver.find_element_by_xpath('/html/body').clear()
        driver.find_element_by_xpath('/html/body').send_keys(new_notice_content)
        driver.switch_to.default_content()
        driver.find_element_by_id('headline').click()
        driver.find_element_by_id('headline').clear()
        driver.find_element_by_id('headline').send_keys(new_notice_headline)
        driver.find_element_by_id('edit').click()

    # 编辑公告结果验证
    def verify_edit_notice(self):
        self.edit_notice()
    # 删除公告操作

    # 删除公告验证

    # 查询公告操作

    # 查询公告验证

    # 退出登录操作
    def logout(self):
        self.driver.find_element_by_partial_link_text('注销').click()
if __name__ == '__main__':
    at = AgileoneTest('Firefox','http://192.168.2.177/agileone/')
    # at.verify_login('admin','admin')
    # at.verify_add_notice('test01','hello',('192.168.2.177','root','123456','agileone'))
    at.edit_notice()