import pytest
from app.models import Product, db

def test_create_product(client):
    response = client.post('/api/v1/products/', json={'title': 'Test Prod', 'sku': 'SKU1', 'price': 10.0})
    assert response.status_code == 201

def test_get_products(client):
    # Add a product first
    client.post('/api/v1/products/', json={'title': 'List Prod', 'sku': 'SKU2', 'price': 20.0})
    
    response = client.get('/api/v1/products/')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['title'] == 'List Prod'
