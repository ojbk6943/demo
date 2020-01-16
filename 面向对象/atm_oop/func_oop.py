import pymysql
# from pack_atm_pymysql.db import *
from db_oop import *

class Func:

    def __init__(self):
        self.db = Db()

    def login(self):
        wrong_input_name_three_times = False
        wrong_input_passwd_three_times = False

        for i in range(3):
            input_username = input("请输入您的用户名")
            result = self.db.query_info_by_name(input_username)   #result接收到的是个元组
            if result:    #result存在就是真
                print('用户名合法，将输入密码')
                break
            else:
                if i < 2:
                    print('您输入的用户名不合法，将再次输入用户名')
                else:
                    print('您已经输错用户名三次，将返回主界面')
                    wrong_input_name_three_times = True

        if wrong_input_name_three_times:
            # show_main_menu()
            return wrong_input_name_three_times      #此处放回一个状态值，login函数返回一个状态值

        # 开始密码的校验
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
            # show_main_menu()
            return wrong_input_passwd_three_times

        print('欢迎%s用户使用蜗牛ATM' % input_username)
        return input_username    #登陆成功会返回输入的用户名，也就是当前的用户名

    def register(self):
        wrong_input_register_name_three_times = False

        for i in range(3):
            input_register_username = input("请输入您要注册的用户名")
            result = self.db.query_info_by_name(input_register_username)
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
            # show_main_menu()
            # return wrong_input_register_name_three_times

            # 加入注册用户名输入无效3次，直接结束当前代码
            return

        # 进行密码的设置
        while True:
            input_passwd_once = input("请输入您要设置的密码:")
            input_passwd_twice = input("请再次输入您要设置的密码:")
            if input_passwd_once == input_passwd_twice \
                    and len(input_passwd_once) in range(6, 13) \
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
                    and int(input_mobile[1]) in range(3, 10):

                print('您输入的手机号码合法')
                break
            else:
                print('您输入的手机号码不合法，请再次输入')

        # 显示注册成功的信息，并将信息保存
        dml_sql = 'insert into atm_info (name,password,mobile,balance) values ("%s","%s","%s",%d)' \
                  % (input_register_username, input_passwd_once, input_mobile, 5000.0)
        self.db.exec_dml(dml_sql)
        print('注册成功,您将返回主界面')

    def transfer(self,valid_username):
        # 转账
        # 提供转入账户 和 转出金额   更新当前登录账户和转入账户的余额
        # 不可以自己转账给自己，不可以转入不存在的账户，转账金额不能超过余额
        # 存款 取款 查询

        # 获取所有合法的用户名信息，除去自己
        valid_name_list = self.db.query_name_list()
        while True:
            transfer_to_username = input('请输入您要转入的账户')
            if transfer_to_username in valid_name_list \
                    and transfer_to_username != valid_username:

                # 设置标志变量，控制金额输入的死循环结构 在错误达到一定次数时，结束循环返回上一层
                # 或者登录成功后的主界面进行后续操作
                print('您输入的转入账户合法，请继续输入金额')

                # 获取当前账户余额以及待转入账户的余额
                login_account_current_balance = self.query_balance(valid_username)
                tranfer_to_account_current_balance = self.query_balance(transfer_to_username)

                # 进行转账
                while True:
                    transfer_amount = float(input('请输入您要转账的金额'))
                    # 判断金额 不可以超过当前余额
                    if transfer_amount > login_account_current_balance:
                        print('你输入的金额过大，无法进行转账')
                    else:
                        # 计算新余额并更新至数据库
                        login_account_new_balance = login_account_current_balance - transfer_amount
                        transfer_to_account_new_balance = tranfer_to_account_current_balance + transfer_amount
                        update_sql = 'update atm_info set balance = %f where name = "%s"' \
                                     % (login_account_new_balance, valid_username)
                        update_sql_1 = 'update atm_info set balance = %f where name = "%s"' \
                                       % (transfer_to_account_new_balance, transfer_to_username)
                        self.db.exec_dml(update_sql)
                        self.db.exec_dml(update_sql_1)
                        break

                        # 您已经向某个账户转入金额XX，余额为XX
                print('转账完成，将返回登录成功用户的操作主界面')
                # show_sub_menu(valid_username)
                break
            else:
                print('您输入的转入账户无效，请参照规则重新输入')


    def query_balance(self,valid_username):
        conn = pymysql.connect(host='192.168.136.128',
                               user='root',
                               password='123456',
                               database='bbs')
        cur = conn.cursor()
        # 占位符需要加引号。来实现占位功能
        cur.execute('select balance from atm_info where name = "%s"' % valid_username)
        result = cur.fetchone()
        return result[0]

    def deposit(self,valid_username):
        pass

    def withdraw(self,valid_username):
        pass

if __name__ == '__main__':
    Func().login()
