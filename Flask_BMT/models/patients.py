''' Holds the class Patient '''
from Flask_BMT import db, models
# from models import base_model
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

if models.storage_type == 'db':
    patient_booking = Table('patient_booking', Base.metadata,
        Column('patient_id', String(60), ForeignKey('patients.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        Column('procedure_id', String(60), ForeignKey('procedures.id', onupdate='CASCADE', ondelete='CASCADE')))


class Patient(BaseModel, Base):
    ''' Object representation of a patient '''
    #__abstract__ = True
    if models.storage_type == 'db':
        __tablename__ = "patients"
        name = Column(String(128), unique=True, nullable=False)
        contact_info = Column(String(60), nullable=False)
        theatre_id = Column(String(60), ForeignKey("theatres.id"), nullable=False)
        procedures = relationship("Procedure", secondary=patient_booking, backref="patient_bookings", cascade="delete",
            lazy="dynamic")

    else:
        name = ""
        contact_info = ""

    def __repr__(self):
        return f"Patient('{self.name}', '{self.contact_info}', '{self.procedures}')"

    def __init__(self, *args, **kwargs):
        ''' Initializes the patient '''
        super().__init__(*args, **kwargs)
