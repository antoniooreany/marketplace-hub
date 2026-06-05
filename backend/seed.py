from app import create_app
from app.extensions import db
from app.models import (
    Integration,
    Product,
    Subscription,
    SyncJob,
    User,
    WebhookEvent,
    Workspace,
)
from flask.app import Flask

app: Flask = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    user: User = User(email="demo@example.com")
    db.session.add(instance=user)
    db.session.commit()

    ws: Workspace = Workspace(name="Demo Workspace", user_id=user.id)
    db.session.add(instance=ws)
    db.session.commit()

    for i in range(10):
        p: Product = Product(
            title=f"Product {i}", sku=f"SKU{i}", price=10.0 * i, workspace_id=ws.id
        )
        db.session.add(instance=p)

    for platform in ["Amazon", "eBay", "Shopify", "Wix"]:
        db.session.add(instance=Integration(platform=platform, workspace_id=ws.id))

    for status in ["queued", "running", "success", "failed", "success"]:
        db.session.add(instance=SyncJob(status=status, workspace_id=ws.id))

    db.session.add(instance=Subscription(plan="Free", workspace_id=ws.id))

    for etype in ["order_created", "order_updated", "product_synced", "error"]:
        db.session.add(
            instance=WebhookEvent(
                event_type=etype, payload={"data": "test"}, workspace_id=ws.id
            )
        )

    db.session.commit()
    print("Database seeded!")
