from datetime import datetime
from flask import render_template, url_for, session, redirect
from . import main
from .forms import RegistrationForm, LoginForm
from .. import db, bcrypt
# from models import User
from Flask_BMT.models.users import User

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
def home_page():
    return render_template("home.html", title="Home-page")


@main.route('/about')
def about_page():
    return render_template("about.html", title="About-page")

@main.route('/user/<username>')
def user(username):
    return '<h1> Hello, {}!</h1>'.format(username)



@main.route('/registerpage', methods=['GET', 'POST'])
def register_page():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(User)
		db.session.commit()
		flash(f"Your account has been created successfully!", "success")
		return redirect(url_for("login_page"))
	return render_template("register.html", form=form, title="Registration-page")
