from flask import Flask
from flask_restful import Api
from flask_login import LoginManager

from users import UserReg, GetUsers, User, UserLogin, UserLogout
from articles import Articles

app = Flask(__name__)
api = Api(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(_id):
    return User.get(_id)


api.add_resource(UserReg, '/register')
api.add_resource(GetUsers, '/users')
api.add_resource(Articles, '/articles')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
