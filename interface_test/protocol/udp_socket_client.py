#! /usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

for i in range(1, 10):
    # 建立一个udp连接
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 连接到的主机和端口
    mysocket.connect(("127.0.0.1", 23456))
    # 发送者姓名 +IPMSG的报文格式：版本号 + 包编号 + 发送 发送者主机名 + 命令字 + 附加信息
    packetId = str(time.time())
    name = "Donald John Trump"
    host = "Trump's Notebook"
    content = "This is the message from python中文"
    # 构建消息体
    message = "1.0:" + packetId + ":" + name + ":" + host + ":"  + content
    mysocket.send(message.encode('utf8'))
    mysocket.close()
    time.sleep(2)
