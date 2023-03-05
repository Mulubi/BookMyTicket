''' Holds the class Patient '''
from Flask_BMT import db, models
# from models import base_model
from .base_model import BaseModel, Base, BaseModelMixin
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Patient(db.Model, BaseModelMixin):
    ''' Object representation of a patient '''
    __abstract__ = True
    if models.storage_type == 'db':
        __tablename__ = "patients"
        name = db.Column(db.String(128), unique=True, nullable=False)
        contact_info = db.Column(db.String(50), nullable=False)
        # theatres = relationship("Theatre", backref="patient")
        # theatre_id = Column(String(128), ForeignKey("theatres.id"), nullable=False)
        current_procedure = relationship("Procedure", backref="current_patient")
        procedure_id = db.Column(db.Integer(128), db.ForeignKey("procedures.id"), nullable=False)

    else:
        name = ""
        contact_info = ""

    def __repr__(self):
        return f"Patient('{self.name}', '{self.contact_info}', '{self.procedure_id}')"

    def __init__(self, *args, **kwargs):
        ''' Initializes the patient '''
        super().__init__(*args, **kwargs)
