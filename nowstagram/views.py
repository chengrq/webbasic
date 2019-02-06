# -*- encoding=UTF-8 -*-

from nowstagram import app
from nowstagram.models import Image, User
from flask import render_template

@app.route('/')
def index():
    image = Image.query.order_by('id desc').limit(10).all()
    return render_template('index.html',images=images)