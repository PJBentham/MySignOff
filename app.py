from flask import (Flask, g, render_template, flash, redirect, url_for)
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import LoginManager, login_user

import forms
import models

DEBUG = True
PORT = 8080
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'kjheruieveqw7863414756___$%^'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'

@login_manager.user_loader
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None

@app.before_request
def before_request():
	"""Connect to the database before each request"""
	g.db = models.DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	"""Close the database connection after each request"""
	g.db.close()
	return response

@app.route('/', methods=['GET', 'POST'])
def index():
	form = forms.LoginForm()
	form2 = forms.InterestedForm()
	if form.validate_on_submit():
		try:
			user = models.User.get(models.User.email == form.email.data)
		except models.DoesNotExist:
			flash("Your email or password doesn't match!", "error")
		else:
			if check_password_hash(user.password, form.password.data):
				login_user(user)
				flash("You've been logged in", "success")
				return redirect(url_for('index'))
			else:
				flash("Your email or password doesn't match!", "error")
	return render_template('home.html', form=form, form2=form2)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = forms.RegistrationForm()
	if form.validate_on_submit():
		flash("Registration Succesful!", "success")
		models.User.create_user(
			username=form.username.data,
			email=form.email.data,
			password=form.password.data
			)
		return redirect(url_for('index'))
	return render_template('register.html', form=form)

# @app.route('/User')

# @app.route('/User/Project')


if __name__ == '__main__':
	models.initialize()
	try:
		models.User.create_user(
			username='paulbentham',
			email='pjbentham@gmail.com',
			password='admin',
			admin=True
			)
	except ValueError:
		pass
	app.run(debug=DEBUG, host=HOST, port=PORT)
