from app.models import Integration, SyncJob, Subscription, WebhookEvent, db

class CoreService:
    @staticmethod
    def get_integrations(workspace_id):
        return Integration.query.filter_by(workspace_id=workspace_id).all()

    @staticmethod
    def get_sync_jobs(workspace_id):
        return SyncJob.query.filter_by(workspace_id=workspace_id).all()

    @staticmethod
    def get_subscription(workspace_id):
        return Subscription.query.filter_by(workspace_id=workspace_id).first()

    @staticmethod
    def get_webhook_events(workspace_id):
        # Placeholder for complex filtering if needed
        return WebhookEvent.query.all()  # simplified for MVP
