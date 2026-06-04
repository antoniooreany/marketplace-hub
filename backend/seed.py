from app import create_app, db
from app.models import User, Workspace, Product, Integration, SyncJob, Subscription, WebhookEvent

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
    
    user = User(email='demo@example.com')
    db.session.add(user)
    db.session.commit()
    
    ws = Workspace(name='Demo Workspace', user_id=user.id)
    db.session.add(ws)
    db.session.commit()
    
    for i in range(10):
        p = Product(title=f'Product {i}', sku=f'SKU{i}', price=10.0*i, workspace_id=ws.id)
        db.session.add(p)
    
    for platform in ['Amazon', 'eBay', 'Shopify', 'Wix']:
        db.session.add(Integration(platform=platform, workspace_id=ws.id))
    
    for status in ['queued', 'running', 'success', 'failed', 'success']:
        db.session.add(SyncJob(status=status, workspace_id=ws.id))
    
    db.session.add(Subscription(plan='Free', workspace_id=ws.id))
    
    for etype in ['order_created', 'order_updated', 'product_synced', 'error']:
        db.session.add(WebhookEvent(event_type=etype, payload={'data': 'test'}, workspace_id=ws.id))
    
    db.session.commit()
    print('Database seeded!')
