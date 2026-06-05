from sqlalchemy.sql.selectable import Select
from sqlalchemy import select
from app.models import Integration, SyncJob, Subscription, WebhookEvent
from app.extensions import db

class PlanLimitError(Exception): pass

class CoreService:
    @staticmethod
    def get_integrations(workspace_id: int) -> list[Integration]:
        stmt: Select[tuple[Integration]] = select(Integration).filter_by(workspace_id=workspace_id)
        return list(db.session.scalars(stmt).all())

    @staticmethod
    def create_integration(platform: str, workspace_id: int) -> Integration:
        sub = CoreService.get_subscription(workspace_id)
        if sub and sub.plan == 'Free':
            count = len(CoreService.get_integrations(workspace_id))
            if count >= 1:
                raise PlanLimitError('Free plan integration limit reached')
        
        integration = Integration(platform=platform, workspace_id=workspace_id)
        db.session.add(integration)
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
        event = WebhookEvent(event_type=event_type, payload=payload, workspace_id=workspace_id, correlation_id=correlation_id)
        db.session.add(event)
        db.session.commit()
        return event
