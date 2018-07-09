from cowapi.models.db import get_db
import json

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)

class Query:
	def __init__(self, resource_name, resource_id=None, result_body=None):
		self.resource_name = resource_name
		self.resource_id = resource_id

	def send_query(self):
		# Query for the State Resource
		if self.resource_name == 'state':
			thisState = State(self.resource_id)
			db = get_db()
			with g.db.cursor() as cursor:
				sql = "SELECT state_name, state_abbr FROM `state_codes` WHERE state_id = %d" % thisState.state_id
				cursor.execute(sql)
				result = cursor.fetchone()
				if cursor.rowcount == 0:
					self.result_body = {"results" : "No results"}
				else:
					thisState.state_name = result['state_name']
					thisState.state_abbr = result['state_abbr']
					self.result_body = {"results": {"State Name" : thisState.state_name, "State ID" : thisState.state_id, "State Abbr": thisState.state_abbr}}

		# Query for the States Resource
		if self.resource_name == 'states':
			self.result_body = { "results" : []}
			db = get_db()
			with g.db.cursor() as cursor:
				sql = "SELECT * FROM `state_codes`"
				cursor.execute(sql)
				result = cursor.fetchall()
				if cursor.rowcount == 0:
					self.result_body = {"results" : "No results"}
				else:
					for row in result:
						self.result_body['results'].append(row)
				self.result_body = json.dumps(self.result_body)

	def pull_result(self):
		return self.result_body

class State:
	def __init__(self, state_id, state_name=None, state_abbr=None):
			self.state_id = state_id