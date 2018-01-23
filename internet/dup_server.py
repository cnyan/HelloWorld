# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-23
-------------------------------------------------
   Change Activity:  18-1-23:
-------------------------------------------------
"""

'dup_server'

__author__ = '闫继龙'


# begin socket 服务器端
"""
一个Socket依赖4项：
服务器地址、服务器端口、客户端地址、客户端端口
来唯一确定一个Socket。
"""
import socket,threading,time

#首先，创建一个基于IPv4和TCP协议的Socket：
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
#用listen()方法开始监听端口,传入的参数指定等待连接的最大数量：
s.listen(5)
print('Waiting for connection...')
#cept()会等待并返回一个客户端的连接:
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    socket.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break

        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

        sock.close()
        print('Connection from %s:%s closed.' % addr)