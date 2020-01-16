import pymysql
import time

#开始界面
def show_main_menu(host, username, password, databaseName):
    while True:
        print('欢迎登录蜗牛ATM')
        print('操作选项：1为登录，2为注册，3为退出')

        choice = input("请输入您的操作选项数字")
        if choice == '1':
            valid_username = login(host, username, password, databaseName)
            show_sub_menu(host, username, password, databaseName,valid_username)
        elif choice == '2':
            register(host, username, password, databaseName,)
        elif choice == '3':
            exit("即将退出")
        else:
            print("请输入合法的选项数字")

#用户登录
def login(host, username, password, databaseName):
    wrong_input_name_three_times = False
    wrong_input_passwd_three_times = False

    for i in range(3):
        input_username = input("请输入您的用户名")

        #去数据库查询输入的用户名是否存在
        result = query_info_by_name(host, username, password, databaseName,input_username)
        if result:   #result存在就代表真
            print('用户名合法，将输入密码')
            break
        else:
            if i < 2:
                print('您输入的用户名不合法，将再次输入用户名')
            else:
                print('您已经输错用户名三次，将返回主界面')
                wrong_input_name_three_times = True

    if wrong_input_name_three_times:
        show_main_menu(host, username, password, databaseName)

    #开始密码的校验
    for i in range(3):
        input_passwd = input("请输入您的密码")
        if input_passwd == result[1]:
            print('密码输入正确，登录成功')
            break
        else:
            if i < 2:
                print('您输入的密码不合法，将再次输入密码')
            else:
                print('您已经输错密码三次，将返回主界面')
                wrong_input_passwd_three_times = True

    if wrong_input_passwd_three_times:
        show_main_menu()

    print('欢迎%s用户使用蜗牛ATM'%input_username)
    return input_username

#注册
def register(host, username, password, databaseName):

    wrong_input_register_name_three_times = False

    for i in range(3):
        input_register_username = input("请输入您要注册的用户名")
        result = query_info_by_name(host, username, password, databaseName,input_register_username)
        if result:
            if i < 2:
                print('您输入的用户名已存在，请再次输入')
            else:
                print("您已经输入非法的注册用户名三次，将返回主界面")
                wrong_input_register_name_three_times = True

        else:
            print("您输入的用户名合法，将进行密码的设置")
            break
    # 判断是否失败三次
    if wrong_input_register_name_three_times:
        show_main_menu(host, username, password, databaseName)

    # 进行密码的设置
    while True:
        input_passwd_once = input("请输入您要设置的密码:")
        input_passwd_twice = input("请再次输入您要设置的密码:")
        if input_passwd_once == input_passwd_twice \
                and len(input_passwd_once) in range(6,13) \
                and input_passwd_once.isalnum():

            print('密码设置成功，将进行手机号码的输入')
            break
        else:
            print('两次输入不一致或不符合标准，请参照标准再次输入')

    # 进行电话号码的校验
    while True:
        input_mobile = input("请输入合法的手机号码")
        if len(input_mobile) == 11 \
            and input_mobile.isdigit() \
            and input_mobile[0] == '1' \
            and int(input_mobile[1]) in range(3,10):

            print('您输入的手机号码合法')
            break
        else:
            print('您输入的手机号码不合法，请再次输入')

    # 显示注册成功的信息，并将信息保存
    dml_sql = 'insert into atm_info (name,password,mobile,balance) values ("%s","%s","%s",%d)'\
              %(input_register_username,input_passwd_once,input_mobile,5000.0)
    exec_dml(host, username, password, databaseName,dml_sql)
    print('注册成功,您将返回主界面')


