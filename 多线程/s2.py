# coding=utf8

print('main thread start.')

import threading
from time import sleep

def f1():
    print('child thread 1, start')
    # sleep(10)
    print('child thread 1, end')

#主线程是解释器在创建的，入口函数在代码开头，
t1 = threading.Thread(target=f1)         #target只能是这个线程的入口函数，target指定入口函数时，不能带括号

t1.start()   #启动创建的子线程t1
# sleep(5)
print('main thread end.')
