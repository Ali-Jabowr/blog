import sqlite3 as sq3
import re
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def __init__(self, _id, username, password, email):
        self.id = _id
        self.email = email
        self.username = username
        self.password = password

    @classmethod
    def find_in_db(cls, username, email, password):
        conn = sq3.connect('data.db')
        cur = conn.cursor()

        query = "SELECT * FROM users WHERE username=? "
        cur.execute(query, (username,))

        row = cur.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        conn.close()
        return user

    @classmethod
    def login_check(cls, email, password):
        con = sq3.connect('data.db')
        cur = con.cursor()

        query = "SELECT * FROM users WHERE email=?"
        cur.execute(query, (email,))

        res = cur.fetchone()
        if res:
            if check_password_hash(res[2], password):
                user_log = cls(*res)
                return user_log


