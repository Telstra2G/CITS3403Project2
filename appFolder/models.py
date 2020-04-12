
from appFolder import db
from werkzeug.security import generate_password_hash, check_password_hash
#from sqlalchemy_utils import ChoiceType, EmailType
# Create User database model
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# first_name = db.Column(db.String(100))
	# last_name = db.Column(db.String(100))
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	# use a regular string field, for which we can specify a list of available choices later on
	# type = db.Column(db.String(100))
	
	
	# email = db.Column(EmailType, unique=True, nullable=False)	
	
	def __repr__(self):
		return '<User {}>'.format(self.username)
		
	def set_password(self, password):
		self.password = generate_password_hash(password)

	def get_password(self, password):
		return check_password_hash(self.password, password)


	

