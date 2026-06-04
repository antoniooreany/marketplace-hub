from app.models import Product, db

class ProductService:
    @staticmethod
    def get_all_products(workspace_id):
        return Product.query.filter_by(workspace_id=workspace_id).all()

    @staticmethod
    def create_product(data, workspace_id):
        product = Product(**data, workspace_id=workspace_id)
        db.session.add(product)
        db.session.commit()
        return product
