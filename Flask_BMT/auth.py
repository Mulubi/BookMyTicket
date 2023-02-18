from config import app
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Registration Page", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
        # if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            # flash(f'You have been logged in as Admin!', 'success')
            # return redirect(url_for('home'))
        # else:
            # flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title="Login Page", form=form)
