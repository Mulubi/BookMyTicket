from flask import render_template, url_for, flash, redirect
from Flask_BMT import app
# from jinja2 import FileSystemLoader

# app.jinja_loader = FileSystemLoader('BookMyTicket/Flask_BMT/templates')

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="Home-page")


@app.route('/about')
def about_page():
    return render_template("about.html", title="About-page")