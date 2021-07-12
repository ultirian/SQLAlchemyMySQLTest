# coding=utf-8
# Libraries
# Class
from sqlalchemy import Column, String, Integer
from base import Base, create_session
from log_in import user_name_entry
from user import User


def to_username():
    session = create_session()
    print("Students Username Required: \n")
    to_username_l = user_name_entry()
    # generates user object for comparison.
    our_user = session.query(User).filter(User.username == to_username_l).one()
    if our_user.username:
        print("Username Found.")
        return to_username_l

    print("Username Not Found")


class Message(Base):
    __tablename__ = 'messages'

    idmessages = Column(Integer, primary_key=True)
    from_user = Column(String(45))
    to_user = Column(String(45))
    messagescol = Column(String(100))

    def __init__(self, **kwargs):
        self.from_user = kwargs["from_user"]
        self.to_user = kwargs["to_user"]
        self.messagescol = kwargs["messagescol"]

    def from_username(self, user_obj):
        self.from_user = user_obj.username
        print(user_obj.name)
        return self.from_user

    def create_message(self):
        pass

    def message_input(self):
        pass
