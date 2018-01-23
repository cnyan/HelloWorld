# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-23
-------------------------------------------------
   Change Activity:  18-1-23:
-------------------------------------------------
"""

'mysql_test'

__author__ = '闫继龙'

import mysql.connector


conn = mysql.connector.connect(user='root',password='123',database='sqltest')

"""
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) PRIMARY key,name VARCHAR (20))')

cursor.execute('insert into user (id,name) VALUES (%s,%s)',['1','make'])
cursor.execute('insert into user (id,name) VALUES (%s,%s)',['2','bob'])
cursor.execute('insert into user (id,name) VALUES (%s,%s)',['3','admin'])
#记录条数
print(cursor.rowcount)

#提交事物
conn.commit()
cursor.close()
"""


# 运行查询:
cursor = conn.cursor()


cursor.execute('select * from user ')
values = cursor.fetchall()
print(values)

# 关闭Cursor和Connection:
cursor.close()
conn.close()
