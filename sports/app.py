#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.login import login_required, login_user, current_user, logout_user
from flask import render_template, request, jsonify, make_response, Response, flash, redirect, session, url_for, g
from sports.models import Base, User, Prediction, Category, Option, Question, HasCategory
from sports import config

from sqlalchemy import desc, and_
from sqlalchemy.orm import load_only

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
db.Model = Base

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('dashboard'))

	form = LoginForm() if request.method == 'POST' else LoginForm(request.args)
	if form.validate_on_submit():

		user = db.session.query(User).filter_by(username=form.username.data).filter_by(password=form.pin.data).first()
		if user is None:
			flash('User does not exist, please register.')
			return redirect(url_for('welcome'))

		login_user(user)
		flash(('Logged in successfully.'))
		return redirect(url_for('dashboard'))
	return render_template('login.html', form=form)


@app.route('/welcome', methods=['GET'])
def welcome():	
	return "Hello"

@app.route('/home')
def home():
	questions = db.session.query(Question).filter_by(complete=False)
	return render_template('home.html', questions=questions)

@app.route('/trigger')
def trigger():
	print db.engine

	connection = db.engine.connect()
	string = "\\d sports_user"
	print string
	result = connection.execute("select * from information_schema.columns where table='sports_user'")
	for row in result:
		print "column:%r" % row['column']
	connection.close()
	return "hi"

