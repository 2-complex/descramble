from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager

app = Flask(__name__, static_url_path = '/static')

app.config.from_object('app.configuration.DevelopmentConfig')

db = SQLAlchemy(app)

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'

from app import views
