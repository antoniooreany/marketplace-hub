from typing import Any
import pytest
from flask.testing import FlaskClient
from app.models import Integration, SyncJob, Subscription
from app.extensions import db

@pytest.fixture
def setup_core_data():
    # Helper to add data for workspace 1 (from conftest)
    db.session.add(instance=Integration(platform='Amazon', workspace_id=1))
    db.session.add(instance=SyncJob(status='success', workspace_id=1))
    db.session.add(instance=Subscription(plan='Pro', workspace_id=1))
    db.session.commit()

def test_get_integrations(client: FlaskClient, setup_core_data) -> None:
    response = client.get('/api/v1/integrations')
    assert response.status_code == 200
    data = response.get_json()
    assert 'content' in data
    assert len(data['content']) == 1
    assert data['content'][0]['platform'] == 'Amazon'

def test_get_sync_jobs(client: FlaskClient, setup_core_data) -> None:
    response = client.get('/api/v1/sync-jobs')
    assert response.status_code == 200
    data = response.get_json()
    assert 'content' in data
    assert len(data['content']) == 1
    assert data['content'][0]['status'] == 'success'

def test_get_subscription(client: FlaskClient, setup_core_data) -> None:
    response = client.get('/api/v1/subscription')
    assert response.status_code == 200
    data = response.get_json()
    assert 'content' in data
    assert data['content']['plan'] == 'Pro'
