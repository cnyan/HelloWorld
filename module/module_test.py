# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-22
-------------------------------------------------
   Change Activity:  18-1-22:
-------------------------------------------------
"""

'hashlib'

__author__ = '闫继龙'


#-------------------------------------------------
import hashlib

md5_str = hashlib.md5()
md5_str.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5_str.hexdigest())

print()
#-------------------------------------------------
# Hmac算法
import hmac
message = b'Hello,world!'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())


print()
#-------------------------------------------------
# 上下文管理是通过__enter__和__exit__这两个方法实现的
class Query(object):
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('Beigin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('error')
        else:
            print('end')

    def query(self):
        print('Query info about %s' % self.name)


with Query('Bob') as q:
    q.query()

print()
#-------------------------------------------------
# 因此Python的标准库contextlib提供了更简单的写法
# ，上面的代码可以改写如下：
from contextlib import contextmanager

class Query2(object):
    def __init__(self,name):
        self.name = name

    def query(self):
        print('Query info about %s' % self.name)

@contextmanager
def create_query(name):
    print('Beigin')
    q = Query2(name)
    yield q
    print('end')

with create_query('kitty') as q:
    q.query()

print()
#-------------------------------------------------
# 我们希望在某段代码执行前后自动执行特定代码，
# 也可以用@contextmanager实现

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag('h1'):
    print('hello')
    print('world')

print()
#-------------------------------------------------
#可以用closing()来把该对象变为上下文对象
#用with语句使用urlopen()：
from contextlib import closing
from urllib.request import  urlopen

with closing(urlopen(r'https://www.baidu.com')) as page:
    for line in page:
        print(line)


print()
#-------------------------------------------------
#urllib的request模块可以非常方便地抓取URL内容，
# 也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：

from urllib import  request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:',f.status,f.reason)

    for k,v in f.getheaders():
        print('%s:%s' % (k,v))

    print('Data:',data.decode('utf-8'))

print()
#-------------------------------------------------
#如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，
# 通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
# 例如，模拟iPhone 6去请求豆瓣首页,这样豆瓣会返回适合iPhone的移动版网页

from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:

    print('Status:',f.status,f.reason)

    for k,v in f.getheaders():
        print('%s:%s' % (k, v))

    print('Data:', f.read().decode('utf-8'))

#-------------------------------------------------
#如果要以POST发送一个请求，只需要把参数data以bytes形式传入
#模拟微博登录:先读取登录的邮箱和口令，然后按照weibo.cn的登录页
# 的格式以username=xxx&password=xxx的编码传入

from urllib import  request,parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')

login_data = parse.urlencode([
    ('username',email),
    ('password',passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer',
     'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print('Status:',f.status,f.reason)

    for k,v in f.getheaders():
        print('%s:%s' % (k,v))

    print('Data:',f.read().decode('utf-8'))




#-------------------------------------------------