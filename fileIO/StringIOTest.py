# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-12
-------------------------------------------------
   Change Activity:  18-1-12:
-------------------------------------------------
"""

'StringIOTest'

__author__ = '闫继龙'


"""
StringIO

很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO顾名思义就是在内存中读写str。

要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
"""

#写内存

from io import StringIO

f = StringIO()
print("写入的字符数目：%d" %f.write("hello"))

f.write(' ')
f.write('world!')

#读取写入的内容:getvalue()方法用于获得写入后的str。
print(f.getvalue())

#读内存数据
f = StringIO("hello\nhi\ngoodbye")
while True:
    #str = f.read()
    str = f.readline()
    if str == '':
        break
    print(str)


#二进制流的内存读写
"""
StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
"""

from io import BytesIO

#写内存
f = BytesIO()
len = f.write('中文'.encode('utf-8',errors='strict'))
print("写入的二进制流字符数目：%d" %len)

#读内存
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

