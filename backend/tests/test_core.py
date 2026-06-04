import pytest
from app.models import Integration, SyncJob, Subscription, db

@pytest.fixture
def setup_core_data():
    # Helper to add data for workspace 1 (from conftest)
    db.session.add(Integration(platform='Amazon', workspace_id=1))
    db.session.add(SyncJob(status='success', workspace_id=1))
    db.session.add(Subscription(plan='Pro', workspace_id=1))
    db.session.commit()

def test_get_integrations(client, setup_core_data):
    response = client.get('/api/v1/integrations')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['platform'] == 'Amazon'

def test_get_sync_jobs(client, setup_core_data):
    response = client.get('/api/v1/sync-jobs')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['status'] == 'success'

def test_get_subscription(client, setup_core_data):
    response = client.get('/api/v1/subscription')
    assert response.status_code == 200
    data = response.get_json()
    assert data['plan'] == 'Pro'
