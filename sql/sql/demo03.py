#数据库插入操作使用执行SQL INSERT语句


import pymysql

# 打开数据库连接
db = pymysql.connect(host="192.168.136.128",
                     user="root",
                     password="123456",
                     database="bbs")

# 使用cursor()方法获取操作游标
cur = db.cursor()

# SQL 插入语句
sql = "INSERT INTO user(first_name,last_name, age, sex, income)VALUES ('zhu1', 'xia1', 25, 'M', 10000000000000000000)"

# 执行sql语句
cur.execute(sql)
# 提交到数据库执行
db.commit()

# 关闭数据库连接
db.close()