import pytest
from app.models import SyncJob, db

def test_sync_job_error_fields(client):
    job = SyncJob(status='failed', workspace_id=1, last_error='Rate limit exceeded', correlation_id='xyz-123')
    db.session.add(job)
    db.session.commit()
    
    saved_job = SyncJob.query.filter_by(correlation_id='xyz-123').first()
    assert saved_job is not None
    assert saved_job.last_error == 'Rate limit exceeded'
    assert saved_job.updated_at is not None
