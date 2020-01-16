from parameterized import parameterized
from selenium.webdriver.common.by import By
from gui_test.webdriver_base.woniusales_test import WoniuSalesTest
from gui_test.woniusales_test.util.services import Services
from gui_test.woniusales_test.util.utility import Utility
from time import sleep
from interface_test.woniusales_requests_test.common.customer_manager import CustomerManager
import unittest
from random import randint
import json
import pymysql
import requests
#准备数据
# with open("..\\test_data\\add_testdata",encoding="utf8") as file:
#     add_test_data = json.load(file)
add_test_data=Utility.read_json("..\\test_data\\add_testdata")
class Customer_Manager_case(unittest.TestCase):
    def setUp(self):
        self.session = requests.session()
        self.base_config_data=Utility.read_json("..\\config\\base_config")
        self.cookie_data =Utility.read_json("..\\config\\cookie_config")
        self.base_url=self.base_config_data["protocol"]+\
           self.base_config_data["host"]+self.base_config_data["port"]+self.base_config_data["program"]
        login_url=self.base_url+self.cookie_data[0][0]
        login_data=self.cookie_data[0][1]
        resp_login = self.session.post(login_url, login_data)
    @parameterized.expand(add_test_data)
    def test_add_customer(self,add_last_url,test_data,expect):
        add_url=self.base_url+add_last_url
        resp_add=CustomerManager().add(self.session,add_url,test_data)

        print(resp_add.text)
        if str(resp_add.text)=="add-successful":
            actual="add-successful"
        else:
            actual = "add-fail"
        self.assertEqual(expect,actual)
        # print(resp_add.text)






if __name__ == '__main__':
    unittest.main()





