''' Holds the class Procedure '''
from Flask_BMT import db, models
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Procedure(BaseModel, Base):
    ''' Object representation of a procedure '''
    #__abstract__ = True
    if models.storage_type == 'db':
        __tablename__ = "procedures"
        name = Column(String(128), unique=True, nullable=False)
        requirements = Column(String(1024), nullable=True)
        #patients = relationship("Patient", secondary=patient_bookings, backref=backref("procedures", lazy="dynamic"),
            #lazy="dynamic")
    else:
        name = ""
        requirements = ""

    def __repr__(self):
        return f"Procedure('{self.name}'"

    def __init__(self, *args, **kwargs):
        ''' Initializes the procedure '''
        super().__init__(*args, **kwargs)
