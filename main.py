import os
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from models.patients import Patient
from models.procedures import Procedure
from models.surgeons import Surgeon
from models.theatres import Theatre
from models.users import User
from models.anaesthetists import Anaesthetist

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#app.config['SECRET_KEY'] = '41ed75074dc9acfc44d3ca8ab3d6477f'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="Home-page") 

@app.route('/about')
def about_page():
    return render_template("about.html", title="About-page")

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
    #if form.validate_on_submit():
        #if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            #flash(f'You have been logged in as Admin!', 'success')
            #return redirect(url_for('home'))
        #else:
            #flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title="Login Page", form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)