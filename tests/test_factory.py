import pytest
from cowapi import create_app


def test_config():
    assert not create_app().testing
    # assert create_app({'TESTING': True}).testing 	# TODO: Fix test


def test_hello(client):
    response = client.get('/')
    assert response.data == b'Welcome to the Correlates of War API.'