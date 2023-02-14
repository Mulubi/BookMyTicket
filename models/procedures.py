''' Holds the class Procedure '''
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Procedure(BaseModel, Base):
    ''' Object representation of a procedure '''
    __tablename__ = "procedures"
    name = Column(String(128), nullable=False)
    patients = relationship("Patient", backref="procedure")
    theatres = relationship("Theatre", backref="procedure")
    
    def __init__(self, *args, **kwargs):
        ''' Initializes the procedure '''
        super().__init__(*args, **kwargs)
