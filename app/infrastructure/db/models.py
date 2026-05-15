from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.session import Base


class OrderModel(Base):
    __tablename__ = "orders"

    order_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    customer_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    idempotency_key: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )

class OutboxMessageModel(Base):
    __tablename__ = "outbox_messages"

    event_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    event_type: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    aggregate_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    payload: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    occurred_at: Mapped[datetime] = (
        mapped_column(
            DateTime,
            nullable=False,
        )
    )
    
    published: Mapped[bool] = mapped_column(
        default=False,
        nullable=False,
    )