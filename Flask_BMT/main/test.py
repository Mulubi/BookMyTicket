from datetime import datetime
from . import main
from .forms import RegistrationForm, LoginForm, PasswordForm
from .. import db, bcrypt
from Flask_BMT.models.users import User
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


@main.route('/test_pw', methods=['GET', 'POST'])
def test_pw():
    email = None
    password = None
    pw_to_check = None
    passed = None
    form = PasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password_hash.data

        form.email.data = ''
        form.password_hash.data = ''

        pw_to_check = User.query.filter_by(email=email).first()
        passed = check_password_hash(pw_to_check.password_hash, password)

    return render_template("test_pw.html", email = email, password = password, pw_to_check = pw_to_check, form = form)
    # return redirect(url_for("main.lists"))