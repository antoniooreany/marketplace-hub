import pytest
from app import create_app
from app.extensions import db
from app.models import User, Workspace

@pytest.fixture
def app():
    app = create_app('app.config.TestingConfig')
    with app.app_context():
        db.create_all()
        # Seed base data
        user = User(email='test@example.com')
        db.session.add(user)
        db.session.commit()
        ws = Workspace(name='Test Workspace', user_id=user.id)
        db.session.add(ws)
        db.session.commit()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
