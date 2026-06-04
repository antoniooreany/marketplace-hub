import pytest

def test_create_product(client):
    response = client.post('/api/v1/products/', json={'title': 'Test Prod', 'sku': 'SKU1', 'price': 10.0})
    assert response.status_code == 201
