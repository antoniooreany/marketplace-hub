from app.core_services import AppService
from app.models import Subscription
from flask import Blueprint, Response, jsonify

core_bp: Blueprint = Blueprint(name="core", import_name=__name__)


@core_bp.route(rule="/integrations", methods=["GET"])
def get_integrations() -> Response:
    return jsonify(
        content=[
            {"id": i.id, "platform": i.platform}
            for i in AppService.get_integrations(workspace_id=1)
        ]
    )


@core_bp.route(rule="/sync-jobs", methods=["GET"])
def get_sync_jobs() -> Response:
    return jsonify(
        content=[
            {"id": s.id, "status": s.status}
            for s in AppService.get_sync_jobs(workspace_id=1)
        ]
    )


@core_bp.route(rule="/subscription", methods=["GET"])
def get_subscription() -> Response:
    sub: Subscription | None = AppService.get_subscription(workspace_id=1)
    return jsonify(content={"plan": sub.plan if sub is not None else "Free"})
