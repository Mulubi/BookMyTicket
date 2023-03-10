from datetime import datetime, date
from flask import render_template, url_for, session, redirect, flash, request
from . import main
from .forms import RegistrationForm, LoginForm, TheatreForm, DashboardForm, TheatreAddForm
from .. import db, bcrypt
# from models import User
from Flask_BMT.models.users import User
from Flask_BMT.models.theatres import TheatreList
from flask_login import login_required, login_user, logout_user, current_user
from Flask_BMT.main.decorator import admin_required, permission_required

# from jinja2 import FileSystemLoader

# app.jinja_loader = FileSystemLoader('BookMyTicket/Flask_BMT/templates')



@main.route('/')
@main.route('/home')
def home_page():
    return render_template("home.html", title="Home-page")


@main.route('/about')
def about_page():
    return render_template("about.html", title="About-page")


@main.route('/theatre-lists', methods=['GET', 'POST'])
@login_required
def theatre_lists():
    bookings = TheatreList.query.order_by(TheatreList.procedure_time)
    return render_template("lists.html", bookings=bookings)


@main.route('/theatre-lists/<int:id>')
@login_required
def theatre_list(id):
    booking = TheatreList.query.get_or_404(id)
    return render_template("list.html", booking=booking)


@main.route('/theatre-lists/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_theatre_list(id):
    booking = TheatreList.query.get_or_404(id)
    form = TheatreAddForm()
    if form.validate_on_submit():
        booking.procedure_time = form.procedure_time.data
        booking.patient_name = form.patient_name.data
        booking.procedure_name = form.procedure_name.data
        booking.surgeon = form.surgeon.data
        booking.anaesthetist = form.anaesthetist.data
        db.session.add(booking)
        db.session.commit()
        flash("Booking has been updated!")
        return redirect(url_for('main.theatre_list', id=booking.id))
    return render_template('edit_theatre_list.html', form=form, booking=booking)


@main.route('/add-list', methods=['GET', 'POST'])
@login_required
def add_lists():
    patient_name = None
    procedure_time = None
    procedure_name = None
    surgeon = None
    anaesthetist = None
    form = TheatreAddForm()
    if request.method == 'POST':
        booking = TheatreList.query.filter_by(
            patient_name=form.patient_name.data).first()
        if booking is None:
            booking = TheatreList(procedure_time=request.form['procedure_time'],
                                       patient_name=request.form['patient_name'],
                                       procedure_name=request.form['procedure_name'],
                                       surgeon=request.form['surgeon'],
                                       anaesthetist=request.form['anaesthetist'])
            db.session.add(booking)
            db.session.commit()
        flash("Booking added successfully!")
    our_bookings = TheatreList.query.order_by(TheatreList.procedure_time)
    return render_template("add_lists.html", patient_name=patient_name,
                           procedure_time=procedure_time, procedure_name=procedure_name,
                           surgeon=surgeon, anaesthetist=anaesthetist, form=form, our_bookings=our_bookings)


@main.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user_page(username):
    #username = None
    return render_template("user.html", username=username)


@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = DashboardForm()
    return render_template("dashboard.html", form=form)


@main.route('/admin')
@login_required
#@admin_required
def admin_page():
    id = current_user.id
    if id == 2:
        return render_template("admin.html")
    else:
        flash("Sorry, you must be an admin. However, that doesn't stop you from checking the bookings today!")
        return redirect(url_for('main.theatre_lists'))


@main.route('/moderate')
@login_required
@permission_required
def moderators_page():
    return 'For Moderators!'
