# import flask and templates
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

app.config.from_object('config')

# TODO: Mongo Client
#db = MongoClient(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])

@app.errorhandler(404)
def not_found(error):
	#TODO: build 404 page
	return render_template('404.html'), 404

# initialize user interactions

# import modules and components via blueprint object variable
from app.mod_user.controllers import mod_user as user_module
from app.mod_question.controllers import mod_question as question_module
from app.mod_home.controllers import mod_home as home_module
from app.mod_admin.controllers import mod_admin as admin_module

# register blueprints
app.register_blueprint(user_module)
app.register_blueprint(question_module)
app.register_blueprint(home_module)
app.register_blueprint(admin_module)