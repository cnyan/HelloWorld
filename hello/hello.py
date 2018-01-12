#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hello world!')

#字符串拼接与格式化
"""
print('输入姓名')
name = input('name:')
print("姓名"+name+",性别%s,年龄%d" %('男',20))

"""

#函数定义与调用
import math

def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)

print(x,y)

#字典迭代器
dict = {"name":"张三","gender":"男","age":24}

print("\n打印输出字典 1:")
for value in dict.items():
    print(value)

print("\n打印输出字典 2:")
for k,v in dict.items():
    print(k,v)

print("\n迭代输出字典键值：")
for key in dict:
    print("键："+key ,end=" ")
    print("值："+ str(dict[key]) ,end=" ")    #数字拼接字符串时，需要转为字符类型
    print()


#列表生成式 ：
print("\n生成 x*x 样式列表 :%s" % [x*x for x in range(1,11)] )

#利用列表生成式 列出当前目录下的所有文件和目录名
import  os;
print("\n列出当前目录下的所有文件和目录名 ")
print( [direct for direct in os.listdir(".")] )

#列表生成器
"""
列表生成器：这种一边循环一边计算的机制，称为生成器（Generator）
generator保存的是算法，每次调用next()，就计算出下一个元素的值，
直到计算到最后一个元素
"""
print("\n列表生成器演示")
list = [x*x for x in range(10)]
generator = (x*x for x in range(10))
print(list)
print(generator)
for value in generator:
    print(value, end=" ")

#使用普通函数 计算斐波那契数列
print("\n\n使用普通函数 斐波那契数列")
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print(b,end=" ")
        a,b = b,a+b
        n+=1
fib(8)

#利用列表生成器 计算斐波那契数列
"""
如果一个函数定义中包含yield关键字，
那么这个函数就不再是一个普通函数，而是一个generator
yield 是一个类似 return 的关键字，
迭代一次遇到yield时就返回yield后面(右边)的值。
重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
简要理解：yield就是 return 返回一个值,
并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
"""

print("\n利用列表生成器 斐波那契数列")
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n+=1

print(fib(10))
for v in fib(10):
    print(v,end=" ")


