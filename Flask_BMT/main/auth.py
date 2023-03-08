from datetime import datetime
from . import main
from .forms import RegistrationForm, LoginForm
from .. import db, bcrypt
from .. import login_manager
from Flask_BMT.models.users import User
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:   
            hashed_password = generate_password_hash(form.password_hash.data)
            user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password_hash=hashed_password)
            db.session.add(user)
            db.session.commit()
            #conn.execute("INSERT INTO users (first_name, last_name, email, password_hash) VALUES (?, ?, ?, ?)", (first_name, last_name, email, password_hash))
            #conn.commit()
        form.first_name.data = ''
        form.last_name.data = ''
        form.email.data = ''
        form.password_hash.data = ''

        flash(f"Your account has been created successfully!", "success")
        return redirect(url_for('main.login'))
    return render_template("register.html", form=form, title="Registration-page")


@main.route('/login2', methods=['GET', 'POST'])
def login2():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password_hash.data):
                login_user(user)
                flash("Success! You are logged in!", category='success')
                return redirect(url_for('main.home_page'))
            else:
                flash('Wrong Password.Try again!')
        else:
            flash("Invalid username or password.", category='danger')
    return render_template("login.html", form=form)
    # return redirect(url_for("main.lists"))

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password_hash.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.home_page')
                flash("Success! You are logged in!", category='success')
            else:
                flash('Wrong Password.Try again!')
            return redirect(next)
        else:
            flash("Invalid username or password.", category='danger')
    return render_template("login.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@main.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.login'))

@main.route('/secret')
@login_required
def secret():
    return "Only authenticated users are allowed"

