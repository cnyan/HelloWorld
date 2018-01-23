# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-23
-------------------------------------------------
   Change Activity:  18-1-23:
-------------------------------------------------
"""

'requests_module'

__author__ = '闫继龙'

import requests

re = requests.get('https://www.douban.com/')
print(re.status_code)

#print(re.text)

print()
#对于带参数的URL，传入一个dict作为params参数：
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)

print()
#可以用content属性获得bytes对象：
print(r.content)

print()
#响应json
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

print()
#需要传入HTTP Header时，我们传入一个dict作为headers参数：
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
#print(r.text)

#要发送POST请求,后传入data参数作为POST请求的数据：
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

"""
上传文件
>>> upload_files = {'file': open('report.xls', 'rb')}
>>> r = requests.post(url, files=upload_files)
注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。

"""

#判断字符编码
import chardet

str_text = '离离原上草'.encode('utf-8')
print(chardet.detect(str_text))




