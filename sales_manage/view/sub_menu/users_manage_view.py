#!/usr/bin/env python
#-*- coding:utf-8 -*-
from sales_manage.manager.users_manager import UsersManager
class UsersManageView:

    def __init__(self):
        self.um = UsersManager()

    def show_manage_users_view(self):
        d = {"1":self.add_users_view,'2':self.update_users_view,
             '3':self.delete_users_view,'4':self.query_users_view,'5':self.list_users_view}
        while 1:
            print('*用户管理*')
            print('1.添加用户')
            print('2.修改用户信息')
            print('3.删除用户')
            print('4.查询用户')
            print('5.用户列表')
            print('6.返回上一级')
            choice = input('请选择：')
            d[choice]()


    def add_users_view(self):
        while 1:
            new_uname = input('请输入用户名：')
            if self.um.check_uname(new_uname):
                print('该用户已存在，请重新输入')
            else:
                break
        new_upass = input('请输入密码：')
        new_realname = input('请输入您的真实姓名:')
        if self.um.add_users(new_uname,new_upass,new_realname):
            print('添加用户成功')
        else:
            print('添加用户失败')


    def update_users_view(self):
        pass

    def delete_users_view(self):
        pass

    def query_users_view(self):
        uname = input('请输入您要查询的用户名：')
        result = self.um.query_user(uname)
        if result is not None:
            print('用户名\t真实姓名')
            print(result[0],result[1],result[2])
        else:
            print('该用户不存在')

    def list_users_view(self):
        result = self.um.list_users()
        print('用户名\t真实姓名')
        for user in result:
            print(user[0],user[1])

