# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-12
-------------------------------------------------
   Change Activity:  18-1-12:
-------------------------------------------------
"""

'ZooRefactor 多重继承'

__author__ = '闫继龙'

class Animal(object):
    pass

# 第一大类:哺乳动物和鸟类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 第二大类：按照“能跑”和“能飞”来归类
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

"""
让Platypus(鸭嘴兽)除了继承自Bird外，再同时继承Mammal,Runnable,Flyable
这种多重继承的设计通常称之为MixIn

MixIn的目的就是给一个类增加多个功能，这
样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能
而不是设计多层次的复杂的继承关系。
"""

# 各种动物:
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal,Flyable): #蝙蝠
    pass

class Parrot(Bird,Flyable): #鹦鹉
    pass

class Platypus(Bird,Mammal,Runnable,Flyable): #鸭嘴兽
    pass
