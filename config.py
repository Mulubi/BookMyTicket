from models.patients import Patient
from models.procedures import Procedure
from models.surgeons import Surgeon
from models.theatres import Theatre
from models.users import User
from models.anaesthetists import Anaesthetist
from Flask_BMT import app, db

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)