from app.models import Integration, SyncJob, Subscription, WebhookEvent
from app.extensions import db

class CoreService:
    @staticmethod
    def get_integrations(workspace_id: int) -> list[Integration]:
        return list(db.session.scalars(db.select(Integration).filter_by(workspace_id=workspace_id)).all())

    @staticmethod
    def get_sync_jobs(workspace_id: int) -> list[SyncJob]:
        return list(db.session.scalars(db.select(SyncJob).filter_by(workspace_id=workspace_id)).all())

    @staticmethod
    def get_subscription(workspace_id: int) -> Subscription | None:
        return db.session.scalars(db.select(Subscription).filter_by(workspace_id=workspace_id)).first()

    @staticmethod
    def get_webhook_events(workspace_id: int) -> list[WebhookEvent]:
        return list(db.session.scalars(db.select(WebhookEvent).filter_by(workspace_id=workspace_id)).all())
