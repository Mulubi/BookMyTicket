from datetime import datetime
from flask import render_template, url_for, session, redirect
from . import main
from .forms import RegistrationForm, LoginForm, TheatreForm
from .. import db, bcrypt
# from models import User
from Flask_BMT.models.users import User
from flask_login import login_required, login_user, logout_user
from Flask_BMT.main.decorator import admin_required, permission_required

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
#@login_required
def home_page():
    return render_template("home.html", title="Home-page")

@main.route('/about')
def about_page():
    return render_template("about.html", title="About-page")

@main.route('/theatre_list', methods=['GET', 'POST'])
@login_required
def lists():
	form = TheatreForm()
	if form.validate_on_submit():
		theatre_list = Theatre(procedure_time=form.procedure_time.data,
								patient_name=form.patient_name.data,
								procedure_name=form.procedure_name.data,
								surgeon=form.surgeon.data,
								anaesthetist=form.anaesthetists.data)
		form.procedure_time.data = ''
		form.patient_name.data = ''
		form.procedure_name.data = ''
		form.surgeon.data = ''
		form.anaesthetist.data = ''

		db.session.add(theatre_list)
		db.session.commit()

		flash("Booking added successfully!")
	return render_template("lists.html", form=form, title="Theatre-lists")

@main.route('/user/<username>')
def user(username):
    return '<h1> Hello, {}!</h1>'.format(username)


@main.route('/dashboard', methods=['GET', 'POST'])
#@login_required
def dashboard():
	#form = DashboardForm()
	return render_template("dashboard.html", form=form)

@main.route('/admin')
@login_required
@admin_required
def admin_page():
    return render_template("admin.html")

@main.route('/moderate')
@login_required
@permission_required
def moderators_page():
    return 'For Moderators!'

