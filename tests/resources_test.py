# Tests for resource Query.send_query() functions
import os
from cowapi import *
from flask import Flask, current_app
import pymysql
from cowapi.models.db import *
from cowapi.models.models import *
import json
from flask import (Blueprint, flash, redirect, render_template, request, session, url_for)

def test_app_setup():
    app =create_app()
    return app

# State send_query() tests
def test_state_gen():
    app = test_app_setup()
    with app.app_context():
        this_state = Query('state', 2)
        return this_state

def test_state_exists():
    test_state = test_state_gen()
    assert test_state != None

def test_state_query_gen():
    app = test_app_setup()
    with app.app_context():
        this_state = Query('state', 2)
        this_state.send_query()
        return this_state.result_body

def test_state_results_format():
    test_state_results = test_state_query_gen()
    dir(test_state_results)
    assert type(test_state_results) is dict
    assert len(test_state_results) == 1
    assert test_state_results["results"] is not None
    assert len(test_state_results["results"]) == 3
    assert test_state_results["results"]["State Name"] is not None
    assert test_state_results["results"]["State ID"] is not None
    assert test_state_results["results"]["State Abbr"] is not None
