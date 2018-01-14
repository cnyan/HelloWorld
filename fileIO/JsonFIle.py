# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-12
-------------------------------------------------
   Change Activity:  18-1-12:
-------------------------------------------------
"""

'JsonFIle'

__author__ = '闫继龙'

#把Python dict 可以直接变成一个JSON：

import json
# dict --> json
d = dict(name ='张三', gender ='男', age = 24)
print("把dict 变成一个JSON：")
jsonStr = json.dumps(d)
print(jsonStr)

#json --> dict
print("把JSON变成 dict：")
dd = json.loads(jsonStr)
print(dd)


#将class 实例对象 转化为 json
#因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量

class Student(object):
    def __init__(self, name, gender, age):
        self._name = name
        self._gender = gender
        self._age = age

    def __str__(self):
        return r'self.name = %s,self.gender = %s ,self.age = %s' % (self._name,str(self._gender),str(self._age))

    __repr__ = __str__

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def gender(self):
        return  self._gender
    @gender.setter
    def gender(self,gender):
        self._gender = gender

    @property
    def age(self):
        return  self._age
    @age.setter
    def age(self,age):
        self._age = age

stu = Student('李四','男',23)  #print(stu.name)

#obj --> json
print("方法一：实例对象 转化为 json")
jsonStr = json.dumps(stu,default= lambda obj: obj.__dict__)
print(jsonStr)

#或者 定义一个方法，将 实例对象转为dict，再转为json
print("方法二：实例对象 转化为 json")
def student2dict(std):
    return {
        'name': std.name,
        'gender': std.gender,
        'age': std.age
    }
jsonStr = json.dumps(stu,default=student2dict)
print(jsonStr)

#json --> obj
#定义一个函数，负责把返回的json 转为对象类型
print("将 json 转为 实例对象")
def dict2student(d):
    return Student(d['name'], d['gender'], d['age'])

jsonStr = json.loads(jsonStr,object_hook=dict2student)
print(jsonStr)