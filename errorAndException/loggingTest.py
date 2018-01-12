# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-12
-------------------------------------------------
   Change Activity:  18-1-12:
-------------------------------------------------
"""

'logging test'

__author__ = '闫继龙'

"""
Python内置的logging模块可以非常容易地记录错误信息：
同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
"""

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')


import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
