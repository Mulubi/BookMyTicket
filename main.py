from flask import Flask
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '41ed75074dc9acfc44d3ca8ab3d6477f'

@app.route('/')
@app.route('/home')
def home():
    return "Home page html goes here"

@app.route('/about')
def about_page():
    return "About Page html goes here"

@app.route('/register')
def register():
    form = RegistrationForm()
    return "register html goes here"

@app.route('/login')
def login():
    form = LoginForm()
    return "login html goes here"


if __name__ == "__main__":
    app.run()