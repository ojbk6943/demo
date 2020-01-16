def exec_thread(so,so_list):
    so.send('欢迎您使用蜗牛聊天室，请确认您的昵称'.encode('gbk'))
    nick_name = so.recv(1024).decode('gbk')

    welcome_info = '欢迎%s用户登录蜗牛聊天室，可以发言了' % nick_name
    print(welcome_info)
    so.send(welcome_info.encode('gbk'))

    while True:
        recv_info = so.recv(1024).decode('gbk')
        # 当收到quit，将当前的so接口从列表中删除，退出循环
        if recv_info == 'quit':
            print(nick_name + '退出聊天室')
            so_list.remove(so)
            break


        # 加工收到的客户端的消息
        new_info = time.ctime() + '-------' + nick_name + '\n' \
                   + recv_info + '\n'

        # 将消息加工后，再在服务器端打印
        print(new_info)

        for _ in so_list:
            _.send(new_info.encode('gbk'))

import socket
import time
from threading import Thread

# s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
# s.bind(('localhost',600))
# s.listen(5)
# so_list = []
#
#
# while True:
#     so,addr = s.accept()
#     print(so)
#     so_list.append(so)
#
#     Thread(target=exec_thread,args=(so,so_list)).start()



# 私聊信息的实现    ’@zhangsan 你还活着吗‘
# 构造一个 名字为键 接口为值的字典，当收到相应格式的信息时，通过名字对应的接口发送相应消息

# 类的封装

class Server:

    def __init__(self):
        # 在构造函数中可以调用方法，直接执行代码
        self.s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
        self.s.bind(('localhost', 600))
        self.s.listen(5)
        self.so_list = []
        self.so = None
        # 构造姓名-接口字典
        # self.name_so_dict = {}

        while True:
            # 每次进入循环时，等待连接的时间一旦超过30秒，就会break循环，析构
            # 计时器线程每次进入循环时开启，每隔一秒，计数加一，三十时，break
            # 另外的线程是我们原先的循环体函数，和计数器线程同时进行
            # 如果三十秒到，break；如果三十秒内有连接，直接将计时器线程杀死

            self.so, addr = self.s.accept()
            print(self.so)
            self.so_list.append(self.so)

            Thread(target=exec_thread, args=(self.so,self.so_list)).start()

    def exec_thread(self,so,so_list):
        so.send('欢迎您使用蜗牛聊天室，请确认您的昵称'.encode('gbk'))
        nick_name = so.recv(1024).decode('gbk')
        # 将相应的名字和接口放入字典
        # name_so_dict[nick_name] = so

        welcome_info = '欢迎%s用户登录蜗牛聊天室，可以发言了' % nick_name
        print(welcome_info)
        so.send(welcome_info.encode('gbk'))

        while True:
            recv_info = so.recv(1024).decode('gbk')
            # 当收到quit，将当前的so接口从列表中删除，退出循环
            if recv_info == 'quit':
                print(nick_name + '退出聊天室')
                so_list.remove(so)
                break

            # # 判断是否是私聊信息，如果是，之发送给指定人
            # # 私聊的格式为’@zhangsan Are you all right？‘
            # if recv_info.startswith('@'):
            #     print('hehehehehe')
            #     # 将名字截取出来，是按空格切割一次后的列表第一个元素（@zhangsan）的下标一切片
            #     name = recv_info.split(' ',1)[0][1:]
            #     # 需要发送的消息是按空格切割一次后的第二位元素，加上注释来自当前用户
            #     new_info = recv_info.split(' ',1)[1] + '---from ' + nick_name
            #     # 通过名字对应的接口发送消息
            #     name_so_dict[name].send(new_info.encode('gbk'))
            #     # 发送完开始新的循环
            #     continue

            # 加工收到的客户端的消息
            new_info = time.ctime() + '-------' + nick_name + '\n' \
                       + recv_info + '\n'

            # 将消息加工后，再在服务器端打印
            print(new_info)

            for _ in so_list:
                _.send(new_info.encode('gbk'))

    # def __del__(self):
    #     self.so.close()
    #     self.s.close()
if __name__ == '__main__':
    Server()