#!/usr/bin/env python3
""" SQLAlchemy model named User """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String)
    reset_token = Column(String)

    def __repr__(self):
        return ("<User(email='%s', hashed_password='%s', "
                "session_id='%s', reset_token='%s')>" %
                (self.email, self.hashed_password,
                 self.session_id, self.reset_token))
