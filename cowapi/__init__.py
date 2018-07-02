import os

from flask import Flask

def create_app(test_config=None):	# Application factory function
	#create and configure the app
	app = Flask('cowapi', instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev'
	)

	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass


	# ROUTES 

	# a basic info page
	@app.route('/')
	def basic_info():
		return 'Welcome to the Correlates of War API.'

	# Return data for all states
	@app.route('/api/v1/resources/states')
	def states_api():
		return 'Returns basic data for all states that have been in the system'

	from cowapi.models import db
	db.init_app(app)

	from cowapi.views import db_test
	app.register_blueprint(views.db_test.bp)

	from cowapi.views import resources
	app.register_blueprint(views.resources.bp)

	return app