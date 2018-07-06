import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from cowapi.models.db import get_db
from cowapi.models.models import State, Query
import pymysql.cursors

from pprint import pprint

# Resource blueprint
bp = Blueprint('resources', __name__, url_prefix='/resources')

# State
@bp.route('/state/<int:state_id>')
def query_state(state_id):
	thisQuery = Query('state', state_id)
	thisQuery.send_query()
	response = thisQuery.pull_result()
	return render_template('response.html', response=response)

# States
@bp.route('/states')
def query_states():
	thisQuery = Query('states')
	thisQuery.send_query()
	response = thisQuery.pull_result()
	return render_template('response.html', response=response)