import os

from flask 		import Flask, url_for, request, session
from flask_admin 	import Admin, BaseView, expose
from flask_login	import LoginManager
from flask_sqlalchemy 	import SQLAlchemy
from flask_migrate 	import Migrate

class MyView(BaseView):
	@expose('/')
	def index(self):
		# Get URL for the test view method
		url = url_for('.test')
		return self.render('index.html', url=url)
	@expose('/test/')
	def test(self):
		return self.render('test.html')

# Define the WSGI application object
app = Flask(__name__)

# Initiating a database 
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Configurations
#app.config.from_object('config')

admin = Admin(app, name="Admin Dashboard")
#add_view adds a button(Hello) on the navigation bar
admin.add_view(MyView(name='Hello'))
admin.add_view(MyView(name='Practice', endpoint='practice', category='Student'))
admin.add_view(MyView(name='Test', endpoint='Test', category='Student'))



from appFolder import routes, models
