from datetime import datetime
from . import main
from .forms import RegistrationForm, LoginForm
from .. import db, bcrypt
from Flask_BMT.models.users import User
from flask import Flask, render_template, url_for, flash, redirect
from flask_login import login_required, logout_user

@main.before_app_first_request
def create_tables():
    db.create_all()


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created successfully!", "success")
        return redirect(url_for("main.login"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error in creating a user: {err_msg}', category='danger')
    return render_template("register.html", form=form, title="Registration-page")


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.home')
            return redirect(next)
        flash("Invalid username or password.")
    return render_template("login.html", form=form, title="Login-page")
    # return redirect(url_for("main.lists"))


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.about_page'))

@main.route('/secret')
@login_required
def secret():
    return "Only authenticated users are allowed"


