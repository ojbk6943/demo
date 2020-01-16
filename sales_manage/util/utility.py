#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Utility:

    # 从json中获取json格式的内容
    @classmethod
    def read_json(cls, path):
        import json
        with open(path) as file:
            contents = json.load(file)
        return contents

    @classmethod
    def get_db_info(cls):

        contents = cls.read_json('..\\config\\base_config')
        db_info = {'DB_HOST': contents['DB_HOST'], 'DB_USERNAME': contents['DB_USERNAME'],
                   'DB_PASSWORD': contents['DB_PASSWORD'], 'DB_NAME': contents['DB_NAME']}
        return db_info

    @classmethod
    def conndb(cls, charset='utf8'):
        import pymysql
        db_info = cls.get_db_info()
        return pymysql.connect(db_info['DB_HOST'], db_info['DB_USERNAME'],
                               db_info['DB_PASSWORD'], db_info['DB_NAME'], charset='utf8')

    # 查询一条记录
    @classmethod
    def query_one(cls, sql):
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
    def query_all(cls, sql):
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
    def update_db(cls, sql):
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

if __name__ == '__main__':
    pass