from collections.abc import Generator

import pytest
from app import create_app
from app.extensions import db
from app.models import User, Workspace
from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture
def app() -> Generator[Flask, None, None]:
    app: Flask = create_app(config_class="app.config.TestingConfig")
    with app.app_context():
        db.create_all()
        # Seed base data
        user: User = User(email="test@example.com")
        db.session.add(instance=user)
        db.session.commit()
        # Assuming model definitions require explicit initialization
        ws: Workspace = Workspace(name="Test Workspace", user_id=user.id)
        db.session.add(instance=ws)
        db.session.commit()
        yield app
        db.drop_all()


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
