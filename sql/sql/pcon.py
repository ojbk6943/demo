import pymysql

#封装，连接数据库和建立游标
def sql_con(host,username,password,databaseName,charset="utf8"):
    # 打开数据库连接
    db = pymysql.connect(host,username,password,databaseName,charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cur = db.cursor()
    return cur,db


#查询
def sel(host,username,password,databaseName,sql,charset="utf8"):
    #a代表游标对象，b代表数据库连接
    a,b = sql_con(host,username,password,databaseName,charset="utf8")
    a.execute(sql)
    data = a.fetchall()  # 存放到一个元组中
    print(data)
    b.close()


#增、删、改
def dcl(host,username,password,databaseName,sql,charset="utf8"):
    a, b = sql_con(host, username, password, databaseName, charset="utf8")
    a.execute(sql)       #执行sql语句
    b.commit()          #提交到数据库执行
    b.close()           #关闭连接



if __name__=='__main__':
  nun = "INSERT INTO user(first_name,last_name, age, sex, income)VALUES ('huang', 'a', 5, 'M', 100)"
  dcl(host="192.168.6.221", username="root", password="123456", databaseName="bbs", sql=nun)
