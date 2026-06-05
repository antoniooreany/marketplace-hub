from datetime import datetime
from typing import Any

from sqlalchemy import JSON, Float, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

class Workspace(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)

class Product(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    sku: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    quantity: Mapped[int] = mapped_column(default=0)
    status: Mapped[str] = mapped_column(String(20), default='active')
    workspace_id: Mapped[int] = mapped_column(
        ForeignKey('workspace.id'), nullable=False
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
    platform: Mapped[str] = mapped_column(String(50), nullable=False)
    workspace_id: Mapped[int] = mapped_column(ForeignKey('workspace.id'), nullable=False)

class SyncJob(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    workspace_id: Mapped[int] = mapped_column(ForeignKey('workspace.id'), nullable=False)
    last_error: Mapped[str | None] = mapped_column(String(500), nullable=True)
    correlation_id: Mapped[str | None] = mapped_column(String(100), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now())

class Subscription(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    plan: Mapped[str] = mapped_column(String(20), default='Free')
    workspace_id: Mapped[int] = mapped_column(ForeignKey('workspace.id'), nullable=False)

class WebhookEvent(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    event_type: Mapped[str] = mapped_column(String(50), nullable=False)
    payload: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False)
    status: Mapped[str] = mapped_column(String(20), default='pending')
    correlation_id: Mapped[str | None] = mapped_column(String(100), nullable=True)
    workspace_id: Mapped[int] = mapped_column(ForeignKey('workspace.id'), nullable=False)
