from selenium.webdriver.common.by import By

from gui_test.webdriver_base.woniusales_test import WoniuSalesTest
from gui_test.woniusales_test.util.services import Services
from gui_test.woniusales_test.util.utility import Utility
from time import sleep
from gui_test.woniusales_test.common.customer_manager import CustomerManager
import unittest
from random import randint
import json
import pymysql
class Customer_Manager_Test(unittest.TestCase):
    # @classmethod
    def setUp(self):
        self.cus=CustomerManager()
        self.customer_data = Services.get_data_from_case(3, 4)
        # pass

    def  test_add_customer(self):

        #准备会员数据
        # customer_data = Services.get_data_from_case(3, 4)
        #加载数据 调起方法测试

        path = '..\\config\\base_config'
        with open(path) as file:
            contents = json.load(file)

        driver = Services.get_driver(contents['BROWSER'], contents['URL'])
        Services.add_woniusales_cookie(driver, contents['URL'])
        Services.click_ele(driver, 'LINK', '会员管理')

        for customer_info in self.customer_data:
        # for customer_info in customer_data:
            sql = 'select count(customerid) from customer'
            old_customer_count = Utility.query_one(sql)
            # self.cus.add_customer(driver, customer_info)
            self.cus.add_customer(driver, customer_info)

            # driver.refresh()
            sleep(2)
            new_customer_count = Utility.query_one(sql)
            if int(new_customer_count[0]) - int(old_customer_count[0]) == 1:
                actual = 'add-successful'
            else:
                if Services.is_element_present(driver, By.XPATH, '/html/body/div[7]/div/div/div[2]/div'):
                    alert_ele = Services.find_ele(driver, 'XPATH', '/html/body/div[7]/div/div/div[2]/div')
                    if alert_ele.text == '该客户信息已经存在，请勿重复添加.':
                        actual = 'already-added'
                    elif alert_ele.text == '请输入客户的电话号码.':
                        actual = 'add-failed'
                    else:
                        pass
                    driver.refresh()
                else:
                    actual = 'add-failed'
            self.assertEqual(customer_info['expect'], actual)
            driver.close()



    def test_query_customer(self):


        #从json中读取数据库配置信息
        import json
        path='..\\config\\base_config'
        with open(path) as file:
            contents = json.load(file)

        #将获取到的信息放入字典
        db_info = {'DB_HOST': contents['DB_HOST'], 'DB_USERNAME': contents['DB_USERNAME'],
                   'DB_PASSWORD': contents['DB_PASSWORD'], 'DB_NAME': contents['DB_NAME'],
                   'DB_BROWSER':contents['BROWSER'],'DB_URL':contents['URL']}
        # print(db_info)
        #随机获取一个数据库中的电话old_phone
        db=pymysql.connect(db_info['DB_HOST'], db_info['DB_USERNAME'],db_info['DB_PASSWORD'],
                           db_info['DB_NAME'], charset='utf8')
        # for
        cur=db.cursor()
        sql = 'select customerphone from customer'
        cur.execute(sql)
        phones=cur.fetchall()
        #phones是个以元组为元素的列表

        random_phone_index = randint(0, len(phones) - 1)
        old_phone=phones[random_phone_index][0]

        #登录系统开始测试
        driver = Services.get_driver(db_info['DB_BROWSER'], db_info['DB_URL'])
        Services.add_woniusales_cookie(driver, db_info['DB_URL'])
        Services.click_ele(driver, 'LINK', '会员管理')
        Services.input(driver, 'ID', 'customerphone', old_phone)
        sleep(2)
        Services.click_ele(driver,'SELECTOR','button.form-control:nth-child(3)')
        sleep(2)
        #断言
        if Services.is_element_present(driver,By.LINK_TEXT, '修改'):
            customer_phone = driver.find_element_by_xpath('//tbody[@id="customerlist"]/tr/td[2]').text

            if int(customer_phone)==int(old_phone):
                 actual='query-successful'
            else:
                actual = 'query-failed'

        else:
            actual = 'query-failed'

        self.assertEqual('query-failed',actual)
        driver.close()
    def test_edit_customer(self):
        path = '..\\config\\base_config'
        with open(path) as file:
            contents = json.load(file)
        print(contents)
        driver = Services.get_driver(contents['BROWSER'], contents['URL'])
        Services.add_woniusales_cookie(driver, contents['URL'])
        Services.click_ele(driver, 'LINK', '会员管理')
        sleep(2)

        # 从数据库查询一条随机的电话号码
        db = pymysql.connect(contents['DB_HOST'], contents['DB_USERNAME'],
                             contents['DB_PASSWORD'],contents['DB_NAME'],
                               charset='utf8')
        cur = db.cursor()
        sql = 'select customerphone from customer'
        cur.execute(sql)
        phones = cur.fetchall()
        # phones是个以元组为元素的列表

        random_phone_index = randint(0, len(phones) - 1)
        randint_phone = phones[random_phone_index][0]

        path = '..\\test_data\\edit_info'
        with open(path) as file:
            contents = json.load(file)
        #调用方法,修改客户信息
        CustomerManager().edit_customer(driver,contents,randint_phone)
        sleep(2)
        #断言
        if Services.is_element_present(driver,By.CSS_SELECTOR,
                                   '.modal-sm > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)'):
                actual = 'edit-pass'
        else:
                actual = 'edit-fail'
        self.assertEqual('edit-pass',actual)
        driver.close()





if __name__ == '__main__':
    unittest.main()
# a=Customer_Manager_Test()
    # a.test_query_customer()
# a.test_add_customer()
    # a.test_edit_customer()




