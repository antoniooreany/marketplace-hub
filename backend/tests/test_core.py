import pytest
from app.core_services import AppService  # Updated import
from app.exceptions import PlanLimitError  # Updated import
from app.extensions import db
from app.models import Integration, Subscription, SyncJob, WebhookEvent
from flask import Flask
from flask.testing import FlaskClient
from werkzeug.test import TestResponse


@pytest.fixture
def setup_core_data() -> None:
    # Helper to add data for workspace 1 (from conftest)
    db.session.add(instance=Integration(platform="Amazon", workspace_id=1))
    db.session.add(instance=SyncJob(status="success", workspace_id=1))
    db.session.add(instance=Subscription(plan="Pro", workspace_id=1))
    db.session.commit()


def test_get_integrations(client: FlaskClient, setup_core_data) -> None:
    response: TestResponse = client.get("/api/v1/integrations")
    assert response.status_code == 200
    data = response.get_json()
    assert "content" in data
    assert len(data["content"]) == 1
    assert data["content"][0]["platform"] == "Amazon"


def test_integration_limit(app: Flask) -> None:
    with app.app_context():
        # Setup Free plan
        sub: Subscription = Subscription(plan="Free", workspace_id=1)
        db.session.add(instance=sub)
        db.session.commit()
        # Add first integration
        AppService.create_integration(platform="eBay", workspace_id=1)

        # Should fail on 2nd
        with pytest.raises(PlanLimitError):
            AppService.create_integration(platform="Shopify", workspace_id=1)


def test_webhook_persistence(app: Flask) -> None:
    with app.app_context():
        event: WebhookEvent = AppService.create_webhook_event(
            event_type="test",
            payload={"data": "val"},
            workspace_id=1,
            correlation_id="corr-1",
        )
        assert event.id is not None
        assert event.correlation_id == "corr-1"


def test_get_sync_jobs(client: FlaskClient, setup_core_data) -> None:
    response: TestResponse = client.get("/api/v1/sync-jobs")
    assert response.status_code == 200
    data = response.get_json()
    assert "content" in data
    assert len(data["content"]) == 1
    assert data["content"][0]["status"] == "success"


def test_get_subscription(client: FlaskClient, setup_core_data) -> None:
    response: TestResponse = client.get("/api/v1/subscription")
    assert response.status_code == 200
    data = response.get_json()
    assert "content" in data
    assert data["content"]["plan"] == "Pro"
