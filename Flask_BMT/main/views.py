from datetime import datetime
from flask import render_template, url_for, session, redirect, flash, request
from . import main
from .forms import RegistrationForm, LoginForm, TheatreForm
from .. import db, bcrypt
# from models import User
from Flask_BMT.models.users import User
from Flask_BMT.models.theatres import TheatreList
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


@main.route('/lists', methods=['GET', 'POST'])
@login_required
def list_page():
	patient_name = None
	form = TheatreForm()
	if request.method == 'POST':
		patient_name = request.form['patient_name']
		procedure_time = request.form['procedure_time']
		procedure_name = request.form['procedure_name']
		surgeon = request.form['surgeon']
		anaesthetist = request.form['anaesthetist']
		#return redirect(url_for('main.lists'))
	return render_template("list_page.html", patient_name=patient_name, form=form)

@main.route('/theatre_list', methods=['GET', 'POST'])
@login_required
def lists():
	patient_name = None
	form = TheatreForm()
	if form.validate_on_submit():
		booking = TheatreList.query.filter_by(patient_name=form.patient_name.data).first()
		if booking is None:
			theatre_list = TheatreList(procedure_time=form.procedure_time.data,
								patient_name=form.patient_name.data,
								procedure_name=form.procedure_name.data,
								surgeon=form.surgeon.data,
								anaesthetist=form.anaesthetists.data)
			db.session.add(theatre_list)
			db.session.commit()
		patient_name = form.patient_name.data
		form.procedure_time.data = ''
		form.patient_name.data = ''
		form.procedure_name.data = ''
		form.surgeon.data = ''
		form.anaesthetist.data = ''
		flash("Booking added successfully!")
	our_bookings = TheatreList.query.order_by(TheatreList.procedure_time)
	return render_template("theatre_lists.html", form=form, patient_name=patient_name, title="Theatre-lists", our_bookings=our_bookings)

@main.route('/user/<username>', methods=['GET', 'POST'])
def user_page(username):
	username = None
	return render_template("user.html", username=username)


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

