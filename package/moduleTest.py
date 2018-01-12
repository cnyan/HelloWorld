#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-11
-------------------------------------------------
   Change Activity:  18-1-11:
-------------------------------------------------
"""

'模块文件测试'

__author__ = '闫继龙'

"""
当我们在命令行运行hello模块文件时，
Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败，
因此，这种if测试可以让一个 模块 通过命令行运行时执行一些额外的代码，
最常见的就是运行测试
"""

import sys

def test():
    args = sys.argv
    if(len(args) == 1):
        print('Hello,%s!' %args[0]) #args[0] 默认参数为文件名称
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()