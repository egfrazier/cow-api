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
					# Use jsonify here like in /resource/states?
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
				#self.result_body = json.dumps(self.result_body)

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

		# Query for Major Tenure, by state
		if self.resource_name == 'major_tenure':
			thisState = State(self.resource_id)
			db = get_db()
			with g.db.cursor() as cursor:
				sql = "SELECT state_name, state_abbr, styear, stmonth, stday, endyear, endmonth, endday FROM `state_codes` INNER JOIN `system_majors_periods` ON state_codes.state_id=system_majors_periods.state_id WHERE state_codes.state_id = %s;" % thisState.state_id
				cursor.execute(sql)
				result = cursor.fetchall()
				if cursor.rowcount == 0:
					self.result_body = {"results" : "No results"}
				else:
					for row in result:
						thisState.state_name = row['state_name']
						thisState.state_abbr = row['state_abbr']
						this_tenure = {"styear": row['styear'], "stmonth": row['stmonth'], "stday": row['stday'], "endyear": row['endyear'], "endmonth": row['endmonth'], "endday": row['endday']}
						thisState.major_tenure.append(this_tenure)
						self.result_body = {"results": {"State Name" : thisState.state_name, "State ID" : thisState.state_id, "State Abbr": thisState.state_abbr, "Major Tenure": thisState.major_tenure}}



		# From here down resource by war type have have their single and
		# multiple queries folded into one Query object.
		# TODO: Verify is this is a fesible approach for they above
		# query functions. 
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
															"timeline": {
																"styear": this_war.timeline['styear'],
																"stmonth": this_war.timeline['stmonth'],
																"stday": this_war.timeline['stday'],
																"endyear": this_war.timeline['endyear'],
																"endmonth": this_war.timeline['endmonth'],
																"endday": this_war.timeline['endday'],
															},
															"deaths": {
																"side_a_deaths": this_war.deaths['side_a_deaths'],
																"side_b_deaths": this_war.deaths['side_b_deaths'],
																"total_combat_deaths": this_war.deaths['total_combat_deaths']
															}
															})

		if self.resource_name == 'intrastate':
			db = get_db()
			with g.db.cursor() as cursor:
				if self.resource_id is None:
					sql = "SELECT * FROM `intra_state_wars_list`;"
					cursor.execute(sql)
					result = cursor.fetchall()
				elif self.resource_id is not None:
					sql = "SELECT * FROM `intra_state_wars_list` WHERE war_id = %s;" % self.resource_id
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
															"timeline": [
																{
																	"styear1": this_war.timeline[0]['styear1'],
																	"stmonth1": this_war.timeline[0]['stmonth1'],
																	"stday1": this_war.timeline[0]['stday1'],
																	"endyear1": this_war.timeline[0]['endyear1'],
																	"endmonth1": this_war.timeline[0]['endmonth1'],
																	"endday1": this_war.timeline[0]['endday1']
																},
																{
																	"styear2": this_war.timeline[1]['styear2'],
																	"stmonth2": this_war.timeline[1]['stmonth2'],
																	"stday2": this_war.timeline[1]['stday2'],
																	"endyear2": this_war.timeline[1]['endyear2'],
																	"endmonth2": this_war.timeline[1]['endmonth2'],
																	"endday2": this_war.timeline[1]['endday2']
																}
															],
															"deaths": {
																"side_a_deaths": this_war.deaths['side_a_deaths'],
																"side_b_deaths": this_war.deaths['side_b_deaths']
															}
															})

		if self.resource_name == 'interstate':
			db = get_db()
			with g.db.cursor() as cursor:
				if self.resource_id is None:
					sql = "SELECT * FROM `inter_state_wars_list`;"
					cursor.execute(sql)
					result = cursor.fetchall()
				elif self.resource_id is not None:
					sql = "SELECT * FROM `inter_state_wars_list` WHERE war_id = %s;" % self.resource_id
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
																"outcome": this_war.meta["outcome"],
																# Consider moving to 'combatants section'
																"side_id": this_war.meta['side_id'],
																"state_id": this_war.meta['state_id'],
																"state_name": this_war.meta['state_name']
															},
															"timeline": [
																{
																	"styear1": this_war.timeline[0]['styear1'],
																	"stmonth1": this_war.timeline[0]['stmonth1'],
																	"stday1": this_war.timeline[0]['stday1'],
																	"endyear1": this_war.timeline[0]['endyear1'],
																	"endmonth1": this_war.timeline[0]['endmonth1'],
																	"endday1": this_war.timeline[0]['endday1']
																},
																{
																	"styear2": this_war.timeline[1]['styear2'],
																	"stmonth2": this_war.timeline[1]['stmonth2'],
																	"stday2": this_war.timeline[1]['stday2'],
																	"endyear2": this_war.timeline[1]['endyear2'],
																	"endmonth2": this_war.timeline[1]['endmonth2'],
																	"endday2": this_war.timeline[1]['endday2']
																}
															],
															"deaths": {
																"total_combat_deaths": this_war.deaths['total_combat_deaths']
															}
															})

		if self.resource_name == 'extrastate':
			db = get_db()
			with g.db.cursor() as cursor:
				if self.resource_id is None:
					sql = "SELECT * FROM `extra_state_wars_list`;"
					cursor.execute(sql)
					result = cursor.fetchall()
				elif self.resource_id is not None:
					sql = "SELECT * FROM `extra_state_wars_list` WHERE war_id = %s;" % self.resource_id
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
																"outcome": this_war.meta["outcome"],
																"was_intervention": this_war.meta['was_intervention']
															},
															"combatants": {
																"side_a": this_war.combatants['side_a'],
																"side_b": this_war.combatants['side_b']
															},
															"timeline": [
																{
																	"styear1": this_war.timeline[0]['styear1'],
																	"stmonth1": this_war.timeline[0]['stmonth1'],
																	"stday1": this_war.timeline[0]['stday1'],
																	"endyear1": this_war.timeline[0]['endyear1'],
																	"endmonth1": this_war.timeline[0]['endmonth1'],
																	"endday1": this_war.timeline[0]['endday1']
																},
																{
																	"styear2": this_war.timeline[1]['styear2'],
																	"stmonth2": this_war.timeline[1]['stmonth2'],
																	"stday2": this_war.timeline[1]['stday2'],
																	"endyear2": this_war.timeline[1]['endyear2'],
																	"endmonth2": this_war.timeline[1]['endmonth2'],
																	"endday2": this_war.timeline[1]['endday2']
																}
															],
															"deaths": {
																"total_combat_deaths": this_war.deaths['total_combat_deaths']
															}
															})



	def pull_result(self):
		return self.result_body

