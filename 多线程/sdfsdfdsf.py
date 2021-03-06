# coding=utf-8
import threading,time
from random import randint

commandList =[]

# 调用 Condition，返回一个条件对象， 该对象包含了一个锁对象
cv = threading.Condition()


# 消费者线程
def thread_consumer ():
    global  commandList

    while True:
        # 先申请锁
        cv.acquire()

        # 如果命令表为空 调用wait() ，该调用会释放锁,并且阻塞在此处，
        # 直到生产者 调用 该该条件变量的notify , 唤醒 自己
        # 一旦被唤醒, 将重新获取锁(所以生产者线程此时不能对共享资源进行操作)
        while commandList == []:
            cv.wait()

        resource = None
        # 拿出 生产者线程 产生的一个资源
        if commandList:
            resource = commandList[0]
            # 表示，已经被本消费者取出该资源了
            commandList.pop(0)

        # 取出一个共享资源后释放锁(生产者线程就可以对共享资源进行操作了)
        cv.release()

        if resource != None:
            # 随机等待一段时间,表示 消费资源的时间
            time.sleep(randint(1, 3))
            print('consume resource %s' % resource)


# 生产者线程
def thread_producer():
    global  commandList

    resource = 0
    while True:

        # 随机等待一段时间，表示生产资源的时间
        time.sleep(randint(1,3))

        # 通过条件变量 先申请锁
        cv.acquire()

        #申请锁成功后， 资源 存放入commandList 中
        commandList.append(resource)

        print('produce resource %s' % resource)

        # 随后调用notify，就像说 有任务啦，等任务的线程来处理吧。。
        # 该调用会唤醒一个 阻塞在该条件变量上等待的消费者线程
        cv.notify()

        cv.release()

        resource += 1



if __name__=='__main__':
    t1 = threading.Thread(target=thread_producer)
    t2 = threading.Thread(target=thread_consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()