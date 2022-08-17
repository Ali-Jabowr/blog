import re
from flask import request
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from db import db

from models.articles import ArticlesModel

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))


    article = db.relationship('ArticlesModel')

    def __init__(self, username, password, email):
        self.email = email
        self.username = username
        self.password = password

    @classmethod
    def find_in_db(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def login_check(cls, email, password):
        res = cls.query.filter_by(email=email).first()
        if res:
            if check_password_hash(res.password, password):
                return res

    def json(self):
        return {'id': self.id,
                'username': self.username,
                'email': self.email,
                'password': self.password,
                'articles': list(map(lambda x: x.articles_display(), ArticlesModel.query.filter_by(author=self.id)))
                }

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
