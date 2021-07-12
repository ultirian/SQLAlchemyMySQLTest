# coding=utf-8
# Libraries
# Class
from user import User


class LogInObject(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logged_in = kwargs["logged_in"]
        self.pw_match = kwargs["pw_match"]
        self.pin_match = kwargs["pin_match"]

    def __repr__(self):
        return (
            "<User(username='{0}', firstname='{1}', lastname='{2}', password='{3}', usertype='{4}', "
            "pin='{5}', is_admin='{6}, is_lecturer='{7}', is_student='{8}', logged_in='{9}', pw_match='{10}', "
            "pin_match='{11}')>".format(
                self.username,
                self.firstname,
                self.lastname,
                self.password,
                self.usertype,
                self.pin,
                self.is_admin,
                self.is_lecturer,
                self.is_student,
                self.logged_in,
                self.pw_match,
                self.pin_match,
            )
        )
