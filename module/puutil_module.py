# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-23
-------------------------------------------------
   Change Activity:  18-1-23:
-------------------------------------------------
"""

'puutil_module'

__author__ = '闫继龙'

#psutil = process and system utilities，
# 它不仅可以通过一两行代码实现系统监控

#获取CPU信息
import psutil
print(psutil.cpu_count())# CPU逻辑数量
print(psutil.cpu_count(logical=False)) # CPU物理核心s

#统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())

#再实现类似top命令的CPU使用率，每秒刷新一次，累计10次
for x in range(3):
    print(psutil.cpu_percent(interval=1,percpu=True))

#获取物理内存
print(psutil.virtual_memory())
#交换内存信息
print(psutil.swap_memory())

print()
#获取磁盘信息
#可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())

print()
#获取网络信息
#psutil可以获取网络接口和网络连接信息
print(psutil.net_io_counters())# 获取网络读写字节／包的个数
print(psutil.net_if_addrs())## 获取网络接口信息