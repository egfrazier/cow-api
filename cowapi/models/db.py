import pymysql

import click
from flask import current_app as app
from flask import g
from flask.cli import with_appcontext

def get_db():
	if 'db' not in g:
		g.db = pymysql.connect(host=app.config['HOST'],
	                             user=app.config['USER'],
	                             password=app.config['PASSWORD'],
	                             db=app.config['DB'],
	                             charset=app.config['CHARSET'],
	                             cursorclass=pymysql.cursors.DictCursor)
		return g.db

def close_db(e=None):
	db = g.pop('db', None)

	if db is not None:
		g.db.close()

def init_db():
    db = get_db()

def init_app(app):
	app.cli.add_command(init_db_command)
	#app.teardown_appcontext(close_db)

@click.command('init-db')
@with_appcontext
def init_db_command():
	# In the Flaskr tutorial the init_db_command function would also contain code to
	# initially set up the Sqlite database, but that code is omited since
	# this database exists/persists independently on MySQL before, during and
	# after the app is started. Therefore, init_db_command funtion only contains
	# code to start a connection to the MySQL database.
	init_db()
	click.echo('Connecting to database...')