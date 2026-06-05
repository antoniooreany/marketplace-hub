import pytest
from flask.testing import FlaskClient

def test_health_check(client: FlaskClient):
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    data: dict[str, object] = response.get_json()
    assert data['status'] == 'healthy'
