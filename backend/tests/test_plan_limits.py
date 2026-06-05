import pytest
from flask import Flask
import pytest
from app.models import Product, Subscription, db
from app.core_services import AppService # Updated import
from app.exceptions import PlanLimitError # Updated import

def test_free_plan_limit(app: Flask) -> None:
    with app.app_context():
        # Setup Free plan
        sub = Subscription(plan='Free', workspace_id=1)
        db.session.add(sub)
        db.session.commit()

        # Add 20 products
        for i in range(20):
            AppService.create_product({'title': f'P{i}', 'sku': f'S{i}', 'price': 1.0}, 1)

        # Should fail on 21st
        with pytest.raises(PlanLimitError):
            AppService.create_product({'title': 'P21', 'sku': 'S21', 'price': 1.0}, 1)
