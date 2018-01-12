# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-12
-------------------------------------------------
   Change Activity:  18-1-12:
-------------------------------------------------
"""

'FooError'

__author__ = '闫继龙'

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value :%s" %s)
    return 10/n


def bar():
    try:
        foo(0)
    except ValueError as e:
        print("ValueError")
        raise   #raise语句如果不带参数，就会把当前错误原样抛出

#foo(0)
bar()