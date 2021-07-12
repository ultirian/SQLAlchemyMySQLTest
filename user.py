# coding=utf-8
# Libraries
from sqlalchemy import Column, String, Integer, Boolean, Table, ForeignKey
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import relationship

from base import Base


# Classes
class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    password = Column(String(50))
    usertype = Column(Integer)
    pin = Column(String(4))
    is_admin = Column(TINYINT())
    is_lecturer = Column(TINYINT())
    is_student = Column(TINYINT())

    def __init__(self, **kwargs):
        self.username = kwargs["username"]
        self.firstname = kwargs["firstname"]
        self.lastname = kwargs["lastname"]
        self.password = kwargs["password"]
        self.usertype = kwargs["usertype"]
        self.pin = kwargs["pin"]
        self.is_admin = kwargs["is_admin"]
        self.is_lecturer = kwargs["is_lecturer"]
        self.is_student = kwargs["is_student"]
        super(User, self).__init__()

    # Returns a string representation of the object.
    def __repr__(self):
        return "<User(username='{0}', firstname='{1}', lastname='{2}', password='{3}', usertype='{4}', " "pin='{5}', is_admin='{6}, is_lecturer='{7}', is_student='{8}')>".format(
            self.username,
            self.firstname,
            self.lastname,
            self.password,
            self.usertype,
            self.pin,
            self.is_admin,
            self.is_lecturer,
            self.is_student,
        )
