# coding=utf-8

import threading,socket

HOST = ''
PORT = 28560
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 这是新线程执行的函数，每个线程负责和一个客户端进行通信
def on_new_client(clientsocket,addr):
    while True:
        data = clientsocket.recv(BUFSIZ)
        # 当对方关闭连接的时候，返回空字符串
        if not data:
            print('%s 关闭了连接' % addr)
            break

        # 接受到的是bytes类型，需要解码
        rstr = data.decode()

        print('%s:%s' % (addr, rstr))
        clientsocket.send(data)

    clientsocket.close()         #四次挥手


# 主线程 创建监听的socket
serversocket = socket.socket()
#绑定端口和ip地址
serversocket.bind(ADDR)

#处于监听状态
serversocket.listen(5)

# 在while循环里面 不断接受新的连接请求，
# 并创建新线程专门和这个服务端进行通信
while True:
   clientsocket, addr = serversocket.accept()
   addr = str(addr)
   print('从 %s 来的连接' % addr)
   th = threading.Thread(target=on_new_client,args=(clientsocket,addr))
   th.start()



