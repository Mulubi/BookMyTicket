''' Holds the class Patient '''
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Patient(BaseModel, Base):
    ''' Object representation of a patient '''
    __tablename__ = "patients"
    name = Column(String(128), nullable=False)
    contact_info = Column(Integer())

    theatre_id = Column(Integer, ForeignKey("theatres.id"), nullable=False)
    theatres = relationship("Theatre", backref="patients")

    procedure_id = Column(String(128), ForeignKey("procedures.id"), nullable=False)
    procedures = relationship("Procedure", backref="patients", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        ''' Initializes the patient '''
        super().__init__(*args, **kwargs)