import pymysql

# 打开数据库连接(ip地址，数据库账户，密码，数据库名字)
db = pymysql.connect("192.168.136.128","root","123456","bbs")

# 使用 cursor() 方法创建一个游标对象 cursor
cur = db.cursor()
sql = "INSERT INTO user(first_name,last_name, age, sex, income)VALUES ('zhu', 'xia', 25, 'M', 10000000000000000000)"
# 使用 execute()  方法执行 SQL 查询
cur.execute(sql)
#
# # 使用 fetchone() 方法获取单条数据.
# data = cur.fetchall()   #存放到一个元组中
# print(data)

# 关闭数据库连接
db.close()