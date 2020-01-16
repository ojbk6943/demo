# 数据库查询操作
# Python查询Mysql使用
# fetchone()方法获取单条数据
# 方法获取多条数据, 使用fetchall()
#
# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()



import pymysql

# 打开数据库连接
db = pymysql.connect(host="192.168.136.128",
                     user="root",
                     password="123456",
                     database="bbs")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "select * from user where income > %s" % (1000)

# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print(results)
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]
    # 打印结果
    print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income))


# 关闭数据库连接
db.close()