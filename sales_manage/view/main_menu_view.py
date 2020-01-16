#!/usr/bin/env python
#-*- coding:utf-8 -*-
from sales_manage.view.sub_menu.member_manage_view import MemberManageView
from sales_manage.view.sub_menu.sell_view import SellView
from sales_manage.view.sub_menu.users_manage_view import UsersManageView
class MainMenuView:
    def  __init__(self):
        pass
    def show_main_menu(self,uname):
        while 1:
            print('**********************')
            print('1.销售出库')
            print('2.商品入库')
            print('3.库存查询')
            print('4.会员管理')
            print('5.用户管理')
            print('6.退出登录')
            print('**********************')
            d = {"1":SellView().show_sale_menu,'2':self.show_goods_instore,
                 '3':self.show_query_store,'4':MemberManageView().show_manage_members_view,
                 '5':UsersManageView().show_manage_users_view}
            choice = input('请选择：')
            d[choice]()
            # fun = self.d[choice]
            # # 通过字符串反射到类的方法
            # show_menu = getattr(MainMenuView(),fun)
            # show_menu()

    def show_goods_instore(self):
        print('*商品入库*')
    def show_query_store(self):
        print('库存查询')
if __name__ == '__main__':
    MainMenuView().show_main_menu(uname='admin')
