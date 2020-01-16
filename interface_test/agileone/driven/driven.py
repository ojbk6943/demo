#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
from interface_test.agileone.util.utility import Utility
from interface_test.agileone.testcase.knowledgehousetest import KnowledgeHouseTest

class Driven:
    def __init__(self,config_path):
        self.session = requests.session()
        content = Utility.read_json(config_path)
        self.base_url = content['protocol'] + content['host'] + content['port'] + content['program']
    def start(self,edit_notice_path,config_path,cookie_path):
        # 获取last_url
        cookie_info = Utility.read_json(cookie_path)
        login_url = self.base_url + cookie_info["login_url"]
        login_data = cookie_info['login_data']
        resp = self.session.post(login_url, login_data)
        from interface_test.agileone.testcase.noticetest import NoticeTest
        nt = NoticeTest()
        # nt.test_add_notice(self.session,self.base_url,add_notice_path)
        nt.test_edit_notice(self.session,self.base_url,edit_notice_path)

    def start1(self, query_knowledge_path):
        # 获取last_url
        cookie_info = Utility.read_json(query_knowledge_path)
        knowledge_url = self.base_url + cookie_info["query_knowledge_url"]
        KnowledgeHouseTest().test_query_knowledge(self.session,knowledge_url)

if __name__ == '__main__':

    driver = Driven('..\\config\\baseconfig')
    driver.start1('..\\testdata\\query_knowledge_data')