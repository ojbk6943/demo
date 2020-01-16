#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Utility:

    @classmethod
    def get_db_info(cls):

        contents = cls.read_json('..\\config\\baseconfig')
        db_info = {'DB_HOST':contents['DB_HOST'],'DB_USERNAME':contents['DB_USERNAME'],
                      'DB_PASSWORD':contents['DB_PASSWORD'],'DB_NAME':contents['DB_NAME']}
        return db_info

    @classmethod
    def conndb(cls,charset='utf8'):
        import pymysql
        db_info = cls.get_db_info()
        return pymysql.connect(db_info['DB_HOST'],db_info['DB_USERNAME'],
                               db_info['DB_PASSWORD'],db_info['DB_NAME'],charset='utf8')

    # 查询一条记录
    @classmethod
    def query_one(cls,sql):
        db_info = cls.get_db_info()
        conn = Utility.conndb(db_info)
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result

    # 查询多条记录
    @classmethod
    def query_all(cls,sql):
        db_info = cls.get_db_info()
        conn = Utility.conndb(db_info)
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    # 更新数据库操作
    @classmethod
    def update_db(cls,sql):
        db_info = cls.get_db_info()
        conn = Utility.conndb(db_info)
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

    # 从文本中读取数据
    @classmethod
    def read_txt(cls,path):
        with open(path) as file:
            contents = file.readlines()

        return contents

    # 执行截图操作
    @classmethod
    def get_png(cls,driver,path):
        driver.get_screenshot_as_file(path+cls.get_time()+'error.png')

    # 从excel中返回
    @classmethod
    def read_xls(cls,path):
        import xlrd
        book = xlrd.open_workbook(path)

    # 从json中获取json格式的内容
    @classmethod
    def read_json(cls,path):
        import json
        with open(path) as file:
            contents = json.load(file)
        return contents

    # 获取一定范围内的随机整数
    @classmethod
    def get_random(cls,end,start=0):
        from random import randint
        return randint(start,end)

    # 从excel中读取内容
    @classmethod
    def read_xls(cls,path,sheet_name):
        import xlrd
        book = xlrd.open_workbook(path)
        return book.sheet_by_name(sheet_name)



    # 断言两个值是否相同
    @classmethod
    def assertequal(cls,expect,actual):
        if expect == actual:
            return True
        else:
            return False



if __name__ == '__main__':
    # sql = 'select * from user'
    # result = Utility.query_all(sql)
    # print(result)
    # Utility.get_db_info()
    # Utility.get_db_info()
    # result = Utility.read_xls('..\\test_data\\woniusales_test_cases.xlsx','customermanager')
    # 所有行
    # for i in range(result.nrows):
    #     for j in range(result.ncols):
    #        print(result.cell(i,j).value,end='\t')
    #     print()
    contents = Utility.read_json('..\\testdata\\add_notice_data')
    print(contents)