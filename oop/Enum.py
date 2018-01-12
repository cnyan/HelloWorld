# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-12
-------------------------------------------------
   Change Activity:  18-1-12:
-------------------------------------------------
"""

'Enum'

__author__ = '闫继龙'


#-------------------------------------------------
#枚举类型
from enum import Enum

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

#样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print()
#-------------------------------------------------
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique

#@unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name,member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)


print()
#-------------------------------------------------
"""
type()函数既可以返回一个对象的类型，又可以创建出新的类型，
比如，我们可以通过type()函数创建出Hello类，
而无需通过class Hello(object)...的定义：

要创建一个class对象，type()函数依次传入3个参数：

    class的名称；
    继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

"""
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
h.hello()


#-------------------------------------------------




#-------------------------------------------------



#-------------------------------------------------