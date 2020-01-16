from func_oop import *
# from pack_atm_pymysql.func import *
class Ui:
    # 每个具体的ui实例，表示新的界面变化，需要回到哪个界面，就调用相应的函数----暂时搁置
    # ui实例对象，负责界面的展示功能，这个实例可以调用不同的方法，进入不同的界面

    def __init__(self):
        self.valid_username = None          #self.valid_username是个状态值（true或者false)
        self.f = Func()                     #调用功能，Func()中又调用Db()

    def show_main_menu(self):               #主界面
        while True:
            print('欢迎登录蜗牛ATM')
            print('操作选项：1为登录，2为注册，3为退出')

            choice = input("请输入您的操作选项数字")
            if choice == '1':
                self.valid_username = self.f.login() #login 登录不成功时返回值是ture或者false 登录成功时返回值是用户名
                if self.valid_username is True:
                    continue
                self.show_sub_menu(self.valid_username)      #能走到这一步说明登录已经成功了，self.valid_username是用户名
            elif choice == '2':
                # 如果注册失败三次，直接return 结束代码的运行，顺序结构返回主界面
                self.f.register()

                # result = register()
                # if result is True:
                #     continue
            elif choice == '3':
                exit("即将退出")
            else:
                print("请输入合法的选项数字")

    def show_sub_menu(self,valid_username):           #登录后子菜单
        while True:
            print('欢迎%s用户成功登录woniuATM' % valid_username)
            choice = input('转账请输入1，查询请输入2，存款请输入3，取款请输入4，返回主界面请按5，退出请按6')
            if choice == '1':
                self.f.transfer(valid_username)
            elif choice == '2':
                self.f.query_balance(valid_username)
            elif choice == '3':
                self.f.deposit(valid_username)  #存款
            elif choice == '4':
                self.f.withdraw(valid_username) #取款
            elif choice == '5':
                self.show_main_menu()
            elif choice == '6':
                exit('将退出，谢谢您的支持')
            else:
                print('请输入正确的业务代码')



# if __name__ == '__main__':
    # show_main_menu()
    # show_sub_menu('adam')
    # Ui().show_main_menu()
t1 = Ui()
t1.show_main_menu()
