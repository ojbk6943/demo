#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests,time,threading

class AgileonePerformanceTest:

    def __init__(self):
        self.session = requests.session()
        self.count_char = 0

    def open_page(self):

        start_time = time.time()*1000
        open_page_resp = self.session.get('http://192.168.2.177/agileone/')
        end_time = time.time()*1000
        open_page_time = end_time - start_time
        content = open_page_resp.text
        print('%s打开页面的响应时间是%d' %(threading.currentThread().getName(),open_page_time))
        print('%s的吞吐量是%d个字符' %(threading.currentThread().getName(),content.__len__()))
        # 获得各个线程的总吞吐量
        self.count_char += content.__len__()
        print(self.count_char)



    def login(self):
        start_time = time.time() * 1000
        login_data = {'username':'admin','password':'admin','savelogin':False}
        login_resp = self.session.post('http://192.168.2.177/agileone/index.php/common/login',login_data)
        end_time = time.time() * 1000
        login_time = end_time - start_time


    def testcase(self):
        start_time = time.time() * 1000
        testcase_data = {"userstoryid":"3","type":"System-Test","status":"Proposed","priority":"Medium","headline":"测试11","content":"执行用例"}
        testcase_resp = self.session.post('http://192.168.2.177/agileone/index.php/testcase/add', testcase_data)
        end_time = time.time() * 1000
        login_time = end_time - start_time
        print(testcase_resp.text)


if __name__ == '__main__':

    at = AgileonePerformanceTest()
    start_time = time.time()*1000
    for i in range(1,6):
        thread = threading.Thread(target=at.open_page)
        thread.setName("第%d个用户"%i)
        # time.sleep(2)

        thread.start()
        thread.join()
    end_time = time.time()*1000
    dur_time = end_time - start_time
    print('当前的线程总吞吐量为%d个字符' %(at.count_char))
    print('总的吞吐率是%s字符/秒' %(at.count_char/dur_time*1000))

