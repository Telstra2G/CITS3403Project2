# MAIN ENTRY: Run the app
from appFolder import app, db
from appFolder.models import User

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User}
#app.run(debug=False)


# Run a test server.
#from appFolder import app
#app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == "__main__":
	app.run()
