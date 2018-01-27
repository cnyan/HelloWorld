# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-27
-------------------------------------------------
   Change Activity:  18-1-27:
-------------------------------------------------
"""

'np_study'

__author__ = '闫继龙'

# 一维数组
import numpy as np
a = np.arange(24)
print(a.ndim) #返回数组维度
print(a)

b = a.reshape(2,6,2)
print(b)
print(b.ndim)

print(b.flags)

print()
#NumPy - 数组创建例程
a = np.empty([3,2],dtype=float,order='C')
b = np.empty([3,2],dtype=float,order='F')
print(a)
print('\n',b)


print()
#NumPy - 来自现有数据的数组

#展示了frombuffer函数的用法
str = b'Hello numpy'
arr = np.frombuffer(str,dtype='S1')
print(arr)


print()
#numpy.fromiter,从任何可迭代对象构建一个ndarray对象
a = np.arange(5)
b = iter(a)
c = np.fromiter(b,dtype=np.int8)
print(c)

print()
#展示了linspace函数的用法。
x = np.linspace(10,20,5)
print(x)

y = np.linspace(10,20,5,endpoint=False)
print(y)

z = np.linspace(10,20,5,retstep=True)
print(z)


print()
#NumPy - 切片和索引
#种可用的索引方法类型： 字段访问，基本切片和高级索引。

#切片,如果只输入一个参数则将返回与索引对应的单个项
a = np.arange(10)
s = slice(2,7,2)
print(a[s])
print(a[2:7:2])
print(a[5])

print()
# 多维ndarray数组切片
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
print('现在我们从索引 a[1:] 开始对数组切片')
print(a[1:])

print()
#多个冒号可以用一个省略号（...）来代替
print('切片还可以包括省略号（...），来使选择元组的长度与数组的维度相同')
print('第二列的元素是')
print(a[...,1])
print('第二行的元素是')
print(a[1,...])
print('第二列及其剩余元素是:')
print(a[...,1:])

print()
#NumPy - 高级索引:有两种类型的高级索引：整数和布尔值。
x = np.array([[1,2,3],[2,3,4],[4,5,6]])
y = x[[0,1,2],[0,1,0]] #(0,0),(1,1),(2,0)整数型索引
z = x[[0,0],[1,1]]
print(x)
print('\n',y)
print(z)

print()
#面的示例获取了 4X3 数组中的每个角处的元素。 行索引是[0,0]和[3,3]，而列索引是[0,2]和[0,2]。
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print('原数组')
print(x)

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
print('这个数组的每个角处的元素是：'  )
print(y)

print()
#这个例子使用了~（取补运算符）来过滤NaN。
a = np.array([np.nan,1,2,np.nan,3,4,5],)
print(a)
print (a[~np.isnan(a)])











































