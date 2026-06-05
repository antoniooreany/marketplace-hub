from typing import NotRequired, TypedDict, cast
from app.extensions import db
from app.models import Product, Subscription
from .exceptions import PlanLimitError
