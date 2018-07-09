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
	g_db_dump = dir(g.db)
	print(g_db_dump)
	return g.db

def close_db(e=None):
	db = g.pop('db', None)

	if db is not None:
		db.close()

def init_db():
    db = get_db()

def init_app(app):
	app.teardown_appcontext(close_db)
	app.cli.add_command(init_db_command)

@click.command('init-db')
@with_appcontext
def init_db_command():
	init_db()
	click.echo('Connecting to database...')