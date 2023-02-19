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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Registration Page", form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
        # if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            # flash(f'You have been logged in as Admin!', 'success')
            # return redirect(url_for('home'))
        # else:
            # flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title="Login Page", form=form)
