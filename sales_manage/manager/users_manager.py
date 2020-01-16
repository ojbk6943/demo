#!/usr/bin/env python
#-*- coding:utf-8 -*-
from sales_manage.util.utility import Utility
class UsersManager:
    #检查用户名
    def check_uname(self,uname):
        sql = 'select * from users where uname="%s"' %(uname)
        result = Utility.query_one(sql)
        if result is not None:
            return True
        else:
            return False
    #检查密码
    def check_pass(self,uname,upass):
        sql = 'select upass from users where uname="%s"' %(uname)
        result = Utility.query_one(sql)
        if result[0] == upass:
            return True
        else:
            return False
     #检查验证码
    def check_verifycode(self,rand_number,verifycode):
        sum = 0
        for i in str(rand_number):
            sum += int(i)

        if str(sum) == verifycode:
            return True
        else:
            return False
    # 添加用户
    def add_users(self,uname,upass,realname):
        sql = 'insert into users(uname,upass,realname) values("%s","%s","%s");' %(uname,upass,realname)
        return Utility.update_db(sql)
    # 用户列表
    def list_users(self):
        sql = 'select uname,realname from users;'
        return Utility.query_all(sql)
    # 根据用户名查询该用户信息
    def query_user(self,uname):
        sql = 'select uname,upass,realname from users where uname="%s"' %(uname)
        return Utility.query_one(sql)