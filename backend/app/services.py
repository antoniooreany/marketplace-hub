from typing import NotRequired, TypedDict, cast
from app.extensions import db
from app.models import Product, Subscription


class ProductCreateData(TypedDict):
    title: str
    sku: str
    price: float
    quantity: NotRequired[int]
    status: NotRequired[str]


class PlanLimitError(Exception):
    pass


class ProductService:
    @staticmethod
    def get_all_products(workspace_id: int) -> list[Product]:
        return cast(list[Product], Product.query.filter_by(workspace_id=workspace_id).all())

    @staticmethod
    def create_product(data: ProductCreateData, workspace_id: int) -> Product:
        sub: Subscription | None = cast(
            Subscription | None,
            Subscription.query.filter_by(workspace_id=workspace_id).first(),
        )
        if sub and sub.plan == 'Free':
            count: int = Product.query.filter_by(workspace_id=workspace_id).count()
            if count >= 20:
                raise PlanLimitError('Free plan limit reached')
        
        # Remove workspace_id from data if present to avoid duplication
        filtered_data = {k: v for k, v in data.items() if k != 'workspace_id'}
        product: Product = Product(**filtered_data, workspace_id=workspace_id)
        db.session.add(instance=product)
        db.session.commit()
        return product
