#删除操作


import pymysql

db = pymysql.connect(host="192.168.136.128",
                     user="root",
                     password="123456",
                     database="bbs")
# 使用cursor()方法获取操作游标
cur = db.cursor()

# SQL 删除语句
sql = "DELETE FROM user WHERE last_name='xia'"

# 执行SQL语句
cur.execute(sql)
# 提交修改
db.commit()

# 关闭连接
db.close()