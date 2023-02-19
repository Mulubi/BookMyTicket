from datetime import datetime
from flask import render_template, url_for, session, redirect
from . import main
from .forms import RegistrationForm, LoginForm
from .. import db
# from models import User
from Flask_BMT.models.users import User

# from jinja2 import FileSystemLoader

# app.jinja_loader = FileSystemLoader('BookMyTicket/Flask_BMT/templates')


@main.route('/user', methods=['GET', 'POST'])
def index():
	form = NameForm
	if form.validate_on_submit():
		# ...
		return redirect(url_for('index'))
	return render_template('index.html',
						form=form,
						name=session.get('name'),
						known=session.get('known', False),
						current_time=datetime.utcnow())


@main.route('/')
@main.route('/home')
def home():
    return render_template("home.html", title="Home-page")


@main.route('/about')
def about_page():
    return render_template("about.html", title="About-page")

@main.route('/user/<username>')
def user(username):
    return '<h1> Hello, {}!</h1>'.format(username)
