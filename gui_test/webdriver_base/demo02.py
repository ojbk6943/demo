#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 对页面元素的操作（找元素，操作元素）；对操作结果进行断言；对代码进行组织

from selenium import webdriver
from time import sleep
from random import randint
import time
import pymysql

driver = webdriver.Firefox()
# 隐式等待
driver.implicitly_wait(20)
driver.get('http://192.168.2.177/agileone/')
driver.maximize_window()

# 登录
uname = driver.find_element_by_id('username')
uname.click()
uname.clear()
uname.send_keys('admin')

upass = driver.find_element_by_id('password')
upass.click()
upass.clear()
upass.send_keys('admin')

driver.find_element_by_id('savelogin').click()

driver.find_element_by_id('login_manager').click()

# 公告管理

#driver.find_element_by_link_text('※ 公告管理 ※').click()
driver.find_element_by_partial_link_text('公告管理').click()

# 增加公告

headline = driver.find_element_by_id('headline')
headline.click()
headline.clear()
headline.send_keys('h1')

driver.find_element_by_class_name('ke-iframe').send_keys('hello')
driver.find_element_by_id('add').click()

# 编辑公告
sleep(2)
notice_total = driver.find_element_by_id('totalRecord').text
# css
# driver.find_element_by_css_selector('#dtrow_108 > td:nth-child(5) > label:nth-child(1)').click()
# driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div[2]/table[2]/tbody/tr[4]/td[5]/label[1]').click()
driver.find_element_by_xpath('//tbody[@id="dataPanel"]/tr[%d]/td[5]/label[1]'%(randint(1,int(notice_total)))).click()
# headline = driver.find_element_by_id('headline')
# headline.click()
# headline.clear()
sleep(3)

# 修改标题
headline = driver.find_element_by_id('headline')
old_headline_value = headline.get_attribute('value')
localtime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())
new_headline_value = localtime + old_headline_value
headline.click()
headline.clear()
headline.send_keys(new_headline_value)

# 修改内容
frame_ele = driver.find_element_by_class_name('ke-iframe')

# 切换入frame
driver.switch_to.frame(frame_ele)
old_notice_content = driver.find_element_by_xpath('/html/body').text
print(old_notice_content)
new_notice_content = localtime + old_notice_content
driver.find_element_by_xpath('/html/body').click()
driver.find_element_by_xpath('/html/body').clear()
driver.find_element_by_xpath('/html/body').send_keys(new_notice_content)

# # 切换回主窗口
driver.switch_to.default_content()
driver.find_element_by_id('edit').click()

# 删除任意的记录

driver.find_element_by_xpath('//tbody[@id="dataPanel"]/tr[%d]/td[5]/label[2]'%(randint(1,int(notice_total)))).click()
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()

# 查询
# 刷新页面
driver.refresh()
sleep(2)
noticeid = driver.find_element_by_id('noticeid')
# # noticeid.click()
# # noticeid.clear()
# # noticeid.send_keys('115')
# # driver.find_element_by_id('search').click()

conn = pymysql.connect('192.168.2.177','root','123456','agileone')
cur = conn.cursor()
sql = "select noticeid from notice"
cur.execute(sql)
rs = cur.fetchall()
rs_count = len(rs)
ran_number = randint(0,rs_count-1)
# 从数据库中随机获取一个noticeid
ran_noticeid = rs[ran_number][0]
noticeid.send_keys(ran_noticeid)
driver.find_element_by_id('search').click()

