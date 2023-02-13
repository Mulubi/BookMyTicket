from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '41ed75074dc9acfc44d3ca8ab3d6477f'

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
    return render_template("login.html", title="Login Page", form=form)


if __name__ == "__main__":
    app.run(debug=True)