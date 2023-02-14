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

    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    patients = relationship("Patient", backref="procedures")

    theatre_id = Column(Integer, ForeignKey("theatres.id"), nullable=False)
    theatres = relationship("Theatre", backref="procedures")
    
    def __init__(self, *args, **kwargs):
        ''' Initializes the procedure '''
        super().__init__(*args, **kwargs)
