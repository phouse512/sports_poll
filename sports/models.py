from datetime import datetime
import os
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship, synonym, backref

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

""" User """
class User(Base):
	__tablename__ = 'sports_user'

	id = Column(Integer, primary_key=True)
	username = Column(String(200))
	password = Column(String(100))

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % self.username

""" Prediction """
class Prediction(Base):
	__tablename__ = 'prediction'

	id = Column(Integer, primary_key=True)
	score = Column(Integer)
	choice = Column(String)
	correct = Column(Boolean)
	user_id = Column(Integer, ForeignKey('sports_user.id'))
	user = relationship("User", backref=backref('predictor', order_by=id))
	question_id = Column(Integer, ForeignKey('question.id'))
	question = relationship("Question", backref=backref('question', order_by=id))

	def __init__(self, score, choice, user_id, question_id):
		self.score = score
		self.choice = choice
		self.user_id = user_id
		self.question_id = question_id

	def __repr__(self):
		return '<Prediction %r>' % self.choice

""" Category """ 
class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key=True)
	name = Column(String)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '<Category %r>' % self.name

""" Option """
class Option(Base):
	__tablename__ = 'option'

	id = Column(Integer, primary_key=True)
	choice_text = Column(String)
	choice_number = Column(Integer)
	question_id = Column(Integer, ForeignKey('question.id'))
	question = relationship("Question",backref=backref('question_origin', order_by=id))

	def __init__(self,choice_text,choice_number,question_id):
		self.choice_text = choice_text
		self.choice_Number = choice_number
		self.question_id = question_id

""" Question """
class Question(Base):
	__tablename__ = 'question'

	id = Column(Integer, primary_key = True)
	complete = Column(Boolean)
	right_answer = Column(Integer)
	prompt = Column(String)
	weight = Column(Integer)
	time = Column(DateTime)

	def __init__(self,right_answer,prompt,weight):
		self.complete = False
		self.right_answer = right_answer
		self.prompt = prompt
		self.weight = weight
		self.time = datetime.now()

""" HasCategory """
class HasCategory(Base):
	__tablename__ = 'has_category'

	id = Column(Integer, primary_key = True)
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship("Category", backref=backref('category_owner', order_by=id))
	question_id = Column(Integer, ForeignKey('question.id'))
	question = relationship("Question", backref=backref('question_owner', order_by=id))

	def __init__ (self, category_id, question_id):
		self.category_id = category_id
		self.question_id = question_id

if __name__ == '__main__':
	#from datetime import timedelta

	from sqlalchemy import create_engine
	from sqlalchemy.orm import sessionmaker

	#PWD = os.path.abspath(os.curdir)

	engine = create_engine('postgres://PhilipHouse:house@localhost/sports', echo=True)

	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	session = Session()

	user = User('phouse512', 'pmh518')

	session.add(user)
	session.commit()
