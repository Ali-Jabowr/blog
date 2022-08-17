from db import db
from flask import request
from flask_restful import Resource
from flask_login import current_user, login_required

from models.articles import ArticlesModel


class Articles(Resource):

    @login_required
    def post(self):
        data = request.get_json()
        article = ArticlesModel(data['title'], data['body'], current_user.id)
        article.add_to_db()
        return {'message': 'post added successfuly...!'}

    def get(self):
        posts = ArticlesModel.query.all()
        return {"articles": list(map(lambda x: x.json(), posts))}

    @login_required
    def delete(self):
        data = request.get_json()
        article = ArticlesModel.query.filter_by(id=data['id']).first()

        if not article:
            return {'message': 'the article does not exists...!'}
        elif article.user.id != current_user.id:
            return {'message': 'You don\'t have permession to delete...'}
        else:
            article.delete_from_db()
            return {'message': 'article deleted successfuly...!'}
