from flask import request
from db import db


class ArticlesModel(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    user = db.relationship('User')

    def __init__ (self, title, body, author):
        self.title = title
        self.body = body
        self.author = author

    def json(self):
        return {'id': self.id,
                'title': self.title,
                'body': self.body,
                'author': self.user.username,
                'author_id': self.user.id
                }

    def get_usr_articles(self, username):
        return ArticlesModel.query.filter_by(author=username).all()

    def articles_display(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body
        }

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
