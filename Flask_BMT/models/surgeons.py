''' Holds the class Surgeon '''
from Flask_BMT import db, models
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Surgeon(BaseModel, Base):
    ''' Object representation of a surgeon '''
    #__abstract__ = True
    if models.storage_type == 'db':
        __tablename__ = "surgeons"
        name = Column(String(128), unique=True, nullable=False)
        contact_info = Column(Integer, nullable=False, default=0)
        speciality = Column(String(128), nullable=True)
    else:
        name = ""
        contact_info = ""
        speciality = ""

    def __repr__(self):
        return f"Patient('{self.name}', '{self.contact_info}'"

    def __init__(self, *args, **kwargs):
        ''' Initializes the surgeon '''
        super().__init__(*args, **kwargs)
