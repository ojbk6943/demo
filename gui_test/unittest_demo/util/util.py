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
    def read_from_txt(cls,path):
        with open(path) as file:
            contents = file.readlines()
        return contents

    @classmethod
    def trans_to_tuple(cls,path):
        contents = Utility.read_from_txt(path)
        li = []
        for content in contents:
            list = content.strip().split(',')
            tup = (list[0],list[1],list[2])
            li.append(tup)
        return li

    @classmethod
    def trans_to_json(cls,path):
        contents = Utility.read_from_txt(path)
        li = []
        for content in contents:
            list = content.strip().split(',')
            dict = {'username':list[0],'password':list[1],'expect':list[2]}
            li.append(dict)
        return li

    @classmethod
    def get_time(cls):
        import time
        return time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())



if __name__ == '__main__':
    # print(Utility.query_one(('192.168.2.177','root','123456','agileone'),'select address from customer'))
    # print(Utility.get_time())
    # Utility.get_kookies()
    # contents = Utility.read_from_txt('../test_data/login_data.txt')
    # print(contents)
    li = Utility.trans_to_json('../test_data/login_data.txt')
    print(li)