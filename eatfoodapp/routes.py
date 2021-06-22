from eatfoodapp import app
from flask import render_template

@app.route('/')
def home():
	heading = "Let's Eat!"
	subheading = "Here are some foods"
	foods = ['pasta','pizza','salad','dessert']
	return render_template('home.html', heading=heading, subheading=subheading, foods=foods)