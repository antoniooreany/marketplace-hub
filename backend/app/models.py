from datetime import datetime
from sqlalchemy import JSON, Float, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(length=120), unique=True, nullable=False)

    def __init__(self, *, email: str) -> None:
        self.email = email

class Workspace(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey(column='user.id'), nullable=False)

    def __init__(self, *, name: str, user_id: int) -> None:
        self.name = name
        self.user_id = user_id

class Product(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(length=200), nullable=False)
    sku: Mapped[str] = mapped_column(String(length=50), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    quantity: Mapped[int] = mapped_column(default=0)
    status: Mapped[str] = mapped_column(String(length=20), default='active')
    workspace_id: Mapped[int] = mapped_column(
        ForeignKey(column='workspace.id'), nullable=False
    )

    def __init__(
        self,
        *,
        title: str,
        sku: str,
        price: float,
        workspace_id: int,
        quantity: int = 0,
        status: str = 'active',
    ) -> None:
        self.title = title
        self.sku = sku
        self.price = price
        self.workspace_id = workspace_id
        self.quantity = quantity
        self.status = status

class Integration(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    platform: Mapped[str] = mapped_column(String(length=50), nullable=False)
    workspace_id: Mapped[int] = mapped_column(ForeignKey(column='workspace.id'), nullable=False)

    def __init__(self, *, platform: str, workspace_id: int) -> None:
        self.platform = platform
        self.workspace_id = workspace_id

class SyncJob(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(length=20), nullable=False)
    workspace_id: Mapped[int] = mapped_column(ForeignKey(column='workspace.id'), nullable=False)
    last_error: Mapped[str | None] = mapped_column(String(length=500), nullable=True)
    correlation_id: Mapped[str | None] = mapped_column(String(length=100), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now())

    def __init__(
        self,
        *,
        status: str,
        workspace_id: int,
        last_error: str | None = None,
        correlation_id: str | None = None,
    ) -> None:
        self.status = status
        self.workspace_id = workspace_id
        self.last_error = last_error
        self.correlation_id = correlation_id

class Subscription(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    plan: Mapped[str] = mapped_column(String(length=20), default='Free')
    workspace_id: Mapped[int] = mapped_column(ForeignKey(column='workspace.id'), nullable=False)

    def __init__(self, *, plan: str = 'Free', workspace_id: int) -> None:
        self.plan = plan
        self.workspace_id = workspace_id

class WebhookEvent(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    event_type: Mapped[str] = mapped_column(String(length=50), nullable=False)
    payload: Mapped[dict[str, object]] = mapped_column(JSON, nullable=False)
    status: Mapped[str] = mapped_column(String(length=20), default='pending')
    correlation_id: Mapped[str | None] = mapped_column(String(length=100), nullable=True)
    workspace_id: Mapped[int] = mapped_column(ForeignKey(column='workspace.id'), nullable=False)

    def __init__(
        self,
        *,
        event_type: str,
        payload: dict[str, object],
        workspace_id: int,
        correlation_id: str | None = None,
        status: str = 'pending',
    ) -> None:
        self.event_type = event_type
        self.payload = payload
        self.workspace_id = workspace_id
        self.correlation_id = correlation_id
        self.status = status
