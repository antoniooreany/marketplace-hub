from flask import Response, jsonify
from .blueprint import api_v1_bp

@api_v1_bp.route(rule='/health', methods=['GET'])
def health_check() -> tuple[Response, int]:
    return jsonify({
        "status": "healthy",
        "version": "v1",
        "service": "marketplace-hub-backend"
    }), 200
