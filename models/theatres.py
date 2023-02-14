''' Holds the class Theatre '''
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Theatre(BaseModel, Base):
    ''' Object representation of a theatre '''
    __tablename__ = "theatres"
    name = Column(String(128), nullable=False)
    surgeon_id = Column(String(128), ForeignKey("surgeons.id"), nullable=False)
    patient_id = Column(String(128), ForeignKey("patients.id"), nullable=False)
    procedure_id = Column(String(128), ForeignKey("procedures.id"), nullable=False)
    anaesthetist_id = Column(String(128), ForeignKey("anaesthetists.id"), nullable=False)

    patients = relationship("Patient", backref="theatres", cascade="all, delete, delete-orphaned")
    procedures = relationship("Procedure", backref="theatres", cascade="all, delete, delete-orphaned")
    surgeons = relationship("Surgeon", backref="theatres", cascade="all, delete, delete-orphaned")
    anaesthetists = relationship("Anaesthetist", backref="theatres", cascade="all, delete, delete-orphaned")

    def __init__(self, *args, **kwargs):
        ''' Initializes the theatre '''
        super().__init__(*args, **kwargs)
