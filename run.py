import os

from Flask_BMT import create_app, db
from Flask_BMT.models.base_model import BaseModel, Base
from Flask_BMT.models.patients import Patient
from Flask_BMT.models.procedures import Procedure
from Flask_BMT.models.surgeons import Surgeon
from Flask_BMT.models.theatres import Theatre
from Flask_BMT.models.users import User
from Flask_BMT.models.anaesthetists import Anaesthetist
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Patient=Patient, Procedure=Procedure,
    			Surgeon=Surgeon, Theatre=Theatre, User=User,
    			Anaesthetist=Anaesthetist)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True) 