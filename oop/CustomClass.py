# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-12
-------------------------------------------------
   Change Activity:  18-1-12:
-------------------------------------------------
"""

'CustomClass 通过Python内建方法，实现类的定制'

__author__ = '闫继龙'

#-------------------------------------------------------------------
#定义好__str__()方法，返回一个好看的字符串就可以了
class Student(object):
     def __init__(self, name):
        self.name = name
     def __str__(self):
        return 'Student object (name: %s)' % self.name

stu = Student("张三")
print(stu)
"""
__str__()，而是__repr__()，
两者的区别是__str__()返回用户看到的字符串，
而__repr__()返回程序开发者看到的字符串，
也就是说，__repr__()是为调试服务的。

解决办法是再定义一个__repr__():
__repr__ = __str__
"""
#-------------------------------------------------------------------

#__iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)

#-------------------------------------------------------------------

#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

# 动态语言，可以给在类的外面绑定方法
def __getitem__(self, n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a

Fib.__getitem__ = __getitem__

f = Fib()
print("斐波那契数列 第10个是：%d" %f[10])

#-------------------------------------------------------------------
#给__getitem__() 函数增加类似列表切片的功能

def __getitem__(self, n):
    if isinstance(n, int):  # n是索引
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
    if isinstance(n, slice):  # n是切片
        start = n.start
        stop = n.stop
        if start is None:
            start = 0
        a, b = 1, 1
        L = []
        for x in range(stop):
            if x >= start:
                L.append(a)
            a, b = b, a + b
        return L

Fib.__getitem__ = __getitem__

print("切片功能：")
f = Fib()
print(f[0:5])

#-------------------------------------------------------------------

#那就是写一个__getattr__()方法，动态返回一个属性
def __getattr__(self, attr):
    if attr == 'age':
        return lambda: 25
    else:
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

Student.__getattr__ = __getattr__
stu = Student("李四")
#print(stu.package)

#-------------------------------------------------------------------
#利用完全动态的__getattr__，我们可以写出一个链式调用：调用API的URL
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain('mypython').status.user.timeline.list)


#-------------------------------------------------------------------
#直接调用对象
#只需要定义一个__call__()方法，就可以直接对实例进行调用。

def __call__(self):
    print('My name is %s.' % self.name)

Student.__call__ = __call__

stu = Student("李四")
stu()


#-------------------------------------------------------------------
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print(callable(f))      #false
print(callable(stu))    #true


#-------------------------------------------------------------------



#-------------------------------------------------------------------




#-------------------------------------------------------------------

