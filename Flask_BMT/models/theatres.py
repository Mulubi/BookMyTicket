''' Holds the class Theatre '''
from Flask_BMT import db, models
from .base_model import BaseModel, Base, BaseModelMixin
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Theatre(db.Model, BaseModelMixin):
    ''' Object representation of a theatre '''
    __abstract__ = True
    if models.storage_type == 'db':
        __tablename__ = "theatres"
        name = Column(String(128), unique=True, nullable=False)
        #surgeon_id = Column(String(128), ForeignKey("surgeons.id"), nullable=False)
        #patient_id = Column(String(128), ForeignKey("patients.id"), nullable=False)
        #procedure_id = Column(String(128), ForeignKey("procedures.id"), nullable=False)
        #anaesthetist_id = Column(String(128), ForeignKey("anaesthetists.id"), nullable=False)

        #patients = relationship("Patient", backref="theatre", lazy=True)
        #procedures = relationship("Procedure", backref="theatre", lazy=True)
        #surgeons = relationship("Surgeon", backref="theatre", lazy=True)
        #anaesthetists = relationship("Anaesthetist", backref="theatre", lazy=True)
    else:
        name = ""

    def __repr__(self):
        return f"Theatre('{self.name}'"

    def __init__(self, *args, **kwargs):
        ''' Initializes the theatre '''
        super().__init__(*args, **kwargs)
