from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Home page html goes here"

@app.route('/about')
def about_page():
    return "About Page html goes here"