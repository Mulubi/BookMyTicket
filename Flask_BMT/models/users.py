''' Holds the class User '''
from Flask_BMT import db, models, bcrypt
from Flask_BMT.models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import query
from werkzeug.security import generate_password_hash, check_password_hash
from .. import login_manager
from flask_login import UserMixin, login_user, AnonymousUserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    ''' Object representation of a user '''
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), unique=True, nullable=False)
    last_name = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(String(128), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role_id = db.Column(db.String(60), db.ForeignKey('roles.id'), nullable=False)


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', '{self.email}')"

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(name='Administrator').first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return self.can(Permission.ADMIN)


class AnonymousUser(AnonymousUserMixin):
    def can(self, perm):
        return False
    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser
