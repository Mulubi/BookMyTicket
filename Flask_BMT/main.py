import os
from models.patients import Patient
from models.procedures import Procedure
from models.surgeons import Surgeon
from models.theatres import Theatre
from models.users import User
from models.anaesthetists import Anaesthetist

# basedir = os.path.abspath(os.path.dirname(__file__))


from config import app, db

from models import auth

import routes




