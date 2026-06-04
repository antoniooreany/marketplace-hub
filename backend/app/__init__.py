import os
from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # Register blueprints
    from .api.v1 import api_v1_bp
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    # Placeholder for other modules
    # app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    # app.register_blueprint(products_bp, url_prefix='/api/v1/products')
    # app.register_blueprint(integrations_bp, url_prefix='/api/v1/integrations')
    # app.register_blueprint(sync_jobs_bp, url_prefix='/api/v1/sync-jobs')
    # app.register_blueprint(subscriptions_bp, url_prefix='/api/v1/subscriptions')
    # app.register_blueprint(webhooks_bp, url_prefix='/api/v1/webhooks')
    # app.register_blueprint(debug_ops_bp, url_prefix='/api/v1/debug-ops')

    return app
