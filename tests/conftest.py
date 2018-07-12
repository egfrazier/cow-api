import sys, os
import tempfile

# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../cowapi/')

import pytest
from cowapi import create_app
from cowapi.models.db import get_db, init_db

# with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
#     _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    # db_fd, db_path = tempfile.mkstemp()

    app = create_app({'TESTING': True})

    with app.app_context():
        init_db()
        get_db()

    yield app

    # os.close(db_fd)
    # os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()