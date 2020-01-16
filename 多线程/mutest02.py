import gevent,time

#导入补丁包
from gevent import monkey
#将程序中用到的耗时操作的代码，换为gevent中自己实现的模块
monkey.patch_all()       #在代码中使用以前的耗时模块


def fun(num):
    for i in range(num):
        print("函数1中循的次数：",i)
        # time.sleep(0.2)        #使用原来的阻塞模块
        gevent.sleep(0.2)
def fun1(num):
    for i in range(num):
        print("函数2中循环的次数：",i)
        # time.sleep(0.2)
        gevent.sleep(0.2)
print("创建协程g1")
g1 = gevent.spawn(fun,3)
print("创建协程g2")
g2 = gevent.spawn(fun1,3)
print("协程创建完成")


#注意gevent模块创建协程有个特点，遇到耗时操作就会去执行其他协程
#g1.join是一个耗时操作，在这里跳转到g1协程去执行
g1.join()     #等待子任务执行完毕后执行
print("g1执行完毕！")
g2.join()
print("g2执行完毕！")




