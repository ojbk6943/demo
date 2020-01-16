# -*- coding: utf-8 -*-

# 从katalon Recorder中生成的代码

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        # 生成浏览器驱动对象
        self.driver = webdriver.Firefox()
        # 隐式等待
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        # 打开首页
        driver.get("http://192.168.6.222/agileone/")
        # 判断id为login的元素是否存在
        self.assertTrue(self.is_element_present(By.ID, "login_manager"))
        # 输入用户名
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        #输入密码
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_id("savelogin").click()
        # 点击登录按钮
        driver.find_element_by_id("login_manager").click()
        # 点击公告管理链接
        driver.find_element_by_link_text(u"※ 公告管理 ※").click()
        # 输入标题
        driver.find_element_by_id("headline").click()
        driver.find_element_by_id("headline").clear()
        driver.find_element_by_id("headline").send_keys("f")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath("//html").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # 点击添加公告按钮
        driver.find_element_by_id("add").click()
        # 点击右侧的编辑按钮
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='admin'])[1]/following::label[1]").click()
        # 点击编辑保存按钮
        driver.find_element_by_id("edit").click()
        self.accept_next_alert = True
        # 点击删除按钮
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='编辑'])[1]/following::label[1]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定要删除该条记录吗[\s\S]$")
        # 点击注销链接
        driver.find_element_by_link_text(u"注销").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            # 该代码已过时
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
