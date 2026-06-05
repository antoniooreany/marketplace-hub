# from flask.app import Flask
from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate

def create_app(config_class: str = 'app.config.Config') -> Flask:
    app: Flask = Flask(import_name=__name__)
    app.config.from_object(obj=config_class)

    # Initialize extensions
    _ = CORS(app=app)
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)

    # Register blueprints
    from .api.v1 import api_v1_bp
    from .api.v1.products import products_bp
    from .api.v1.core import core_bp
    
    app.register_blueprint(blueprint=api_v1_bp, url_prefix='/api/v1')
    app.register_blueprint(blueprint=products_bp, url_prefix='/api/v1/products')
    app.register_blueprint(blueprint=core_bp, url_prefix='/api/v1')

    # Placeholder for other modules
    # app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    # app.register_blueprint(integrations_bp, url_prefix='/api/v1/integrations')
    # app.register_blueprint(sync_jobs_bp, url_prefix='/api/v1/sync-jobs')
    # app.register_blueprint(subscriptions_bp, url_prefix='/api/v1/subscriptions')
    # app.register_blueprint(webhooks_bp, url_prefix='/api/v1/webhooks')
    # app.register_blueprint(debug_ops_bp, url_prefix='/api/v1/debug-ops')

    return app
