# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-12
-------------------------------------------------
   Change Activity:  18-1-12:
-------------------------------------------------
"""

'StudentRector 重构'

__author__ = '闫继龙'

class StudentRector(object):

    #定义一个特殊的__slots__变量，来限制该class实例能添加的属性
    __slots__ = ('_name','_score','_age') # 用tuple定义允许绑定的属性名称


    @property
    def score(self):
        return  self._score
    @score.setter
    def score(self,score):

        if not isinstance(score,int):
            raise ValueError('score must be an integer!')
        if score<0 or score>100:
            raise  ValueError('core must between 0 ~ 100!')
        self._score = score

    @property
    def name(self):
        return  self._name

    @name.setter
    def name(self,name):
        self._name = name


stu = StudentRector()
stu.score = 80

stu.name = "张三"

print("学生成绩：%s" %stu.score)
print("学生姓名：%s" %stu.name)
