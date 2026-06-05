from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_health_check(client: FlaskClient) -> None:
    response: TestResponse = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
