#from pprint import pprint
user_list = ['wangduoyu','zhuangqiang','dacongming']
password_list = ['123456','654321','888888']
user_info_dict = {'adam':['admin','18092190001',5000],
                  'beth':['admin','18092190001',5000],
                  'charlie':['admin','18092190001',5000],
                  }

# 登

while True:
    print('欢迎登录蜗牛ATM')
    print('操作选项：1为登录，2为注册，3为退出')

    choice = input("请输入您的操作选项数字")
    if choice == '1':
        wrong_input_name_three_times = False
        wrong_input_passwd_three_times = False

        #循环三次，
        for i in range(3):
            username = input("请输入您的用户名")
            if username in user_list:
                print('用户名合法，将输入密码')
                break
            else:
                if i < 2:
                    print('账户名输入错误，请再次输入用户名:')
                else:
                    print('账户名输错三次，将返回主界面')
                    wrong_input_name_three_times = True

        if wrong_input_name_three_times:
            continue

        # 开始密码的校验
        for i in range(3):
            passwd = input("请输入您的密码")
            if passwd == password_list[user_list.index(username)]:
                print('密码输入正确，登录成功')
                break
            else:
                if i < 2:
                    print('您输入的密码不合法，将再次输入密码')
                else:
                    print('您已经输错密码三次，将返回主界面')
                    wrong_input_passwd_three_times = True

        if wrong_input_passwd_three_times is True:
            continue


        print('欢迎%s用户使用蜗牛ATM' % username)

    elif choice == '2':    #开始注册了
        wrong_input_register_name_three_times = False

        for i in range(3):   #控制只能最多只能输入三次
            input_register_username = input("请输入您要注册的用户名")
            if input_register_username in user_info_dict:
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
            continue

        # 进行密码的设置
        while True:
            input_passwd_once = input("请输入您要设置的密码：")
            input_passwd_twice = input("请再次输入您要设置的密码：")
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
        user_info_dict[input_register_username] = [input_passwd_once, input_mobile, 5000]
        print(user_info_dict)
        print('注册成功,您将返回主界面')
    elif choice == '3':
        exit("即将退出")
    else:
        print("请输入合法的选项数字")


