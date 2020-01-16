#!/usr/bin/env python
#-*- coding:utf-8 -*-

from interface_test.woniusales_test.util.utility import Utility

class TestData:

    @classmethod
    def get_customer_data(cls, path, sheet_name,url, j, k ,type):
        result = Utility.read_xls(path, sheet_name)
        customer_info = []
        for i in range(1, result.nrows):

            case_type = result.cell(i,0).value

            if type in case_type:
                customer_data = []
                temp1 = result.cell(i, j).value
                temp2 = result.cell(i, k).value
                temp3 = result.cell(i, url).value
                li = temp1.split('\n')
                dict = {}
                for info in li:
                    t = info.split('=')
                    dict[t[0]] = t[1]
                customer_data.append(temp3)
                customer_data.append(dict)
                customer_data.append(temp2)
                customer_info.append(customer_data)

        return customer_info





if __name__ == '__main__':
    customer_data = TestData.get_customer_data('..\\testdata\\woniusales_test_data.xlsx','customer',2,4,6,'QUERY')
    print(customer_data)