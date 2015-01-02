Vote on Questions
•	Specific players
•	Games
•	Stats

Betting on Reputation
Leaderboard
Profile – type of questions
User management system
Questions based on ranking
User 


Users
Questions 
User Question Interactions
Categories


Data Structure:

Debating between PyMongo vs. Postgresql
=======================================

We need to be able to:
---------------------
	query all questions
	query all questions that have been answered by a given user
	query all unanswered questions
	query all answered questions
	query questions sorted by the most given answers (most popular vs least popular)
	query a user's win perecentage (% right vs % wrong)
	query users with the highest win percentage
	query all responses for a given question
	query a question's win percentage
	query total number of votes

Users:
	location
	email
	first name
	last name
	username
	password (SHA-1 encrypted)
	join date
	power ranking
	role
	last logged in

Questions:
	array of possible answers
	correct answer
	date posted
	date answered
	weight
	question status (active, hidden, done, etc.)
	array of categories

User Answers:

	

PyMongo Wins
