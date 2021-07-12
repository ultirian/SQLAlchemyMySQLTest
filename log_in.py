"""
Name: Christopher Weaver
Date: 11/07/2021
Project: USW Coursework 2 Remake with Python and MySQL
Additional lib Used: black, pylint, sqlacodegen.
Description: Log in methods associated with log in class.
"""

# coding=utf-8
# Libraries
import pyinputplus as pyin
from log_in_class import LogInObject
from user import User
from base import create_session
from sqlalchemy.orm.exc import NoResultFound


# Functions


def query_user():
    # Call create_session() func to local object
    session = create_session()
    # Query the user
    username_input_local = pyin.inputStr(" Insert Search User: ")
    our_user = session.query(User).filter_by(username=username_input_local).first()
    if our_user:
        print("Username Found")
        print("\nOur User:")
        print("Username: ", our_user.username, "Firstname: ", our_user.firstname)
    else:
        print("Username Not Found")
        print("\nOur User:")
        print(our_user)

    session.close()


def log_in_user():
    check_username_match()


def pin_check(pin_in):
    pin_entry = pyin.inputStr("Insert Pin: ")
    if pin_entry == pin_in:
        print("Pin OK")
        return True

    print("Pin Bad")
    return False


def check_password_match(pw_in):
    print(pw_in)
    pwd_entry = pyin.inputStr("Insert Password: ")
    if pw_in == pwd_entry:
        print("Password OK!")
        return True
    print("BAD PASSWORD!")
    return False


def is_logged_in(pin_match, pw_match):
    if pin_match & pw_match:
        return True
    return False


def user_name_entry():
    username_l = pyin.inputStr("Insert Username: ")
    return username_l


def check_username_match():
    # create session
    session = create_session()
    # User Inputs
    unl = user_name_entry()
    # generates user object for comparison.
    our_user = session.query(User).filter(User.username == unl).one()
    # Creating object
    print(our_user)
    # User Object
    user_obj = LogInObject(
        username=our_user.username,
        password=our_user.password,
        firstname=our_user.firstname,
        lastname=our_user.lastname,
        pin=our_user.pin,
        usertype=our_user.usertype,
        is_admin=our_user.is_admin,
        is_lecturer=our_user.is_lecturer,
        is_student=our_user.is_student,
        pin_match=False,
        logged_in=False,
        pw_match=False,
    )

    try:
        if (
            our_user
            and check_password_match(our_user.password)
            and pin_check(our_user.pin)
        ):
            print("Username Found")
            # debugging
            print("Username: ", our_user.username, "Firstname: ", our_user.firstname)
            print("Password Match")
            print("Pin match")
            # set condition args to true
            user_obj.pw_match = True
            user_obj.pin_match = True
            user_obj.logged_in = is_logged_in(user_obj.pin_match, user_obj.pw_match)
            print(user_obj)
            return user_obj

        else:
            print("Username Not Found")
            print("\nOur User:")
            print(our_user)
    except NoResultFound as e:
        print(e)
