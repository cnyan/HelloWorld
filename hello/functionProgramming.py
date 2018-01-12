#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
我们通过把大段代码拆成函数，通过一层一层的函数调用，
就可以把复杂任务分解成简单的任务，
这种分解可以称之为面向过程的程序设计。
函数就是面向过程的程序设计的基本单元。


编程中提到的 lambda 表达式，通常是在需要一个函数，
但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
"""

#capitalize 讲字符串首字母改为大写
print("\n利用map()函数，把用户输入的不规范的英文名字，变为首字母大写:")
namelist = map(lambda l:str(l).capitalize(),['adam', 'LISA', 'barT'])
for name in namelist:
    print(name,end=" ")

#reduce把一个函数作用在一个序列上，这个函数必须接收两个参数
print("\n\n请编写一个prod()函数，可以接受一个list并利用reduce()求积")

from functools import reduce
def prod(list):
    return reduce(lambda x,y:x*y,list)

ji = prod([1,2,3,4])
print(ji)


#Python内建的filter()函数用于过滤序列
print("\n在一个list中，删掉偶数，只保留奇数")
def is_odd(num):
    if num%2==1:
        return num

numlist = filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15])
for num in numlist:
    print(num,end=" ")

#函数作为返回值
print("\n\n懒求和，返回求和函数")
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

"""
#lazy_sum 返回的是函数，
# 故调用的时候 应该lazy_sum(*args)()
print(lazy_sum(1,2,3,4,5)())
等价于==

f = lazy_sum(1,2,3,4,5)
print(f())
返回的函数并没有立刻执行，而是直到调用了f()才执行
"""
#print(lazy_sum(1,2,3,4,5)())
f = lazy_sum(1,2,3,4,5)
print(f())

#闭包
"""
注意到返回的函数在其定义内部引用了局部变量args，
所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用

返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。 
"""
#count()函数返回的式一个list集合，元素是函数
print("\n闭包的错误引用")
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1 = count
for f in f1():
    print(f(),end=" ")

#函数对象有一个__name__属性，可以拿到函数的名字
print("\n拿到f1函数的名字:"+f1.__name__)

#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）