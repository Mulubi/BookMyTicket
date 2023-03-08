from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors, auth, test, decorator

@main.app_context_processor
def inject_permissions():
	return dict(Permission=Permission)

