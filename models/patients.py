''' Holds the class Patient '''
import models
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Patient(BaseModel, Base):
    ''' Object representation of a patient '''
    __tablename__ = "patients"
    name = Column(String(128), unique=True, nullable=False)
    contact_info = Column(Integer())
    #theatres = relationship("Theatre", backref="patient")
    theatre_id = Column(String(128), ForeignKey("theatres.id"), nullable=False)
    procedure_id = Column(String(128), ForeignKey("procedures.id"), nullable=False)

    def __repr__(self):
        return f"Patient('{self.name}', '{self.contact_info}', '{self.procedure_id}')"

    def __init__(self, *args, **kwargs):
        ''' Initializes the patient '''
        super().__init__(*args, **kwargs)
