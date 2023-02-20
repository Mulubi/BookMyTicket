''' Holds the class User '''
from Flask_BMT import db, models
from Flask_BMT.models.base_model import BaseModel, Base, BaseModelMixin
from sqlalchemy import Column, String, DateTime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, BaseModelMixin):
    ''' Object representation of a user '''
    __abstract__ = True
    if models.storage_type == 'db':
        __tablename__ = "users"
        first_name = db.Column(db.String(128), nullable=False)
        last_name = db.Column(db.String(128), unique=True, nullable=False)
        email = db.Column(String(128), nullable=False)
        password_hash = db.Column(db.String(128), nullable=False)
    else:
        first_name = ""
        last_name = ""
        email = ""
        password_hash = ""

    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', '{self.email}')"

    def __init__(self, *args, **kwargs):
        ''' Initializes the user '''
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
