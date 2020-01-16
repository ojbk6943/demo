#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests,time,threading

class AgileonePerformanceTest:

    def __init__(self):
        self.session = requests.session()
        self.count_char = 0
        self.all_time = 0

    def open_page(self):


        open_page_resp = self.session.get('http://192.168.2.177/agileone/')
        content = open_page_resp.text
        if 'AgileOne - Welcome to Login' in content:
            # 获得各个线程的总吞吐量
            self.count_char += content.__len__()
        else:
            print('%s打开页面失败' %(threading.currentThread().getName()))


    def login(self):

        login_data = {'username':'admin','password':'admin','savelogin':False}
        login_resp = self.session.post('http://192.168.2.177/agileone/index.php/common/login',login_data)
        if login_resp.text == 'successful':
            self.count_char += login_resp.text.__len__()
        else:
            print('%s登录失败' %(threading.currentThread().getName()))

    def testcase(self):
        import random,re
        rand_number = random.randint(10000,99999)
        testcase_data = {"userstoryid":"3","type":"System-Test","status":"Proposed","priority":"Medium","headline":"测试%d"%(rand_number),"content":"执行用例"}
        testcase_resp = self.session.post('http://192.168.2.177/agileone/index.php/testcase/add', testcase_data)
        if re.match('\\d+',testcase_resp.text):
            self.count_char += testcase_resp.text.__len__()

    def logout(self):
        self.session.get('http://192.168.2.177/agileone/index.php/common/logout')

    def case(self):
        start_time = time.time()*1000
        self.open_page()
        time.sleep(1)
        self.login()
        time.sleep(2)
        self.testcase()
        time.sleep(1)
        self.logout()
        end_time = time.time()*1000
        dur_time = end_time - start_time
        self.all_time += dur_time



if __name__ == '__main__':

    at = AgileonePerformanceTest()
    for i in range(1,6):

        thread = threading.Thread(target=at.case)
        thread.setName("第%d个用户"%i)

        thread.start()
        thread.join()

    print('当前的线程总吞吐量为%d个字符' %(at.count_char))
    print('总的吞吐率是%s字符/秒' %(at.count_char/at.all_time*1000))
    print('用户的平均响应时间为%f秒' %(at.all_time/5/1000))

