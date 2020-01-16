# 创建数据库表
# 如果数据库连接存在我们可以使用execute()
# 方法来为数据库创建表，如下所示创建表bbs：

import pymysql

# 打开数据库连接
db = pymysql.connect(host="192.168.136.128",
                     user="root",
                     password="123456",
                     database="bbs")

# 使用 cursor() 方法创建一个游标对象 cursor
cur = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cur.execute("drop table if exists user")

# 使用预处理语句创建表
sql = """create table user (
         first_name  CHAR(20) NOT NULL,
         last_name  CHAR(20),
         age INT,  
         sex CHAR(1),
         income FLOAT )"""

cur.execute(sql)
print("*********************************")
# 关闭数据库连接
db.close()