from typing import cast

from app.core_services import AppService  # Updated import
from app.core_services import ProductCreateData  # TypedDict is now in core_services
from app.exceptions import PlanLimitError  # Imported from new exceptions file
from app.models import Product
from flask import Blueprint, Response, jsonify, request

products_bp: Blueprint = Blueprint(name="products", import_name=__name__)


@products_bp.route(rule="/", methods=["GET"])
def get_products() -> Response:
    # Dummy workspace ID for MVP
    products: list[Product] = AppService.get_all_products(
        workspace_id=1
    )  # Updated call
    return jsonify(
        content=[{"id": p.id, "title": p.title, "sku": p.sku} for p in products]
    )


@products_bp.route(rule="/", methods=["POST"])
def create_product() -> tuple[Response, int]:
    try:
        data: ProductCreateData = cast(ProductCreateData, request.json)
        product: Product = AppService.create_product(
            data=data, workspace_id=1
        )  # Updated call
        return jsonify(content={"id": product.id}), 201
    except PlanLimitError as e:
        return jsonify(error={"message": str(e)}), 403
