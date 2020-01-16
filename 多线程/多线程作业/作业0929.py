# 然后编写一个python程序，创建两个子线程，分别到下面的网址获取文本内容
#
# http://mirrors.163.com/centos/6/isos/x86_64/README.txt
# http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt
#
# 主线程等待这个两个子线程获取到信息后，将其内容依次合并后存入名为 readme.TXT 的文件中

import requests   #导入requests库
import threading  #导入进程模块
import time       #导入时间模块

def GetContent1(url1):   # 创建函数1
    r1=requests.get(url1)
    r1.text
    global a
    a=r1.text
# # 创建进程
t1=threading.Thread(target=GetContent1,args=('http://mirrors.163.com/centos/6/isos/x86_64/README.txt',))
t2=threading.Thread(target=GetContent1,args=('http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt',))
#t1线程开始执行，并将获取的内容追加到readme.TXT
t1.start()
t1.join()
fh=open('readme.TXT',"a+")
fh.write(a)
fh.close()

#t2线程开始执行，并将获取的内容追加到readme.TXT
t2.start()
t2.join()
fh=open('readme.TXT',"a+")
fh.write(a)
fh.close()
