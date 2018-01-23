# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-14
-------------------------------------------------
   Change Activity:  18-1-14:
-------------------------------------------------
"""

'Multiprocessing 多进程'

__author__ = '闫继龙'

"""
#-------------------------------------------------
# 一、fork（）函数

import  os

print('进程：%s 开始' % os.getpid())

#有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务

pid = os.fork()

if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


print()

"""

"""
#-------------------------------------------------
# 二、multiprocessing模块提供了一个Process类来代表一个进程对象
# 下面的例子演示了启动一个子进程并等待其结束：
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    #创建子进程时，只需要传入一个执行函数和函数的参数
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    #创建一个Process实例，用start()方法启动，
    p.start()
    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('Child process end.')


"""

"""
#-------------------------------------------------
# 进程池
#如果要启动大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import  os,time,random

def long_time_task(name):
    print('Run task %s (pid:%s) ……' % (name,os.getpid()))
    start = time.time() #获取当前时间
    time.sleep(random.random() * 5)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(4):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    #对Pool对象调用join()方法会等待所有子进程执行完毕，
    # 调用join()之前必须先调用close()
    p.close()
    p.join()
    print('All subprocesses done.')


"""

#-------------------------------------------------
# 子进程
#很多时候，子进程并不是自身，而是一个外部进程。
# 我们创建了子进程后，还需要控制子进程的输入和输出
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print("\n#如果子进程还需要输入，则可以通过communicate()方法输入：")
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')

print(output.decode('utf-8'))
print('Exit code:', p.returncode)



#-------------------------------------------------




#-------------------------------------------------




#-------------------------------------------------





#-------------------------------------------------






#-------------------------------------------------