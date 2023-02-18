''' Holds the class Procedure '''
import models
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Procedure(BaseModel, Base):
    ''' Object representation of a procedure '''
    if models.storage_type == 'db':
        __tablename__ = "procedures"
        name = Column(String(128), unique=True, nullable=False)
        # patients = relationship("Patient", backref="procedure")
        # theatres = relationship("Theatre", backref="procedure")
        # theatre_id = Column(String(128), ForeignKey("theatres.id"), nullable=False)
        # patients = relationship("Patient", backref="procedure", lazy=True)
    else:
        name = ""

    def __repr__(self):
        return f"Procedure('{self.name}'"

    def __init__(self, *args, **kwargs):
        ''' Initializes the procedure '''
        super().__init__(*args, **kwargs)
