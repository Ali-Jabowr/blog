from flask import Flask
from flask_restful import Api
from flask_login import LoginManager
from os import path

from resources.users import UserReg, GetUsers, UserLogin, UserLogout
from resources.articles import Articles
from models.users import User


app = Flask(__name__)
api = Api(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

login_manager = LoginManager()
login_manager.init_app(app)

#establishing and configuring database
DB_NAME = 'data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_NOTIFICATION'] = False

@app.before_first_request
def create_tables():
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print('database created successfuly...!')

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


api.add_resource(UserReg, '/register')
api.add_resource(GetUsers, '/users')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(Articles, '/article')


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=8000, debug=True)
