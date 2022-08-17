import re
from flask import request
from flask_restful import Resource
from flask_login import login_user, logout_user, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from models.users import User
from models.articles import ArticlesModel


class UserReg(Resource):
    pattern = re.compile("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+")

    def post(self):
        data = request.get_json()
        if not User.find_in_db(data['username']):

            if not UserReg.pattern.match(data['email']):
                return {'messege': "Email not valid"}

            elif not data['password'] == data['confirm']:
                return {"message": "passwords don't match"}

            else:
                password = generate_password_hash(data['password'], method='sha256')
                user = User(data['username'], password, data['email'])
                try :
                    user.add_to_db()
                    return {"message": "the user added successfuly...!"}
                except:
                    return {"message": "an error has occurred...!"}


        return {'messege': "the user already registerd"}


class GetUsers(Resource):
    def get(self):
        return {'users': list(map(lambda x: x.json(), User.query.all()))}


class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = User.login_check(data['email'], data['password'])
        if user:

            login_user(user)
            return {"message": "logged in successfuly...!"}
        else:
            return {"message": "Email or password incorrect...!"}


@login_user
class UserLogout(Resource):
    def post(self):
        logout_user()
        return {"message": "User Loggedout successfuly...!"}
