from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User, Char_sheet
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Homepage')


@app.route('/login')
def login():
    return render_template("login.html", title='Log in')


@app.route('/signup')
def signup():
    return render_template("login.html", title='Sign up')


@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact us')


