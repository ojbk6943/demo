import threading
import time

print("aaa")

def loop(arg):
    print("1234",time.ctime())
    time.sleep(arg)
    print("56789",time.ctime())

def loop1(arg):
    print("-1234",time.ctime())
    time.sleep(arg)
    print("-56789",time.ctime())
t1=threading.Thread(target=loop,args=(1,))  #创建新线程
t2=threading.Thread(target=loop1,args=(2,)) #创建
t1.start()
t2.start()

time.sleep(3)
t1.join()
t2.join()
print("333333",time.ctime())
