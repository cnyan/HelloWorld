#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-11
-------------------------------------------------
   Change Activity:  18-1-11:
-------------------------------------------------
"""

'zoo'

__author__ = '闫继龙'

class Animal(object):

    #类属性：类的所有实例都可以访问该属性
    class_attr = '类属性'

    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)

