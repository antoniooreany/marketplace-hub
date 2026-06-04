from flask import Blueprint, jsonify
from app.core_services import CoreService

core_bp = Blueprint('core', __name__)

@core_bp.route('/integrations', methods=['GET'])
def get_integrations():
    return jsonify([{'id': i.id, 'platform': i.platform} for i in CoreService.get_integrations(1)])

@core_bp.route('/sync-jobs', methods=['GET'])
def get_sync_jobs():
    return jsonify([{'id': s.id, 'status': s.status} for s in CoreService.get_sync_jobs(1)])

@core_bp.route('/subscription', methods=['GET'])
def get_subscription():
    sub = CoreService.get_subscription(1)
    return jsonify({'plan': sub.plan if sub else 'Free'})
