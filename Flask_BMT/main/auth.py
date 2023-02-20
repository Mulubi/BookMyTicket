from datetime import datetime
from . import main
from .forms import RegistrationForm, LoginForm
from .. import db
# from ..models import User
from flask import Flask, render_template, url_for, flash, redirect


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(User)
        db.session.commit()
        flash(f"Your account has been created successfully!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form, title="Registration-page")


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
        # if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            # flash(f'You have been logged in as Admin!', 'success')
            # return redirect(url_for('home'))
        # else:
            # flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return redirect(url_for("home"))
    return render_template("login.html", form=form, title="Login-page")

    