# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-25
-------------------------------------------------
   Change Activity:  18-1-25:
-------------------------------------------------
"""

'np_test'

__author__ = '闫继龙'

import numpy as np

#向量相加
def np_sum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

#时间效率
from datetime import datetime

size = 1000
start_time = datetime.now()
c = np_sum(size)
end_time = datetime.now()
#print('c:',c)
print('时间差:',(end_time-start_time).microseconds)



#numpy 数组
a = np.arange(5)
print('a:',a)
print('a.dtype',a.dtype)

print()
#创建多维数组
m = np.array([np.arange(2),np.arange(2)] )
print('m:\n',m)

print()
# 广播
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = np.array([1.0,2.0,3.0])
print  ('第一个数组：')
print (a)
print()
print  ('第二个数组：')
print (b)
print()
print  ('第一个数组加第二个数组：')
print (a + b)

print()
# NumPy 包包含一个迭代器对象numpy.nditer
# 使用arange()函数创建一个 3X4 数组，并使用nditer对它进行迭代。
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('原始数组:\n',a)
print('迭代数组')
for x in np.nditer(a):
    print(x,end=' ')

#通过nditer实现矩阵(数组)的转置
print('\n,矩阵转置')
b = a.T
print(b)

print()
#可以通过显式提醒，来强制nditer对象使用某种顺序：
for x in np.nditer(b, order =  'C'):
    print(x,end=' ')
print()
for x in np.nditer(b,order='F'):
    print(x,end=' ')

#修改数组的值
print('\n')
print('原始数组是:')
print(a)
print('通过op_flags设置读写')
for x in np.nditer(a,op_flags=['readwrite']):
    x[...] = 2 * x
print(a)


print('\nbroadcast广播机制')
#如前所述，NumPy 已经内置了对广播(broadcast)的支持。
# 此功能模仿广播机制。 它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。

x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
print('x:',x)
print('y:',y)
# 对 y 广播 x
b = np.broadcast(x,y)

#布尔型索引
print('\n布尔型索引')
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data = np.arange(28).reshape(7,4)
#data = np.empty(28).reshape(7,4)
print(data)
print('bool_data')
names == 'Bob'
bool_data = data[names == 'Bob']
print(bool_data)

#花式索引
print('\n 花式索引')
arr = np.empty((8,4)) #8*4矩阵
for i in range(8):
    arr[i] = i
print(arr)

print('\n')
print(arr[[3,4,0,6]])


print('\n数组的组合')
#数组的组合
a = np.arange(9).reshape(3,3)
print(a)


