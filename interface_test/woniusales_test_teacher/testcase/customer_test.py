#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest,requests
from parameterized import parameterized
from interface_test.woniusales_test.util.utility import Utility
from interface_test.woniusales_test.testcase.test_data import TestData
from interface_test.woniusales_test.common.customer import Customer

add_customer_info = TestData.get_customer_data('..\\testdata\\woniusales_test_data.xlsx','customer',2,4,6,'ADD')
query_customer_info = TestData.get_customer_data('..\\testdata\\woniusales_test_data.xlsx','customer',2,4,6,'QUERY')

class CustomerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):

        self.session = requests.session()

        # 获取基本的url
        content = Utility.read_json("..\\config\\baseconfig")
        self.base_url = content['protocol'] + content['host'] + content['port'] + content['program']

        # 获取cookie信息
        cookie_info = Utility.read_json("..\\config\\cookieconfig")

        login_url = self.base_url + cookie_info['login_url']
        login_data = cookie_info['login_data']
        resp = self.session.post(login_url,login_data)


    def tearDown(self):
        pass

    @parameterized.expand(add_customer_info)
    def test_add_customer(self,add_customer_url,add_customer_data,expect):
        add_customer_resp = Customer().add_customer(self.session,add_customer_url,add_customer_data)
        self.assertEqual(add_customer_resp.text,expect)

    # def test_edit_customer(self):
    #     pass
    #
    @parameterized.expand(query_customer_info)
    def test_query_customer(self,query_customer_url,query_customer_data,expect):

        # sql = "select * from customer"
        # rs = Utility.query_all(sql)
        # customer_info = rs[Utility.get_random(len(rs)-1)]
        # query_customer_data['customerphone'] = customer_info[1]
        query_customer_resp = Customer().query_customer(self.session,query_customer_url,query_customer_data)
        query_result = query_customer_resp.json()

        try:
            if query_result[0]['customerphone'] == query_customer_data['customerphone']:
                actual = 'query_success'
        except:
            actual = 'query_null'

        self.assertEqual(actual,expect)



if __name__ == '__main__':

    unittest.main(verbosity=2)
