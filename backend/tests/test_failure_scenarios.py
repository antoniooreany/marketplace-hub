from flask import Flask
from app.models import SyncJob
from app.extensions import db

def test_sync_job_error_fields(app: Flask) -> None:
    with app.app_context():
        job: SyncJob = SyncJob(status='failed', workspace_id=1, last_error='Rate limit exceeded', correlation_id='xyz-123')
        db.session.add(job)
        db.session.commit()

        saved_job = db.session.scalars(db.select(SyncJob).filter_by(correlation_id='xyz-123')).first()
        assert saved_job is not None
        assert saved_job.last_error == 'Rate limit exceeded'
        assert saved_job.updated_at is not None
