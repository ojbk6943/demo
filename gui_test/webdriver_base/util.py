#!/usr/bin/env python
#-*- coding:utf-8 -*-

#  该类包含一系列的公用工具

class Utility:

    @classmethod
    def conndb(cls,host,username,password,dbname,charset='utf8'):
        import pymysql
        return pymysql.connect(host,username,password,dbname,charset='utf8')

    # 查询一条记录
    @classmethod
    def query_one(cls,db_info,sql):
        conn = Utility.conndb(db_info[0],db_info[1],db_info[2],db_info[3])
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result

    # 查询多条记录
    @classmethod
    def query_all(cls,db_info,sql):
        conn = Utility.conndb(db_info[0],db_info[1],db_info[2],db_info[3])
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    # 更新数据库操作
    @classmethod
    def update_db(cls,db_info,sql):
        conn = Utility.conndb(db_info[0], db_info[1], db_info[2], db_info[3])
        cur = conn.cursor()
        flag = False
        try:
            cur.execute(sql)
            conn.commit()
            flag = True
        finally:
            cur.close()
            conn.close()
            return flag


    @classmethod
    def get_time(cls):
        import time
        return time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())

    @classmethod
    def get_kookies(cls):
        from selenium import webdriver
        driver = webdriver.Firefox()
        driver.get('http://192.168.2.177/agileone/')
        driver.add_cookie({'name':'username','value':'admin'})
        driver.add_cookie({'name':'password','value':'admin'})
        driver.add_cookie({'name':'PHPSESSID','value':'dc81146196d5c2a616cabac77c46a8c4'})
        driver.get('http://192.168.2.177/agileone/')


if __name__ == '__main__':
    # print(Utility.query_one(('192.168.2.177','root','123456','agileone'),'select address from customer'))
    # print(Utility.get_time())
    # Utility.get_kookies()
    import os
    print(os.path.abspath(''))