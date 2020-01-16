import pymysql
class Db:
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.2.154',
                               user='root',
                               password='123456',
                               database='test')
        self.cur = self.conn.cursor()    #建立游标对象

    #查询数据指定用户名查询，将查询结果返回
    def query_info_by_name(self,name):
        # self.cur = self.conn.cursor()
        self.cur.execute('select * from atm_info where name="%s"' % name)
        # self.cur.close()
        # self.conn.close()
        return self.cur.fetchone()         #返回的是元组

    def exec_dml(self,dml_sql):             #执行sql操纵语句
        # self.cur = self.conn.cursor()
        self.cur.execute(dml_sql)
        self.conn.commit()     #提交sql的执行

        # self.cur.close()
        # self.conn.close()

    def query_name_list(self):
        self.cur = self.conn.cursor()
        self.cur.execute('select name from atm_info')
        result = self.cur.fetchall()      #元组
        # self.cur.close()
        # self.conn.close()
        result_list = [i[0] for i in result]
        print(result_list)
        return result_list

    def __del__(self):                    #这是什么？结束化函数
        self.cur.close()
        self.conn.close()

# if __name__ == '__main__':
#     t1 = Db().query_name_list()
