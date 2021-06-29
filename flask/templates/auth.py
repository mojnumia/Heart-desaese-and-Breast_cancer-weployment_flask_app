from flask import Blueprint,render_template
auth=Blueprint("auth", __name__)
@auth.route('/signup')
def signup():
	return render_template('signup.html')

@auth.route('/login')
def login():
	return "login"

@auth.route('/logout')
def logout():
	return "logout here"