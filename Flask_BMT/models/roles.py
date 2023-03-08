''' Holds the Role class where all the users will get their allocated rights to the app '''
from Flask_BMT import db, models, bcrypt
from Flask_BMT.models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Boolean
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import query
from werkzeug.security import generate_password_hash, check_password_hash
from .. import login_manager
from flask_login import UserMixin, login_user
from datetime import datetime


class Permission:
	FOLLOW = 1
	COMMENT = 2
	WRITE = 4
	MODERATE = 8
	ADMIN = 16


class Role(db.Model):
    ''' Object representation of a role '''
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f"Role('{self.name}')"

    def __init__(self, **kwargs):
    	super(Role, self).__init__(**kwargs)
    	if self.permissions is None:
    		self.permissions = 0

    def add_permission(self, perm):
    	if not self.has_permission(perm):
    		self.permissions += perm

    def remove_permission(self, perm):
    	if self.has_permission(perm):
    		self.permissions -= perm

    def reset_permissions(self, perm):
    	self.permissions = 0

    def has_permission(self, perm):
    	return self.permissions & perm == permissions

    @staticmethod
    def insert_roles():
        roles = {
            'User' : [Permission.COMMENT],
  			'Moderator' : [Permission.COMMENT, Permission.WRITE, Permission.MODERATE],
  			'Administrator' : [Permission.FOLLOW, permission.COMMENT, Permission.WRITE, Permission.MODERATE, Permission.ADMIN],
  			}
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
                role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()
