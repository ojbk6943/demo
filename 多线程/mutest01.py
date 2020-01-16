import gevent
import time
def fun(num):
    for i in range(num):
        print("函数1中循环的次数：",i)
        gevent.sleep(0.1)
        # time.sleep(0.1)

def fun1(num):
    for i in range(num):
        print("函数2中的循环的次数：",i)
        gevent.sleep(0.1)
        # time.sleep(0.1)

print("创建协程g1")
g1 = gevent.spawn(fun,3)
print("创建协程g2")
g2 = gevent.spawn(fun1,3)
print("创建协程完成")


# #注意gevent模块创建协程有个特点，遇到耗时操作就会去执行其他协程
#g1.join是一个耗时操作，在这里跳转到g2协程执行
g1.join()     #等待子任务执行完毕后执行
print("g1执行完毕！")
g2.join()
print("g2执行完毕")
