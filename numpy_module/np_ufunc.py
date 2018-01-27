# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-26
-------------------------------------------------
   Change Activity:  18-1-26:
-------------------------------------------------
"""

'np_ufunc'

__author__ = '闫继龙'

import numpy as np

#利用数组进行数据处理

#向量化
points = np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
print(xs)



