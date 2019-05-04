import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from cowapi.models.db import get_db
from cowapi.models.models import State, Query, System_year
import pymysql.cursors

from pprint import pprint
import json
from flask import jsonify

# Resource blueprint
bp = Blueprint('resources', __name__, url_prefix='/api/v1/resources')

# State
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
	return jsonify(response)
	#return render_template('response.html', response=response)

# States
@bp.route('/states')
def query_states():
	thisQuery = Query('states')
	thisQuery.send_query()
	response = thisQuery.pull_result()
	return jsonify(response)
	#return render_template('response.html', response=response)

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
	return jsonify(response)
	#return render_template('response.html', response=response)

@bp.route('/system_year/<int:year>')
def system_year(year):
	""" This function returns a JSON representation
		response of a list of all members of the
		international state system for a given year.
		
		TODO: Add a Boolean property identifying whether
		the state was or was not a Major Power that
		year.
	"""
	this_query = Query('system_year', year)
	this_query.send_query()
	response = this_query.pull_result()
	return jsonify(response)
	#return render_template('response.html', response=response)


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

	thisQuery = Query('major_tenure', state_id)
	thisQuery.send_query()
	response = thisQuery.pull_result()
	return jsonify(response)
	#return render_template('response.html', response=response)

# TODO: Major Powers by Year

# TODO: Future resources:
	# - All extra state wars
	# - Extrastate wars by ID

@bp.route('/wars/nonstate/', defaults={'req_war_id': None})
@bp.route('/wars/nonstate/<int:req_war_id>')
def query_nonstate_wars(req_war_id):
	""" This function returns a JSON representation
		response of a nonstate war. If no war_id
		argument is passed in, then all nonstate wars
		are returned.
	"""
	this_query = Query('nonstate', req_war_id)
	this_query.send_query()
	response = this_query.pull_result()
	return jsonify(response)
	#return render_template('response.html', response=response)

@bp.route('/wars/intrastate/', defaults={'req_war_id': None})
@bp.route('/wars/intrastate/<int:req_war_id>')
def query_intrastate_wars(req_war_id):
	""" This function returns a JSON representation
		response of a intrastate war. If no war_id
		argument is passed in, then all intrastate wars
		are returned.
	"""
	this_query = Query('intrastate', req_war_id)
	this_query.send_query()
	response = this_query.pull_result()
	return jsonify(response)
	#return render_template('response.html', response=response)

@bp.route('/wars/interstate/', defaults={'req_war_id': None})
@bp.route('/wars/interstate/<int:req_war_id>')
def query_interstate_wars(req_war_id):
	""" This function returns a JSON representation
		response of a interstate war. If no war_id
		argument is passed in, then all interstate wars
		are returned.
	"""
	this_query = Query('interstate', req_war_id)
	this_query.send_query()
	response = this_query.pull_result()
	return jsonify(response)
	#return render_template('response.html', response=response)

@bp.route('/wars/extrastate/', defaults={'req_war_id': None})
@bp.route('/wars/extrastate/<int:req_war_id>')
def query_extrastate_wars(req_war_id):
	""" This function returns a JSON representation
		response of a extrastate war. If no war_id
		argument is passed in, then all extrastate wars
		are returned.
	"""
	this_query = Query('extrastate', req_war_id)
	this_query.send_query()
	response = this_query.pull_result()
	#response = json.dumps(response)
	return jsonify(response)


# TODO: Basic search query string funcionality on each of these endpoints