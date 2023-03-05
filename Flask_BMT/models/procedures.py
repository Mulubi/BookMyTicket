''' Holds the class Procedure '''
from Flask_BMT import db, models
from .base_model import BaseModel, Base, BaseModelMixin
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Procedure(db.Model, BaseModelMixin):
    ''' Object representation of a procedure '''
    __abstract__ = True
    if models.storage_type == 'db':
        __tablename__ = "procedures"
        name = db.Column(String(128), unique=True, nullable=False)
        # patients = relationship("Patient", backref="procedure")
        # theatres = relationship("Theatre", backref="procedure", lazy=True)
        # theatre_id = Column(String(128), ForeignKey("theatres.id"), nullable=False)
        patient_id = db.Column(Integer(128), db.ForeignKey("patients.id"), nullable=False)
        patients = db.relationship("Patient", backref="procedure")
    else:
        name = ""

    def __repr__(self):
        return f"Procedure('{self.name}'"

    def __init__(self, *args, **kwargs):
        ''' Initializes the procedure '''
        super().__init__(*args, **kwargs)