class State:
	def __init__(self, state_id, state_name=None, state_abbr=None):
			self.state_id = state_id
			self.system_tenure = []
			self.major_tenure = []

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
		if self.meta['war_type'] == 'intrastate':
			self.meta['is_interationalized'] = row['is_internationalized']
		if self.meta['war_type'] == 'interstate':
			self.meta['side_id'] = row['side_id']
			self.meta['state_id'] = row['state_id']
			self.meta['state_name'] = row['state_name']
		if self.meta['war_type'] == 'extrastate':
			self.meta['was_intervention'] = row['was_intervention']


	def set_war_combatants(self, row):
		if self.meta['war_type'] == 'nonstate':
			self.combatants['side_a'] = [row['side_a1'], row['side_a2']]
			self.combatants['side_b'] = [row['side_b1'], row['side_b2'], row['side_b3'], row['side_b4'], row['side_b5']]
		elif self.meta['war_type'] in ['intrastate', 'extrastate']:
			self.combatants['side_a'] = {'side_a_id': row['side_a_id'], 'side_a_name': row['side_a_name']}
			self.combatants['side_b'] = {'side_b_id': row['side_b_id'], 'side_b_name': row['side_b_name']}

	def set_nonstate_war_timeline(self, row):
		if self.meta['war_type'] == 'nonstate':
			self.timeline = {
								'styear': row['styear'], 
								'stmonth': row['stmonth'],
								'stday': row['stday'],
								'endyear': row['endyear'],
								'endmonth': row['endmonth'],
								'endday': row['endday']
								}
		elif self.meta['war_type'] in ['intrastate','interstate', 'extrastate']:
			self.timeline = [
								{
								'styear1': row['styear1'], 
								'stmonth1': row['stmonth1'],
								'stday1': row['stday1'],
								'endyear1': row['endyear1'],
								'endmonth1': row['endmonth1'],
								'endday1': row['endday1']
								},
								{
								'styear2': row['styear2'], 
								'stmonth2': row['stmonth2'],
								'stday2': row['stday2'],
								'endyear2': row['endyear2'],
								'endmonth2': row['endmonth2'],
								'endday2': row['endday2']
								}
							]

	def set_war_deaths(self, row):
		if self.meta['war_type'] in ['nonstate']:
			self.deaths['side_a_deaths'] = row['side_a_deaths']
			self.deaths['side_b_deaths'] = row['side_b_deaths']
			self.deaths['total_combat_deaths'] = row['total_combat_deaths']
		if self.meta['war_type'] in ['intrastate']:
			self.deaths['side_a_deaths'] = row['side_a_deaths']
			self.deaths['side_b_deaths'] = row['side_b_deaths']
		if self.meta['war_type'] in ['interstate', 'extrastate']:
			self.deaths['total_combat_deaths'] = row['combat_deaths']


	def __init__(self, war_type, row):
		self.meta = {}
		self.meta['war_type'] = war_type
		self.combatants = {}
		self.timeline = {}
		self.deaths = {}
		self.set_war_meta(row)
		self.set_war_combatants(row)
		self.set_nonstate_war_timeline(row)
		self.set_war_deaths(row)
