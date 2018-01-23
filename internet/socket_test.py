# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-23
-------------------------------------------------
   Change Activity:  18-1-23:
-------------------------------------------------
"""

'socket_test'

__author__ = '闫继龙'

"""
通常我们用一个Socket表示“打开了一个网络链接”，
而打开一个Socket需要知道目标计算机的IP地址和端口号，
再指定协议类型即可。
"""

import socket

# begin socket 客户端

# 创建一个socket:
s = socket.socket()
# 建立连接:
s.connect(('www.sina.com.cn',80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#发送的文本格式必须符合HTTP标准，
# 如果格式没问题，接下来就可以接收新浪服务器返回的数据了：

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
data = b''.join((buffer))

# 关闭连接:
s.close()

header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('../src/file/sina.html','wb') as f:
    f.write(html)


# end socket 客户端



