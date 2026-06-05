from typing import Generator
import pytest
from flask import Flask
from flask.testing import FlaskClient
from app import create_app
from app.extensions import db
from app.models import User, Workspace

@pytest.fixture
def app() -> Generator[Flask, None, None]:
    app = create_app('app.config.TestingConfig')
    with app.app_context():
        db.create_all()
        # Seed base data
        user = User(email='test@example.com')
        db.session.add(user)
        db.session.commit()
        # workspace_id is implicitly assigned via relationship if set up, 
        # or we must pass the user.id explicitly if that's the FK
        ws = Workspace(name='Test Workspace', user_id=user.id)
        db.session.add(ws)
        db.session.commit()
        yield app
        db.drop_all()

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
