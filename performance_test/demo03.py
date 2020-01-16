#!/usr/bin/env python
#-*- coding:utf-8 -*-


from locust import HttpLocust,TaskSet,task

# 继承任务套
class WoniuSalesTest(TaskSet):

    def open_page(self):
        self.client.get('/WoniuSales1.4/')

    def login(self):
        data = {'username':'admin','password':'admin','verifycode':'0000'}
        resp = self.client.post('/WoniuSales1.4/user/login',data,catch_response=True)
        if 'login-pass' == resp.text:
            resp.success()
        else:
            resp.failure('login-fail')

    def query_store(self):
        data = {'goodsserial': '', 'goodsname': '', 'barcode': '', 'goodstype': '', 'earlystoretime': '',
                'laststoretime': '', 'page': '1'}
        self.client.post('/WoniuSales1.4/query/stored',data)

    @task
    def doquery(self):
        self.open_page()
        self.login()
        self.query_store()

    @task
    def doadd_customer(self):
        pass

class WebSite(HttpLocust):
    task_set = WoniuSalesTest
    min_wait = 1000
    max_wait = 3000

