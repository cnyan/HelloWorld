# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-12
-------------------------------------------------
   Change Activity:  18-1-12:
-------------------------------------------------
"""

'FileTest'

__author__ = '闫继龙'


import  logging
logging.basicConfig(level=logging.INFO)




try:
    fopen1 = open("/home/yan/Desktop/软件源.txt",'r', encoding='gbk', errors='ignore')
    str = fopen1.read()
    print(str)
except Exception as e:
    logging.exception(e)
    #raise IOError('file read error!')

finally:
    fopen1.close()


#Python引入了with语句来自动帮我们调用close()方法：
with open("/home/yan/Desktop/软件源.txt",'r', encoding='gbk', errors='ignore') as fopen2:
    #print(fopen.read())
    for line in fopen2.readlines():
        #print(line)
        fopen2.close()


#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
with open('/home/yan/Pictures/习近平.jpg','rb') as fopen3:
    print(fopen3.read())
    fopen3.close()