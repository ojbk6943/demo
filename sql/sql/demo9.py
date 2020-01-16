import pymysql
x = 60
def pconect(host,username,password,databases):
    # 打开数据库连接(ip地址，数据库账户，密码，数据库名字)
    db = pymysql.connect(host,username,password,databases)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cur = db.cursor()
    return db,cur

def select(host,username,password,databases,ic):
    a,b=pconect(host,username,password,databases)
    sql ="select * from user where income > %s" % (ic)
    print(sql)
    # 使用 execute()  方法执行 SQL 查询
    b.execute(sql)
    data = b.fetchall()
    # 关闭数据库连接
    a.close()
    return data

def DIU(host, username, password, databases,sql):
    a, b = pconect(host, username, password, databases)
    # 执行sql语句
    b.execute(sql)
    # 提交到数据库执行
    a.commit()
    # 关闭数据库连接
    a.close()


# if __name__ == "__main__":
   dg = select("192.168.136.128","root","123456","bbs",1000)
   print(dg)
    # DIU("192.168.136.128","root","123456","bbs","UPDATE user SET income = 3000 WHERE last_name='xia1'")