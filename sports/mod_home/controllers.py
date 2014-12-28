from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app.mod_home import helper

# initialize module, set url
mod_home = Blueprint('home', __name__, url_prefix='')


@mod_home.route('/', methods=['GET'])
def index():
	# landing page, same for all users, but include session

@login_required
@mod_home.route('/dashboard', methods = ['GET'])
def dashboard():
	# the view that a logged in user sees
	# sees popular questions,
	# new questions, personal data

