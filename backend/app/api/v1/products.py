from app.models import Product
from typing import cast
from flask import Blueprint, Response, jsonify, request
from app.services import ProductService, ProductCreateData, PlanLimitError

products_bp: Blueprint = Blueprint(name='products', import_name=__name__)

@products_bp.route(rule='/', methods=['GET'])
def get_products() -> Response:
    # Dummy workspace ID for MVP
    products: list[Product] = ProductService.get_all_products(workspace_id=1)
    return jsonify(content=[{'id': p.id, 'title': p.title, 'sku': p.sku} for p in products])

@products_bp.route(rule='/', methods=['POST'])
def create_product() -> tuple[Response, int]:
    try:
        data: ProductCreateData = cast(ProductCreateData, request.json)
        product: Product = ProductService.create_product(data=data, workspace_id=1)
        return jsonify(content={'id': product.id}), 201
    except PlanLimitError as e:
        return jsonify(error={'message': str(e)}), 403
