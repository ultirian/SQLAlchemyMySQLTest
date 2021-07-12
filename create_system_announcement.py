# coding=utf-8
# Libraries

import datetime

import pyinputplus as pyin

from base import create_session

# Functions
from system_announcement_class import systemannouncement


def create_announcement(user_obj):

    if validate_admin(user_obj):
        session = create_session()
        date_time_now = datetime.datetime.now()
        s_announcement = systemannouncement(
            username=user_obj.username,
            time=date_time_now,
            subject=subject(),
            message_body=write_message(),
        )
        print(s_announcement)
        session.add(s_announcement)
        session.commit()
        session.close()
    else:
        print("Get Reked")


def validate_admin(user_obj):
    if user_obj.is_admin:
        return True
    else:
        print("You are not admin.\n")
        return False


def subject():
    subj = pyin.inputStr("Please Insert Subject: ")
    return subj


def write_message():
    message = pyin.inputStr("Input Message Body: ")
    return message
