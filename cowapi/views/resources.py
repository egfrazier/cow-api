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
bp = Blueprint('resources', __name__, url_prefix='/api/v1/resources')


@bp.route('/state/<int:state_id>')
def query_state(state_id):
	""" This function returns a JSON represntation
		response of the queried state.

		:param name: State ID.
		:type name: int.
		:returns: str -- the HTML view output.
	"""
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

# System membership tenure for a Given State
@bp.route('/system_tenure/<int:state_id>')
def system_tenure(state_id):
	""" This function returns a JSON representation
		response of the System membership tenure for a given
		state (by state_id).

		:param name: State ID.
		:type name: int.
		:returns: str -- the HTML view output.
	"""

	thisQuery = Query('system_tenure', state_id)
	thisQuery.send_query()
	response = thisQuery.pull_result()
	return render_template('response.html', response=response)

# Major Power Tenure for a Given State
@bp.route('/major_tenure/<int:state_id>')
def major_tenure(state_id):
	""" This function returns a JSON representation
		response of the Major tenure for a given
		state (by state_id) and designates any tenure
		where the state was a Major Power.

		:param name: State ID.
		:type name: int.
		:returns: str -- the HTML view output.
	"""

	thisQuery = Query('system_tenure', state_id)
	thisQuery.send_query()
	response = thisQuery.pull_result()
	return render_template('response.html', response=response)