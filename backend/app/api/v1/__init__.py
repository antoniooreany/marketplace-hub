from flask import Blueprint

api_v1_bp = Blueprint('api_v1', __name__)

# Import routes to register them with the blueprint
from . import health

# Placeholder imports for other modules
# from . import auth, products, integrations, sync_jobs, subscriptions, webhooks, debug_ops
