''' Holds the class Surgeon '''
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Surgeon(BaseModel, Base):
    ''' Object representation of a surgeon '''
    __tablename__ = "surgeons"
    name = Column(String(128), nullable=False)
    contact_info = Column(Integer())

    theatre_id = Column(Integer, ForeignKey("theatres.id"), nullable=False)
    theatres = relationship("Theatre", backref="surgeons")
    
    def __init__(self, *args, **kwargs):
        ''' Initializes the surgeon '''
        super().__init__(*args, **kwargs)
