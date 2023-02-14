''' Holds the class Anaesthetist '''
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Anaesthetist(BaseModel, Base):
    ''' Object representation of an anaesthetist '''
    __tablename__ = "anaesthetists"
    name = Column(String(128), nullable=False)
    contact_info = Column(Integer())
    theatres = relationship("Theatre", backref="anaesthetist")
    
    def __init__(self, *args, **kwargs):
        ''' Initializes the anaesthetist '''
        super().__init__(*args, **kwargs)
