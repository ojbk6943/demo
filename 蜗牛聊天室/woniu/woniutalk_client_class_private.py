import time
import socket
from threading import Thread

# def send_msg():
#     while True:
#         send_info = input('请输入您要发送的消息' + '\n')
#         s.send(send_info.encode('gbk'))
#         if send_info == 'quit':
#             break
#
# def recv_msg():
#     while True:
#         print(s.recv(1024).decode('gbk'))
#
#
# s = socket.socket()
# s.connect(('localhost',600))
#
# recv_info = s.recv(1024).decode('gbk')
# nick_name = input(recv_info)
# s.send(nick_name.encode('gbk'))
# print(s.recv(1024).decode('gbk'))
#
#
# # 设置收的线程为守护线程，这样可以保证，如果主线程结束，就不再收
# # 不再发，就不再收   保证主线程随发的线程结束而结束
#
# rt = Thread(target=recv_msg)
# st = Thread(target=send_msg)
# # 设置收为守护线程
# rt.setDaemon(True)
# st.start()
# rt.start()
#
# # 保证主线程只会在发的子线程结束后，才在关闭接口之后结束，随之结束守护的收消息线程。
# st.join()
# # 接口需要使用之后关闭
# s.close()
# # 多线程  客户端如果不用多线程 发送代码行运行之后才可以进行接收
# # 导致每次发送信息后才能收到服务器自上次接受后更新的信息
# # 需要通过多线程保证同时收发

class Client:

    def __init__(self):
        self.s = socket.socket()
        self.s.connect(('localhost', 600))

        recv_info = self.s.recv(1024).decode('gbk')
        nick_name = input(recv_info)
        self.s.send(nick_name.encode('gbk'))
        print(self.s.recv(1024).decode('gbk'))

        #两个线程分别接收和发送消息
        rt = Thread(target=self.recv_msg)
        st = Thread(target=self.send_msg)
        rt.setDaemon(True)
        st.start()
        rt.start()


        # 由析构函数负责接口的关闭，不需要阻塞
        # st.join()


    def send_msg(self):
        while True:
            send_info = input('请输入您要发送的消息' + '\n')
            self.s.send(send_info.encode('gbk'))
            if send_info == 'quit':
                break

    def recv_msg(self):
        while True:
            print(self.s.recv(1024).decode('gbk'))

    # 在析构函数处关闭接口
    def __del__(self):
        self.s.close()

if __name__ == '__main__':
    Client()
