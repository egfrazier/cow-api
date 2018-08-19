from cowapi.models.db import get_db
import json

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)

# CONSIDER: Renaming resource_id to resource_value

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

		# Query for System Tenure, by state
		if self.resource_name == 'system_tenure':
			thisState = State(self.resource_id)
			db = get_db()
			with g.db.cursor() as cursor:
				sql = "SELECT state_name, state_abbr, styear, stmonth, stday, endyear, endmonth, endday FROM `state_codes` INNER JOIN `system_states_periods` ON state_codes.state_id=system_states_periods.state_id WHERE state_codes.state_id = %s;" % thisState.state_id
				cursor.execute(sql)
				result = cursor.fetchall()
				if cursor.rowcount == 0:
					self.result_body = {"results" : "No results"}
				else:
					for row in result:
						thisState.state_name = row['state_name']
						thisState.state_abbr = row['state_abbr']
						this_tenure = {"styear": row['styear'], "stmonth": row['stmonth'], "stday": row['stday'], "endyear": row['endyear'], "endmonth": row['endmonth'], "endday": row['endday']}
						thisState.system_tenure.append(this_tenure)
						self.result_body = {"results": {"State Name" : thisState.state_name, "State ID" : thisState.state_id, "State Abbr": thisState.state_abbr, "System Tenure": thisState.system_tenure}}

		# TODO: Query for System Membership, by year.
		if self.resource_name == 'system_year':
			this_year = System_year(self.resource_id)
			db = get_db()
			with g.db.cursor() as cursor:
				sql = "SELECT state_codes.state_id, state_abbr, state_name FROM system_year INNER JOIN state_codes ON state_codes.state_id=system_year.state_id WHERE system_year=%d;" % this_year.year
				cursor.execute(sql)
				result = cursor.fetchall()
				if cursor.rowcount == 0:
					self.result_body = {"results" : "No results"}
				else:
					for row in result:
						state_id = row['state_id']
						state_name = row['state_abbr']
						state_abbr = row['state_name']
						system_list_item = {"state_id": state_id, "state_abbr": state_abbr, "state_name": state_name}
						this_year.system_list.append(system_list_item)
					self.result_body = {"results": {"year": this_year.year, "system_list": this_year.system_list}}

	def pull_result(self):
		return self.result_body

class State:
	def __init__(self, state_id, state_name=None, state_abbr=None):
			self.state_id = state_id
			self.system_tenure = []

'''
{
	state : {
		state_id: 5,
		state_abbr: 'CUB',
		state_name: 'Cuba',
		system_tenure: [
			{
			styear: 1907,
			stmonth: 01,
			stday:01,
			endyear: 1920,
			endmonth: 01,
			endday:01,
			isMajor: False
			},
			{
			styear: 1956,
			stmonth: 01,
			stday:01,
			endyear: 2016,
			endmonth: 01,
			endday:01,
			isMajor: True
			}
		]
	}
}
'''

class System_year:
	def __init__(self, year):
		self.year = year
		self.system_list = []
'''
{
	"results": {
		"year": XXXX,
		"system_list": [
			{
				"state_id": 2,
				"state_abbr": "USA",
				"state_name": "United States of America"
			},
			{
				"state_id": 20,
				"state_abbr": "CAN",
				"state_name": "Canada"
			}
		]
	}
}
'''