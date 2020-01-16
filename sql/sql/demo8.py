from sql.pcon import dcl

nun = 'delete from user where age=5'
dcl(host="192.168.6.221", username="root", password="123456", databaseName="bbs", sql=nun)



