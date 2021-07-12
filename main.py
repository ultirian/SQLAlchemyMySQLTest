# coding=utf-8
# Libraries

from create_new_user import add_user
from log_in import log_in_user, check_username_match
from create_system_announcement import create_announcement
from user import User

if __name__ == "__main__":
    # log_in_user()
    user_obj = check_username_match()
    print(user_obj)
    create_announcement(user_obj)
# create_session()
# add_user()
# generate_pin()
# query_user()
