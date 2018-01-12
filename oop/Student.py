# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-11
-------------------------------------------------
   Change Activity:  18-1-11:
-------------------------------------------------
"""

'Student Class'

__author__ = '闫继龙'

class Student(object):

    def __init__(self):
        pass

# private 私有变量的命名形式：
# __name
# 注意！ __xxx__ 表示系统特殊变量

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("name:%s,score:%s" % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    #属性存取方法
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


#jim = Student()
bob = Student('Bob', 60)
lily = Student('Lily', 93)
#jim.print_score()
bob.print_score()
lily.print_score()

print(bob.get_grade())
print(lily.get_grade())

bob.__name = 'BOB'
bob.set_score(99)
bob.print_score()
