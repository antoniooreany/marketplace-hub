from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, String
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
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)
    workspace_id = db.Column(db.Integer, db.ForeignKey('workspace.id'), nullable=False)

class SyncJob(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(db.String(20), nullable=False)
    workspace_id: Mapped[int] = mapped_column(
        db.ForeignKey('workspace.id'), nullable=False
    )
    last_error: Mapped[str | None] = mapped_column(db.String(500), nullable=True)
    correlation_id: Mapped[str | None] = mapped_column(db.String(100), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now()
    )

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.String(20), default='Free')
    workspace_id = db.Column(db.Integer, db.ForeignKey('workspace.id'), nullable=False)

    if TYPE_CHECKING:
        plan: str

class WebhookEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False)
    payload = db.Column(db.JSON, nullable=False)
    status = db.Column(db.String(20), default='pending')
    correlation_id = db.Column(db.String(100), nullable=True)
    workspace_id = db.Column(db.Integer, db.ForeignKey('workspace.id'), nullable=False)
