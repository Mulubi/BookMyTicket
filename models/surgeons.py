''' Holds the class Surgeon '''
import models
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Surgeon(BaseModel, Base):
    ''' Object representation of a surgeon '''
    __tablename__ = "surgeons"
    name = Column(String(128), unique=True, nullable=False)
    contact_info = Column(Integer())
    #theatres = relationship("Theatre", backref="surgeon")
    theatre_id = Column(String(128), ForeignKey("theatres.id"), nullable=False)
    
    def __repr__(self):
        return f"Patient('{self.name}', '{self.contact_info}'"

    def __init__(self, *args, **kwargs):
        ''' Initializes the surgeon '''
        super().__init__(*args, **kwargs)
