# coding=utf-8
from socket import *

HOST = '192.168.2.186'
PORT = 28560        #服务器端口
BUFSIZ = 1024
ADDR = (HOST, PORT)

#创建socket，指明协议
tcpCliSock = socket(AF_INET, SOCK_STREAM)

#连接远程地址和端口，发送syn，等待 syn ack，也是阻塞式的
tcpCliSock.connect(ADDR)

while True:
    data = input('>> ')
    if not data:        #如果输入的消息是空字符
        break
    #     发送消息，必须是 bytes类型
    tcpCliSock.send(data.encode())      #把消息转换成bytes类型并发送出去

    # 阻塞式等待接收消息
    data = tcpCliSock.recv(BUFSIZ)
    # 当对方关闭连接的时候，返回空字符串
    if not data:
        break
    # 解码打印字符串
    print(data.decode())                #把消息转换成字符串类型并打印出来

tcpCliSock.close()