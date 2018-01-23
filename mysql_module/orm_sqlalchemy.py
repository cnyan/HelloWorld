# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-24
-------------------------------------------------
   Change Activity:  18-1-24:
-------------------------------------------------
"""

'orm_sqlalchemy'

__author__ = '闫继龙'


#这就是传说中的ORM技术：Object-Relational Mapping，
# 把关系数据库的表结构映射到对象上
"""
class User(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name
"""


from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类：
Base = declarative_base()

#创建User 对象
class User(Base):
    #表的名字
    __tablename__ = 'user'

    #表的结构
    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    books = relationship('Book')


engine = create_engine('mysql+mysqlconnector://root:123@localhost:3306/sqltest')

#创建DBSession类型
DBSession = sessionmaker(bind=engine)


#我们向数据库表中添加一行记录，可以视为添加一个User对象
"""
#创建session对象:
session = DBSession()
#创建user 对象
new_user = User(id='4',name='Kit')
#添加到session
session.add(new_user)
#提交即保存到数据库
session.commit()
#关闭session
session.close()
"""

#SQLAlchemy提供的查询接口如下：
session = DBSession(bind=engine)

# 创建Query查询，filter是where条件，
# 最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='4').one()

# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()


#例如，如果一个User拥有多个Book，就可以定义一对多关系如下：

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20),ForeignKey('user.id'))

#创建session
session = DBSession(bind=engine)
#创建对象
new_book1 = Book(id='1',name="python",user_id='2')
new_book2 = Book(id='2',name="java",user_id='1')
new_book3 = Book(id='3',name="ios",user_id='4')
new_book4 = Book(id='4',name="android",user_id='3')
#对象添加到session中
session.add(new_book1)
session.add(new_book2)
session.add(new_book3)
session.add(new_book4)
# 提交即保存到数据库:
session.commit()
session.close()


