# from flask.blueprints import Blueprint


from flask import Blueprint

api_v1_bp: Blueprint = Blueprint(name='api_v1', import_name=__name__)

from . import health

