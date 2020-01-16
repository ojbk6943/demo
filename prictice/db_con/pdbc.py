import pymysql
db = pymysql.connect("192.168.2.96","root","123456","test")
cur=db.cursor()

sql="insert into classnew values ('jlk','sdaf','sdaf')"
#cur.execute(sql)
sql="select * from classnew "
cur.execute(sql)
db.commit
#
data=cur.fetchall()

#
print(data)
db.close()

