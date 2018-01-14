# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-12
-------------------------------------------------
   Change Activity:  18-1-12:
-------------------------------------------------
"""

'PicklingTest 序列化'

__author__ = '闫继龙'

#文件以及目录操作，基于系统OS
import os

print(os.name)

print("当前绝对路径：%s" % os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:

# 然后创建一个目录
#os.mkdir("/home/yan/Desktop/file")
# 删掉一个目录:
#os.rmdir('/home/yan/Desktop/test')

# 创建一个空文件
#os.mknod("/home/yan/Desktop/file/dump.txt")
# 删除一个文件
#os.remove("/home/yan/Desktop/dump.txt")

# 对文件重命名:
#os.rename('test.txt', 'test.py')
# 删掉文件:
#os.remove('test.py')

#判断路径下的文件或文件夹是否存在
if os.path.exists('/home/yan/Desktop/dump.txt'):
    print('/home/yan/Desktop/dump.txt 已经存在')
else:
    print('/home/yan/Desktop/dump.txt 不存在')

if os.path.exists('/home/yan/Desktop/file'):
    print('/home/yan/Desktop/file 已经存在')
else:
    print('/home/yan/Desktop/file 不存在')

#检查路径是否为文件
if os.path.isfile('/home/yan/Desktop/file/dump.txt'):
    print('/home/yan/Desktop/dump.txt 是文件')
else:
    print('/home/yan/Desktop/dump.txt 不是文件')




#数据序列化
import pickle

d = dict(name='张三',age='23',score=80)
#print(pickle.dumps(d)) #pickle.dumps()方法把任意对象序列化成一个bytes

f = open('/home/yan/Desktop/file/dump.txt','wb') #wb:以二进制格式写入数据
pickle.dump(d, f)
f.close()

#反序列化
f = open('/home/yan/Desktop/file/dump.txt','rb')
d = pickle.load(f)
f.close()
print('反序列化的结果是：')
print(d)

