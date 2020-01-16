#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Demo02:

    def login(self):

        while 1:
            uname = input('请输入用户名：')
            if uname == 'admin':
                print('用户名输入正确')
                break
            else:
                print('用户名输入错误，请重新输入')

        pass_errcount = 0
        while 1:
            if pass_errcount < 3:
                upass = input('请输入密码：')
                if upass == '123':
                    print('密码输入正确')
                    break
                else:
                    pass_errcount += 1
                    print('密码输入错误，请重新输入')
            else:
                print('密码错误次数过多，退出登录')
                exit(0)

        print('欢迎登录！')

if __name__ == '__main__':
    Demo02().login()
    # admin,123
    # admin1,admin,123
    # admin,223,123
    # admin,223,323,323

    # admin1,admin,223,123
    # admin,223,323,323

