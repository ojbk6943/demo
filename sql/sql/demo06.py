#数据库更新操作


import pymysql

db = pymysql.connect(host="192.168.136.128",
                     user="root",
                     password="123456",
                     database="bbs")

# 使用cursor()方法获取操作游标
cur = db.cursor()


# SQL 更新语句
sql = "UPDATE user SET income = 3000 WHERE last_name='xia'"

# 执行SQL语句
cur.execute(sql)
# 提交到数据库执行
db.commit()


# 关闭数据库连接
db.close()