from datetime import datetime
from flask import render_template, url_for, session, redirect
from . import main
from .forms import RegistrationForm, LoginForm
from .. import db, bcrypt
# from models import User
from Flask_BMT.models.users import User
from flask_login import login_required, login_user, logout_user

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
@login_required
def home_page():
    return render_template("home.html", title="Home-page")

@main.route('/about')
def about_page():
    return render_template("about.html", title="About-page")

@main.route('/theatre_list')
@login_required
def lists():
    return render_template("lists.html", title="Theatre-lists")

@main.route('/user/<username>')
def user(username):
    return '<h1> Hello, {}!</h1>'.format(username)


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")