#封装，连接数据库和建立游标
def sql_con(host,username,password,databaseName,charset="utf8"):
    # 打开数据库连接
    db = pymysql.connect(host,username,password,databaseName,charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cur = db.cursor()
    return cur,db

#用来在登录或者注册的时候，查找是否存在输入的用户名
def query_info_by_name(host,username,password,databaseName,name):
    a,b = sql_con(host,username,password,databaseName,charset="utf8")
    a.execute('select * from atm_info where name="%s"'%name)
    b.close()
    return a.fetchone()

#可注册插入数据到数据库
def exec_dml(host, username, password, databaseName,dml_sql):
    a, b = sql_con(host, username, password, databaseName, charset="utf8")
    a.execute(dml_sql)
    b.commit()
    b.close()


#登录后的操作
def show_sub_menu(host, username, password, databaseName,valid_username):

    print('欢迎%s用户成功登录woniuATM')
    while True:
        choice = input('转账请输入1，查询请输入2，存款请输入3，取款请输入4，返回主界面请按5，退出请按6')
        if choice == '1':
            transfer(host, username, password, databaseName,valid_username)         #转账
        elif choice == '2':
            query_balance(host, username, password, databaseName,valid_username)    #余额查询
        elif choice == '3':
            deposit(host, username, password, databaseName,valid_username)          #存款
        elif choice == '4':
            withdraw(host, username, password, databaseName,valid_username)         #取款
        elif choice == '5':
            show_main_menu(host, username, password, databaseName)                  #返回主界面
        elif choice == '6':
            exit('将退出，谢谢您的支持')                                             #退出
            break
        else:
            print('请输入正确的业务代码')

#转账
def transfer(host, username, password, databaseName,valid_username):
    while True:
        re = query_info_by_name(host, username, password, databaseName,valid_username)
        data = float(input("转账金额："))
        #data=0为退出操作
        if data == 0:
            break
        elif data > re[3]:
            print("余额不足")
            #continue
        else:
            trans_name = input("请输入转账用户：")
            tname = query_info_by_name(host, username, password, databaseName, trans_name)
            if trans_name == tname[0]:
               overage1 = re[3]-data
               #更新金额
               transfer_deposit(host, username, password, databaseName, overage1, valid_username)
               #更新金额
               overage2 = tname[3]+data
               transfer_deposit(host, username, password, databaseName, overage2, trans_name)
               print("转账成功，剩余金额：%f" % overage1 )
               break
            #需要一个函数，更新金额
            else:
                print("您输入的账户不存在，请重新输入")

#查询余额
def query_balance(host, username, password, databaseName,valid_username):
    a, b = sql_con(host, username, password, databaseName, charset="utf8")
    a.execute('select * from atm_info where name="%s"' % valid_username)
    re = a.fetchone()
    print("您的余额为：%f" % re[3])
    b.close()

#存款
def deposit(host, username, password, databaseName,valid_username):
    dit = float(input("请输入存款金额："))
    re = query_info_by_name(host, username, password, databaseName,valid_username)
    #dit代表要存款的金额，re代表之前的金额，两个相加为我们要更新上去数据
    postit = dit+re[3]
    a, b = sql_con(host, username, password, databaseName, charset="utf8")
    dml_sql = 'update atm_info set balance = "%.3f" where name="%s"' % (postit,valid_username)
    a.execute(dml_sql)
    b.commit()
    b.close()

#取款
def withdraw(host, username, password, databaseName,valid_username):
    while True:
        dit = float(input("请输入取款金额："))
        re = query_info_by_name(host, username, password, databaseName, valid_username)
        if dit > re[3]:
            print("余额不足")
        else:
            # dit代表要存款的金额，re代表之前的金额，两个相加为我们要更新上去数据
            postit = re[3] - dit
            a, b = sql_con(host, username, password, databaseName, charset="utf8")
            dml_sql = 'update atm_info set balance = "%.3f" where name="%s"' % (postit, valid_username)
            a.execute(dml_sql)
            b.commit()
            print("您的余额为：%f" % postit)
            b.close()
            break

#转账时，更新金额
def transfer_deposit(host, username, password, databaseName,overage,valid_username):
    a, b = sql_con(host, username, password, databaseName, charset="utf8")
    dml_sql = 'update atm_info set balance = "%.3f" where name="%s"' % (overage,valid_username)
    a.execute(dml_sql)                       #"%3f"的意思是小数点精度
    b.commit()
    b.close()


# if __name__ == '__main__':
show_main_menu("192.168.136.128", "root", "123456", "bbs")