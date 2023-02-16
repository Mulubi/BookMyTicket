''' Holds the class User '''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel, Base):
    ''' Object representation of a user '''
    __tablename__ = "users"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), unique=True, nullable=False)
    email = Column(String(128), nullable=False)
    password_hash = Column(String(128), nullable=False)

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