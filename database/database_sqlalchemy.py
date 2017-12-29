# _*_ coding:utf-8 _*_

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id      = Column(Integer, primary_key=True)
    email   = Column(String(45))
    passwd  = Column(String(45))
    admin   = Column(Integer)
    name    = Column(String(45))
    image   = Column(String(500))
    created_at = Column(Integer)

engine = create_engine('mysql+mysqlconnector://root:Mtt2017@localhost:3306/webapp')

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user = Users(id=7, email='321654@qq.com', passwd='8888', admin=1, name='wtt', image='abc.png', created_at=1510728072)

session.add(new_user)

session.commit()

session.close()


session = DBSession()

users = session.query(Users).filter(Users.id < '8').all()

for i in range(len(users)):
    print(i)
    print(users[i].id)
    print(users[i].email)
    print(users[i].passwd)
    print(users[i].admin)
    print(users[i].name)
    print(users[i].image)
    print(users[i].created_at)

session.close()