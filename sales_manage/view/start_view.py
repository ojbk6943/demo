#!/usr/bin/env python
#-*- coding:utf-8 -*-
from sales_manage.manager.users_manager import UsersManager
from sales_manage.view.main_menu_view import MainMenuView
class StartView:
    def __init__(self):
        self.um = UsersManager()
    def welcomeinfo(self):
        print('****************************')
        print('**欢迎使用蜗牛销售管理系统***')
        print('****************************')
    def input_uname(self):
        while 1:
            uname = input('请输入账号:')
            if self.um.check_uname(uname):
                return uname
            else:
                print('账号输入错误，请重新输入')
    def input_upass(self,uname):
        upass_errcount = 0
        while 1:
            if upass_errcount < 3:
                upass = input('请输入密码')
                if self.um.check_pass(uname, upass):
                    break
                else:
                    print('密码输入错误，请重新输入')
                    upass_errcount += 1
            else:
                print('密码错误次数过多，退出登录')
                exit(0)

    def input_verifycode(self):
        import random
        rand_number = random.randint(1000,9999)
        print('验证码显示为%d'%rand_number)
        while 1:
            verifycode = input('请输入以上四位数字之和：')
            if self.um.check_verifycode(rand_number, verifycode):
                break
            else:
                print('验证码输入错误，请重新输入')
    def login(self):
        self.welcomeinfo()
        uname = self.input_uname()
        self.input_upass(uname)
        self.input_verifycode()
        MainMenuView().show_main_menu(uname)
if __name__ == '__main__':
    StartView().login()


