from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4

from app.domain.orders.value_objects import OrderId


@dataclass(frozen=True, kw_only=True)
class DomainEvent:
    correlation_id: UUID

    event_id: UUID = field(
        default_factory=uuid4
    )

    occurred_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                UTC
            )
        )
    )


@dataclass(frozen=True)
class OrderCreated(
    DomainEvent
):
    order_id: OrderId


@dataclass(frozen=True)
class InventoryReserved(
    DomainEvent
):
    order_id: OrderId


@dataclass(frozen=True)
class PaymentAuthorized(
    DomainEvent
):
    order_id: OrderId


@dataclass(frozen=True)
class PaymentFailed(
    DomainEvent
):
    order_id: OrderId


@dataclass(frozen=True)
class OrderConfirmed(
    DomainEvent
):
    order_id: OrderId