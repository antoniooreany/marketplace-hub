from app.models import Integration, SyncJob, Subscription, WebhookEvent

class CoreService:
    @staticmethod
    def get_integrations(workspace_id: int) -> list[Integration]:
        return Integration.query.filter_by(workspace_id=workspace_id).all()

    @staticmethod
    def get_sync_jobs(workspace_id: int) -> list[SyncJob]:
        return SyncJob.query.filter_by(workspace_id=workspace_id).all()

    @staticmethod
    def get_subscription(workspace_id: int) -> Subscription | None:
        return Subscription.query.filter_by(workspace_id=workspace_id).first()

    @staticmethod
    def get_webhook_events(workspace_id: int) -> list[WebhookEvent]:
        return WebhookEvent.query.filter_by(workspace_id=workspace_id).all()
