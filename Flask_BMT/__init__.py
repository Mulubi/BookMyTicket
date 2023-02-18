import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = '41ed75074dc9acfc44d3ca8ab3d6477f'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
db = SQLAlchemy(app)

from Flask_BMT import auth, routes
