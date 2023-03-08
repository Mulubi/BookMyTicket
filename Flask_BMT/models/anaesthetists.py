''' Holds the class Anaesthetist '''
from Flask_BMT import db, models
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Anaesthetist(BaseModel, Base):
    ''' Object representation of an anaesthetist '''
    #__abstract__ = True
    if models.storage_type == 'db':
        __tablename__ = "anaesthetists"
        name = Column(String(128), unique=True, nullable=False)
        contact_info = Column(Integer, nullable=False, default=0)
    else:
        name = ""
        contact_info = ""

    def __repr__(self):
        return f"Anaesthetist('{self.name}', '{self.contact_info}')"

    def __init__(self, *args, **kwargs):
        ''' Initializes the anaesthetist '''
        super().__init__(*args, **kwargs)
