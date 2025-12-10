import sys
import os

# Ensure the app module can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app
from app.models import db as _db


@pytest.fixture(scope='session')
def app():
    """Create and configure a new app instance for the test session."""
    app = create_app('TestingConfig')
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """A test client that creates a fresh database for each test function."""
    _db.create_all()
    client = app.test_client()
    try:
        yield client
    finally:
        _db.session.remove()
        _db.drop_all()


@pytest.fixture(scope='function')
def db(app):
    """Provide access to the SQLAlchemy instance configured for tests."""
    _db.create_all()
    try:
        yield _db
    finally:
        _db.session.remove()
        _db.drop_all()