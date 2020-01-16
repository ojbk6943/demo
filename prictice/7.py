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



# if __name__=='__main__':
#   nun = "INSERT INTO user(first_name,last_name, age, sex, income)VALUES ('huang', 'a', 5, 'M', 100)"
#   dcl(host="192.168.6.221", username="root", password="123456", databaseName="bbs", sql=nun)









#from pprint import pprint
user_list = ['wangduoyu','zhuangqiang','dacongming']
password_list = ['123456','654321','888888']
user_info_dict = {'adam':['admin','18092190001',5000],
                  'beth':['admin','18092190001',5000],
                  'charlie':['admin','18092190001',5000],
                  }
#创建一个死循环，反复的跳回主界面，主界面有三个按钮

while True:
    print('欢迎登录在线ATM系统')
    print('请选择您需要的操作:1,登录 2,注册 3.退出')
    choice=int(input("请输入数字："))
    flag = True
  #按钮1代表登录
    if choice==1:
        #连接数据库
        sql_con(host="192.168.2.96", username="root", password="123456", databaseName="test")
    #登录的操作最多执行三次
        for i in range(3):
     #判断用户名是否合法，如果不合法跳回主页面，如果合法提示登录成功。
           username = input("请输入您的用户名：")
           if username in user_list:
                print("用户名合法请输入密码：")
                break
           else:
               if i<2:
                   print("用户名不存在请重新输入")
                   continue
               else:
                   print("用户名输入错误三次返回主界面")
                   flag=False
        if flag==False:
            continue

  #按钮2代表注册
    elif choice==2:
    #注册的操作最多执行三次
        sql_con() #打开数据库链接
        for i in range(3):
            # 判断用户名是否合法，如果不合法跳回主页面，如果合法提示登录成功。
            username = input("请输入您的用户名：")

            if username in user_list:
                if i<2:                           #用户名重复两次内
                    print("用户名已存在请重新输入")
                    continue
                else:                             #用户名重复第三次
                    print("用户名输入错误三次返回主界面")
                    flag=False
            else:
                print("用户名合法请输入密码")
                break
        if flag == False:
            continue

     #判断用户名是否已经存在，已存在-重新输入，不存在-进入下一步设置密码-密码确认两次。
       #密码设置
       while True:
               psw=input("请输入密码：")
               dcl()#将第一次输入的密码写入密码表
               psw1=input("请再次输入密码：")
               dcl()  # 将第二次输入的密码写入密码表
               if psw==psw1 and psw.isalnum() and len(psw) in range(6, 13):
                   print("密码设置成功即将设置电话号码")
                   break
               else:
                   print("两次密码不一致请重新设置")


       #电话号码的验证
       while True:
            input_mobile = input("请输入合法的手机号码")
            dcl()#将手机号码写入手机号码表
            if len(input_mobile) == 11 \
                    and input_mobile.isdigit() \
                    and input_mobile[0] == '1' \
                    and int(input_mobile[1]) in range(3, 10):

                print('您输入的手机号码合法')
                break
            else:
                print('您输入的手机号码不合法，请再次输入')

       user_info_dict[username]=[username,psw,input_mobile,5000]
       print(user_info_dict)
       print('注册成功,您将返回主界面')
       break
    elif choice==3:
        #exit("即将退出")
        print("即将退出")
        break
    else:
        print("请输如合法选项")
        #
  #按钮3代表退出




