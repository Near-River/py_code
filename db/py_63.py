#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# sqlalchemy: ORM framework

# create the base class for objects
Base = declarative_base()
# Initial connection to the database
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test')
# Create DBSession
DBSession = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'user'

    # table structure
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    def __str__(self):
        return 'id: %s  name: %s' % (self.id, self.name)


def insertEntity():
    session = DBSession()
    new_user = User(id='1', name='Jack')
    session.add(new_user)
    session.commit()
    session.close()


def queryEntity():
    session = DBSession()
    user = session.query(User).filter(User.id == '1').one()
    print('type:', type(user))
    print('user:', user)
    session.close()


if __name__ == '__main__':
    # insertEntity()
    queryEntity()
