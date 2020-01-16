#!/usr/bin/env python
#-*- coding:utf-8 -*-

from interface_test.agileone.util.utility import Utility
from interface_test.agileone.common.notice import Notice
import re

class NoticeTest:

    def test_add_notice(self,session,base_url,add_notice_path):
        # 获得测试数据
        json_notice_info = Utility.read_json(add_notice_path)
        for notice_info in  json_notice_info:
            add_notice_url = base_url + notice_info[0]
            add_notice_data = notice_info[1]
            add_notice_resp = Notice().add_notice(session,add_notice_url,add_notice_data)
            print(add_notice_resp.text)
            if re.match('\\d+',add_notice_resp.text):   #检查返回的编码是不是数字
                actual = "add notice success"
            else:
                actual = "add notice fail"

            flag = Utility.assertequal(notice_info[2],actual)
            if flag:
                print('add notice test success')
            else:
                print('add notice test fail')




    def test_edit_notice(self,session,base_url,edit_notice_path):
        # 数据库中随机找到一条notice信息，记录其编号、标题和内容
        sql = "select * from notice"
        notice_result = Utility.query_all(sql)
        rand_index = Utility.get_random(len(notice_result)-1)
        old_notice_info = notice_result[rand_index]
        noticeid = old_notice_info[0]
        old_notice_headline = old_notice_info[1]
        old_notice_content = old_notice_info[2]
        notice_date = str(old_notice_info[4])

        # 修改其标题和内容，点击编辑，记录新数据
        new_notice_headline = old_notice_headline + str(Utility.get_random(start=100,end=999))
        new_notice_content = old_notice_content + str(Utility.get_random(start=100,end=999))
        json_edit_notice_info = Utility.read_json(edit_notice_path)
        edit_notice_url = base_url + json_edit_notice_info['edit_notice_url']
        new_notice_data = {"noticeid":noticeid,"headline":new_notice_headline,
                           "content":new_notice_content,"scope":"1","expireddate":notice_date}
        edit_notice_resp = Notice().edit_notice(session,edit_notice_url,new_notice_data)
        # 判断新内容和旧内容是否相同
        sql = 'select headline,content from notice where noticeid=%d' %(noticeid)
        edit_notice_result = Utility.query_one(sql)

        if edit_notice_result[0] == new_notice_headline and edit_notice_result[1] ==\
                new_notice_content and edit_notice_resp.text == "1":

            actual = 'edit notice success'
        else:
            actual = 'edit notice fail'

        print(json_edit_notice_info['expect'])
        flag = Utility.assertequal(json_edit_notice_info['expect'],actual)
        if flag :
            print('edit notice test success')
        else:
            print('edit notice test fail')

    def test_query_notice(self):
        pass

    def test_delete_notice(self):
        pass

if __name__ == '__main__':
    nt = NoticeTest()
    nt.test_edit_notice()