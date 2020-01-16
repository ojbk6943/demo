#!/usr/bin/env python
#-*- coding:utf-8 -*-

def fun1(x,y,z):

    if x>0 or y>0:
        result = 1
        if z >= 10:
            result = 2
    else:
        result = 3

    return result

def login(uname,upass):
    if uname == 'admin' and upass== '123':
        return 'login-pass'
    else:
        return 'login-fail'

def do_login():
    uname = input('请输入账号')
    upass = input('请输入密码')
    # 密码输入错误次数超过3次即退出系统

if __name__ == '__main__':

    # x = 1,x=0;z=10,z=9
    # x = 1,z=10,y = 0
    # x = 1,z = 9,y = 0
    # x = 0,z = 10,y = 0
    # x = 0,z = 9, y = 0
    # 语句覆盖（最低要求） 路径覆盖（目标）
    result1 = fun1(1,0,10)
    result2 = fun1(1,0,9)
    result3 = fun1(0,0,10)

    print(result1,result2,result3)