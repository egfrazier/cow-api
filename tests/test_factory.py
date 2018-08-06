import pytest
from cowapi import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing 	# TODO: Fix test

def test_config2(client):
	response = client.get('api/v1/resources/state/995')
	assert response.data == b"<!doctype html>\n<title>COW API</title>\n<body>{&#39;results&#39;: {&#39;State Name&#39;: &#39;Test Country&#39;, &#39;State ID&#39;: 995, &#39;State Abbr&#39;: &#39;TST&#39;}}</body>\n</html>"

def test_hello(client):
    response = client.get('/')
    assert response.data == b'Welcome to the Correlates of War API.'