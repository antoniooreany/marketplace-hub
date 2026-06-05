from app.extensions import db
from app.models import Product, Subscription

class PlanLimitError(Exception): pass

class ProductService:
    @staticmethod
    def get_all_products(workspace_id):
        return Product.query.filter_by(workspace_id=workspace_id).all()

    @staticmethod
    def create_product(data, workspace_id):
        sub = Subscription.query.filter_by(workspace_id=workspace_id).first()
        if sub and sub.plan == 'Free':
            count = Product.query.filter_by(workspace_id=workspace_id).count()
            if count >= 20:
                raise PlanLimitError('Free plan limit reached')
        
        product = Product(**data, workspace_id=workspace_id)
        db.session.add(product)
        db.session.commit()
        return product
