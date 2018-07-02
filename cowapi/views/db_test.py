# Datebase connection test blueprint

import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from cowapi.models.db import get_db
import pymysql.cursors

from pprint import pprint

bp = Blueprint('db-test', __name__, url_prefix='/db_test')

@bp.route('/test')
#def db_test():
#	return "This is the DB test page."
def db_test():
	db = get_db()
	with g.db.cursor() as cursor:
		sql = "SELECT * FROM `state_codes`"
		cursor.execute(sql)
		return str(cursor.fetchall())