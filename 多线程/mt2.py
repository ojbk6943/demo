# coding=utf8
import threading
from time import sleep

# 存储支付账号余额
weizhifu = {
    'caixukong'     : 12000,
    'limingchen'  : 7500,
    'gouqi'  : 10000,
    'zhaolei' : 10340,
}

# 线程1 ： 购物处理，参数是用户账户和扣款金额
def thread1_gouwu_pay(account,amount):
    print('* t1: get balance from bank')
    balance = weizhifu[account]

    # 下面的sleep(2) 表示一些处理过程需要花上2秒钟
    print('* t1: do something(like discount lookup) for 2 seconds')
    sleep(2)

    print('* t1: deduct')
    weizhifu[account] = balance - amount


# 线程2 ： licai赚取利息 参数是用户账户和当前利息
def thread2_licai_interest(account,amount):
    print('$ t2: get balance from bank')
    balance = weizhifu[account]

    # 下面的sleep(1) 表示一些处理过程需要花上1秒钟
    print('$ t2: do something2.... for 1 seconds')
    sleep(1)

    print('$ t2: add')
    weizhifu[account] = balance + amount



t1 = threading.Thread(target=thread1_gouwu_pay,  args=('caixukong',100))
t2 = threading.Thread(target=thread2_licai_interest, args=('caixukong',200))
t1.start()
t2.start()
t1.join()
t2.join()
print('finally, caixukong balance is %s' % weizhifu['caixukong'])
