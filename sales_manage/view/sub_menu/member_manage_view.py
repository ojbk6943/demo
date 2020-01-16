#!/usr/bin/env python
#-*- coding:utf-8 -*-
from sales_manage.manager.members_manager import MembersManager
from sales_manage.util.utility import Utility


class MemberManageView:
    def __init__(self):
        self.mm = MembersManager()
    def show_manage_members_view(self):

        d = {"1": self.add_members_view, '2': self.update_members_view,
             '3': self.delete_members_view, '4': self.query_members_view, '5': self.list_members_view}
        while 1:
            print('*客户管理*')
            print('1.添加客户')
            print('2.修改客户信息')
            print('3.删除客户')
            print('4.查询客户')
            print('5.会员列表')
            print('6.返回上一级')
            choice = input('请选择：')
            d[choice]()
    def add_members_view(self):
        add_count=0
        while 1:
                cphone = input('请输入电话号码：')
                result = self.mm.check_cphone(cphone)
                if result is not None:
                    print('该号码已存在，请重新输入')
                else:
                    break
        cname = input('请输入姓名')
        csex = input('请输入性别（男/女）')
        cdate = input('请输入出生日期：')
        uname_now=input('请输入当前的用户名：')
        uid = self.mm.get_uid(uname_now)[0]
        if self.mm.add_customer(cphone,cname,csex,cdate,uid):
            print('会员添加成功')
        else:
            print('会员添加失败')

    def update_members_view(self,uname):
        pass

    def delete_members_view(self,uname):
        pass

    def query_members_view(self,uname):
        pass

    def list_members_view(self):
        members_data=self.mm.list_customer()
        for members in members_data:
            print(members)
