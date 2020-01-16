#!/usr/bin/env python
#-*- coding:utf-8 -*-
from sales_manage.util.utility import Utility


class MembersManager:
    #检查电话号码是否已经存在
    def check_cphone(self,cphone):
        sql = 'select * from customer where cphone="%s"' %cphone
        return Utility.query_one(sql)
    #获取uname的uid
    def get_uid(self,uname):
        sql = 'select uid from users where uname="%s"' %uname
        return Utility.query_one(sql)
    #增加会员
    def add_customer(self,cphone,cname,csex,cdate,uid):
        sql = 'insert into customer(cphone,cname,csex,cdate,uid) ' \
              'values("%s","%s","%s","%s",%d)'%(cphone,cname,csex,cdate,uid)

        return Utility.update_db(sql)
    #会员列表
    def list_customer(self):
        sql='select cname,cphone from customer'
        customer_result=Utility.query_all(sql)
        return customer_result