#!/usr/bin/env python
#-*- coding:utf-8 -*-

# webdriver高级功能的使用
from selenium import webdriver
import time
# 显式等待

def webdriver_wait():
    from selenium.webdriver.support.ui import WebDriverWait
    driver = webdriver.Firefox()
    # driver.implicitly_wait(20)
    driver.get('http://www.sohu.com.cn/')
    driver.maximize_window()
    WebDriverWait(driver,10,0.5).until(lambda driver:driver.find_element_by_xpath('//div[@id="search"]/span')).click()
    # driver.find_element_by_xpath('//div[@id="search"]/span').click()

# 文件上传
def upload():
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)

    driver.get('http://192.168.2.20:8080/WoniuSales/')
    driver.maximize_window()
    driver.add_cookie({'name': 'username', 'value': 'admin'})
    driver.add_cookie({'name': 'password', 'value': 'admin'})
    driver.get('http://192.168.2.20:8080/WoniuSales/goods')
    # driver.find_element_by_partial_link_text('批次管理').click()
    # driver.find_element_by_id('batchfile').send_keys('H:\\test\\test1.txt')

# 切换windows窗口
def switch_window():
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.get('http://www.woniuxy.com/')
    time.sleep(3)
    driver.find_element_by_partial_link_text('前端').click()
    driver.f
    time.sleep(3)
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_partial_link_text('关于蜗牛').click()
    time.sleep(3)
    print(driver.window_handles)
    # driver.find_element_by_partial_link_text('关于蜗牛').click()

# 鼠标键盘的使用
def click_right():
    from selenium.webdriver.common.action_chains import ActionChains
    # from selenium.webdriver.common.keys import Keys

    driver = webdriver.Ie()
    driver.implicitly_wait(20)
    driver.get('http://192.168.2.20:8080/WoniuSales/')
    ele = driver.find_element_by_partial_link_text('商品入库')
    ActionChains(driver).context_click(ele).perform()
    time.sleep(2)
    ele.send_keys('t')


def move_to_ele():
    from selenium.webdriver.common.action_chains import ActionChains
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.get('http://www.woniuxy.com/')
    ele = driver.find_element_by_partial_link_text('Java全栈开发')
    ActionChains(driver).move_to_element(ele).perform()
    driver.find_element_by_css_selector('#major-detail-1 > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > a:nth-child(1)').click()


# 截图
def get_img():
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.get('http://192.168.2.20:8080/WoniuSales/')
    from gui_test.webdriver_base.util import Utility
    # now = Utility.get_time()
    # driver.get_screenshot_as_file('image\\'+now+'error.png')
    s = driver.get_screenshot_as_png()
    print(s)

# 注入js代码
def excute_javascript():
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.get('http://192.168.2.20:8080/WoniuSales/')
    driver.add_cookie({'name': 'username', 'value': 'admin'})
    driver.add_cookie({'name': 'password', 'value': 'admin'})
    driver.get('http://192.168.2.20:8080/WoniuSales/')
    driver.find_element_by_partial_link_text('会员管理').click()
    childdate_ele = driver.find_element_by_id('childdate')
    #document.getElementById('childdate').readonly=false;
    driver.execute_script('document.getElementById("childdate").readOnly=false;')
    childdate_ele.clear()
    childdate_ele.send_keys('2005-01-01')


if __name__ == '__main__':
    # webdriver_wait()
    # upload()
    # switch_window()
    # click_right()
    # get_img()
    excute_javascript()