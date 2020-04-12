
from appFolder import app, db
from flask import Markup, send_file, flash, json, redirect, render_template, request, Response
from appFolder.models import User
#from appFolder.models import LoginForm, RegisterForm

 
# Creating some default routes
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', index=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit()==True:
		if request.form.get('email') == 'test@uta.com':
			flash('You are successfully logged in!', 'success')
			return redirect('index')
		else:
			flash('Something went terribly wrong.', 'danger')
	return render_template('login.html', form=form, login=True, title='Login')


@app.route('/register')
def register():
	form = RegisterForm()
	return render_template('register.html', form=form, register=True)
	
@app.route('/users')
def user():
	users = User.objects.all()
	return render_template('users.html', users=users)


