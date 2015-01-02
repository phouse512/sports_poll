from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app.mod_home import helper

# initialize module, set url
mod_admin = Blueprint('admin', __name__, url_prefix='/admin')


@mod_admin.route('/', methods=['GET'])
def index():
	# landing page, same for all users, but include session

@login_required
@mod_home.route('/dashboard', methods = ['GET'])
def dashboard():
	# the view that a logged in user sees
	# sees popular questions,
	# new questions, personal data

# create user route
@login_required
@mod_admin.route('/user', methods=['GET', 'POST'])
def create_user():
	

### desired routes

# crud interface for users
## create users
## edit users
## delete users

# crud interface for questions
## create questions
## update questions
