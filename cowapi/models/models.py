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

		if self.resource_name == 'nonstate':
			db = get_db()
			with g.db.cursor() as cursor:
				if self.resource_id is None:
					sql = "SELECT * FROM `non_state_wars_list`;"
					cursor.execute(sql)
					result = cursor.fetchall()
				elif self.resource_id is not None:
					sql = "SELECT * FROM `non_state_wars_list` WHERE war_id = %s;" % self.resource_id
					cursor.execute(sql)
					result = cursor.fetchall()
				if cursor.rowcount == 0:
					self.result_body = {"results" : "No results"}
				else:
					self.result_body = {"results" : []}
					for row in result:
						this_war = War(self.resource_name, row)
						this_war.set_war_meta(row)
						self.result_body["results"].append({"meta":{ 
																"war_id": this_war.meta["war_id"], 
																"war_name": this_war.meta["war_name"],
																"war_type": this_war.meta["war_type"], 
																"war_location": this_war.meta["war_location"], 
																"initiator": this_war.meta["initiator"], 
																"trans_from": this_war.meta["trans_from"], 
																"trans_to": this_war.meta["trans_to"], 
																"outcome": this_war.meta["outcome"]
															},
															"combatants": {
																"side_a": this_war.combatants['side_a'],
																"side_b": this_war.combatants['side_b']
															},
															"timeline": [{
																"styear": this_war.timeline[0]['styear'],
																"stmonth": this_war.timeline[0]['stmonth'],
																"stday": this_war.timeline[0]['stday'],
																"endyear": this_war.timeline[0]['endyear'],
																"endmonth": this_war.timeline[0]['endmonth'],
																"endday": this_war.timeline[0]['endday'],
															}],
															"deaths": {
																"side_a_deaths": this_war.deaths['side_a_deaths'],
																"side_b_deaths": this_war.deaths['side_b_deaths'],
																"total_combat_deaths": this_war.deaths['total_combat_deaths']
															}
															})




	def pull_result(self):
		return self.result_body

class State:
	def __init__(self, state_id, state_name=None, state_abbr=None):
			self.state_id = state_id
			self.system_tenure = []

class System_year:
	def __init__(self, year):
		self.year = year
		self.system_list = []

class War:
	def set_war_meta(self, row):
		self.meta['war_id'] = row['war_id']
		self.meta['war_name'] = row['war_name']
		self.meta['war_location'] = row['war_location']
		self.meta['initiator'] = row['initiator']
		self.meta['trans_from'] = row['trans_from']
		self.meta['trans_to'] = row['trans_to']
		self.meta['outcome'] = row['outcome']


	def set_war_combatants(self, row):
		self.combatants['side_a'] = [row['side_a1'], row['side_a2']]
		self.combatants['side_b'] = [row['side_b1'], row['side_b2'], row['side_b3'], row['side_b4'], row['side_b5']]

	def set_nonstate_war_timeline(self, row):
		self.timeline.append({
							'styear': row['styear'], 
							'stmonth': row['stmonth'],
							'stday': row['stday'],
							'endyear': row['endyear'],
							'endmonth': row['endmonth'],
							'endday': row['endday']
							})

	def set_war_deaths(self, row):
		self.deaths['side_a_deaths'] = row['side_a_deaths']
		self.deaths['side_b_deaths'] = row['side_b_deaths']
		self.deaths['total_combat_deaths'] = row['total_combat_deaths']


	def __init__(self, war_type, row):
		self.meta = {}
		self.meta['war_type'] = war_type
		self.combatants = {}
		self.timeline = []
		self.deaths = {}
		self.set_war_meta(row)
		self.set_war_combatants(row)
		self.set_nonstate_war_timeline(row)
		self.set_war_deaths(row)
