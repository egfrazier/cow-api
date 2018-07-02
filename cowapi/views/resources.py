import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from cowapi.models.db import get_db
import pymysql.cursors

from pprint import pprint

# Resource blueprint
bp = Blueprint('resources', __name__, url_prefix='/resources')

#Single State
@bp.route('/state/<int:state_id>')
def query_state(state_id):
	db = get_db()
	with g.db.cursor() as cursor:
		sql = "SELECT * FROM `state_codes` WHERE state_id = %d" % state_id
		cursor.execute(sql)
		return str(cursor.fetchall())

# All States
@bp.route('/states')
def query_states():
	db = get_db()
	with g.db.cursor() as cursor:
		sql = "SELECT * FROM `state_codes`"
		cursor.execute(sql)
		return str(cursor.fetchall())