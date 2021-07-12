# coding=utf-8
# Libraries
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

# Classes
from user import User


class systemannouncement(Base):
    __tablename__ = "systemannouncement"
    __table_args__ = {"comment": "system announcement Table\\n"}

    idSystemAnnouncement = Column(Integer, primary_key=True)
    username = Column(String(45))
    time = Column(DateTime)
    subject = Column(String(45))
    message_body = Column(String(45))

    def __init__(self, username, time, subject, message_body):
        self.username = username
        self.time = time
        self.subject = subject
        self.message_body = message_body

    def __repr__(self):
        return "<systemannouncement(username='{0}', time ='{1}', subject='{2}, msg_body='{3}'>".format(
            self.username, self.time, self.subject, self.message_body
        )
