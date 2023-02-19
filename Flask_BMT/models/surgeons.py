''' Holds the class Surgeon '''
from Flask_BMT import db, models
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Surgeon(BaseModel, Base):
    ''' Object representation of a surgeon '''
    if models.storage_type == 'db':
        __tablename__ = "surgeons"
        name = Column(String(128), unique=True, nullable=False)
        contact_info = Column(Integer())
        # theatres = relationship("Theatre", backref="surgeon")
        # theatre_id = Column(String(128), ForeignKey("theatres.id"), nullable=False)
    else:
        name = ""
        contact_info = ""

    def __repr__(self):
        return f"Patient('{self.name}', '{self.contact_info}'"

    def __init__(self, *args, **kwargs):
        ''' Initializes the surgeon '''
        super().__init__(*args, **kwargs)
