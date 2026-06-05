from sqlalchemy.sql.selectable import Select
from sqlalchemy import select
from app.models import Integration, Product, SyncJob, Subscription, WebhookEvent
from app.extensions import db
from .exceptions import PlanLimitError
from typing import NotRequired, TypedDict, cast # Needed for ProductCreateData, and cast for explicit casting


class ProductCreateData(TypedDict): # Moved from services.py
    title: str
    sku: str
    price: float
    quantity: NotRequired[int]
    status: NotRequired[str]


class AppService: # Renamed from CoreService
    @staticmethod
    def get_all_products(workspace_id: int) -> list[Product]: # Moved from ProductService
        stmt: Select[tuple[Product]] = select(Product).filter_by(workspace_id=workspace_id)
        return list(db.session.scalars(stmt).all())

    @staticmethod
    def create_product(data: ProductCreateData, workspace_id: int) -> Product: # Moved from ProductService
        sub: Subscription | None = AppService.get_subscription(workspace_id) # Call self
        if sub and sub.plan == 'Free':
            count: int = len(AppService.get_all_products(workspace_id)) # Call self
            if count >= 20:
                raise PlanLimitError('Free plan limit reached')

        # Explicitly extract and cast arguments for Product constructor
        # This resolves Pyright 'object' to 'str' assignment errors
        title = cast(str, data['title'])
        sku = cast(str, data['sku'])
        price = cast(float, data['price'])
        quantity = cast(int, data.get('quantity', 0))
        status = cast(str, data.get('status', 'active'))

        product: Product = Product(
            title=title,
            sku=sku,
            price=price,
            workspace_id=workspace_id,
            quantity=quantity,
            status=status
        )
        db.session.add(instance=product)
        db.session.commit()
        return product

    @staticmethod
    def get_integrations(workspace_id: int) -> list[Integration]:
        stmt: Select[tuple[Integration]] = select(Integration).filter_by(workspace_id=workspace_id)
        return list(db.session.scalars(stmt).all())

    @staticmethod
    def create_integration(platform: str, workspace_id: int) -> Integration:
        sub: Subscription | None = AppService.get_subscription(workspace_id) # Call self
        if sub and sub.plan == 'Free':
            count: int = len(AppService.get_integrations(workspace_id)) # Call self
            if count >= 1:
                raise PlanLimitError('Free plan integration limit reached')

        integration: Integration = Integration(platform=platform, workspace_id=workspace_id)
        db.session.add(instance=integration)
        db.session.commit()
        return integration

    @staticmethod
    def get_sync_jobs(workspace_id: int) -> list[SyncJob]:
        stmt: Select[tuple[SyncJob]] = select(SyncJob).filter_by(workspace_id=workspace_id)
        return list(db.session.scalars(stmt).all())

    @staticmethod
    def get_subscription(workspace_id: int) -> Subscription | None:
        stmt: Select[tuple[Subscription]] = select(Subscription).filter_by(workspace_id=workspace_id)
        return db.session.scalars(stmt).first()

    @staticmethod
    def get_webhook_events(workspace_id: int) -> list[WebhookEvent]:
        stmt: Select[tuple[WebhookEvent]] = select(WebhookEvent).filter_by(workspace_id=workspace_id)
        return list(db.session.scalars(stmt).all())

    @staticmethod
    def create_webhook_event(event_type: str, payload: dict[str, object], workspace_id: int, correlation_id: str | None = None) -> WebhookEvent:
        event: WebhookEvent = WebhookEvent(event_type=event_type, payload=payload, workspace_id=workspace_id, correlation_id=correlation_id)
        db.session.add(instance=event)
        db.session.commit()
        return event
