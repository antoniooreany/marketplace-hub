from typing import cast
from flask import Blueprint, jsonify, request
from app.services import ProductService, ProductCreateData

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_products():
    # Dummy workspace ID for MVP
    products = ProductService.get_all_products(1)
    return jsonify([{'id': p.id, 'title': p.title, 'sku': p.sku} for p in products])

@products_bp.route('/', methods=['POST'])
def create_product():
    data = cast(ProductCreateData, request.json)
    product = ProductService.create_product(data, 1)
    return jsonify({'id': product.id}), 201
