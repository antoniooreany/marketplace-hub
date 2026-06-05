from sqlalchemy import select
from app.models import Integration, SyncJob, Subscription, WebhookEvent
from app.extensions import db

class CoreService:
    @staticmethod
    def get_integrations(workspace_id: int) -> list[Integration]:
        stmt = select(Integration).filter_by(workspace_id=workspace_id)
        return list(db.session.scalars(stmt).all())

    @staticmethod
    def get_sync_jobs(workspace_id: int) -> list[SyncJob]:
        stmt = select(SyncJob).filter_by(workspace_id=workspace_id)
        return list(db.session.scalars(stmt).all())

    @staticmethod
    def get_subscription(workspace_id: int) -> Subscription | None:
        stmt = select(Subscription).filter_by(workspace_id=workspace_id)
        return db.session.scalars(stmt).first()

    @staticmethod
    def get_webhook_events(workspace_id: int) -> list[WebhookEvent]:
        stmt = select(WebhookEvent).filter_by(workspace_id=workspace_id)
        return list(db.session.scalars(stmt).all())
