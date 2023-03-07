''' Holds the class Theatre '''
from Flask_BMT import db, models
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, String, ForeignKey, Table
from sqlalchemy.orm import relationship

if models.storage_type == 'db':
    theatre_procedure = Table('theatre_procedure', Base.metadata,
        Column('theatre_id', String(60), ForeignKey('theatres.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        Column('procedure_id', String(60), ForeignKey('procedures.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True))

    theatre_surgeon = Table('theatre_surgeon', Base.metadata,
        Column('theatre_id', String(60), ForeignKey('theatres.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        Column('surgeon_id', String(60), ForeignKey('surgeons.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True))

    theatre_anaesthetist = Table('theatre_anaesthetist', Base.metadata,
        Column('theatre_id', String(60), ForeignKey('theatres.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        Column('anaesthetist_id', String(60), ForeignKey('anaesthetists.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True))


class Theatre(BaseModel, Base):
    ''' Object representation of a theatre '''
    #__abstract__ = True
    if models.storage_type == 'db':
        __tablename__ = "theatres"
        name = Column(String(128), unique=True, nullable=False)
        procedures = relationship("Procedure", secondary=theatre_procedure, backref="theatre_procedures",
            lazy="dynamic")
        surgeons = relationship("Surgeon", secondary=theatre_surgeon, backref="theatre_surgeons",
            lazy="dynamic")
        anesthetists = relationship("Anaesthetist", secondary=theatre_anaesthetist, backref="theatre_anaesthetists",
            lazy="dynamic")
        patients = relationship("Patient", backref="theatre", lazy="dynamic", cascade="delete")
    else:
        name = ""

    def __repr__(self):
        return f"Theatre('{self.name}'"

    def __init__(self, *args, **kwargs):
        ''' Initializes the theatre '''
        super().__init__(*args, **kwargs)
