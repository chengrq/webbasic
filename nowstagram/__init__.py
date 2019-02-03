# -*- encoding=UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('app.conf.txt')
db = SQLAlchemy(app)

from nowstagram import views, models