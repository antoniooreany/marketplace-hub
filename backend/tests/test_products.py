from werkzeug.test import TestResponse
from flask.testing import FlaskClient

def test_create_product(client: FlaskClient) -> None:
    response: TestResponse = client.post('/api/v1/products/', json={'title': 'Test Prod', 'sku': 'SKU1', 'price': 10.0})
    assert response.status_code == 201

def test_get_products(client: FlaskClient) -> None:
    # Add a product first
    _ = client.post('/api/v1/products/', json={'title': 'List Prod', 'sku': 'SKU2', 'price': 20.0, 'workspace_id': 1})

    response = client.get('/api/v1/products/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'content' in data
    assert len(data['content']) == 1
    assert data['content'][0]['title'] == 'List Prod'
