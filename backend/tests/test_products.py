from app.core_services import AppService  # Updated import
from app.extensions import db
from app.models import Subscription
from flask import Flask
from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_create_product(client: FlaskClient) -> None:
    response: TestResponse = client.post(
        "/api/v1/products/",
        json={"title": "Test Prod", "sku": "SKU1", "price": 10.0, "workspace_id": 1},
    )
    assert response.status_code == 201


def test_get_products(client: FlaskClient) -> None:
    # Add a product first
    _ = client.post(
        "/api/v1/products/",
        json={"title": "List Prod", "sku": "SKU2", "price": 20.0, "workspace_id": 1},
    )

    response: TestResponse = client.get("/api/v1/products/")
    assert response.status_code == 200
    data = response.get_json()
    assert "content" in data
    assert len(data["content"]) == 1
    assert data["content"][0]["title"] == "List Prod"


def test_create_product_plan_limit_error(app: Flask, client: FlaskClient) -> None:
    with app.app_context():
        # Setup Free plan
        sub: Subscription = Subscription(plan="Free", workspace_id=1)
        db.session.add(instance=sub)
        db.session.commit()
        # Add 20 products to hit the limit
        for i in range(20):
            AppService.create_product(
                data={"title": f"P{i}", "sku": f"S{i}", "price": 1.0}, workspace_id=1
            )

        # Attempt to create one more, should return 403
        response: TestResponse = client.post(
            "/api/v1/products/",
            json={"title": "P21", "sku": "S21", "price": 1.0, "workspace_id": 1},
        )
        assert response.status_code == 403
        data = response.get_json()
        assert "error" in data
        assert data["error"]["message"] == "Free plan limit reached"
