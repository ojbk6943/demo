from seleniumauto import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(15)
driver.maximize_window()
driver.get(r'https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('蜗牛学院')
driver.find_element_by_id('su').click()
retext=driver.find_element_by_css_selector('div[id="content_left"]>div:nth-child(2)>h3')
woniutext=retext.text
print(woniutext)
if woniutext =='...西安|上海IT|Java|软件测试|Python开发培训学校|机构-蜗牛学院':
    print("检查正确")
else:
    print("#########################")
driver.quit()