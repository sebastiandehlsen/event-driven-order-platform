from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4

from app.domain.orders.value_objects import OrderId


@dataclass(frozen=True)
class OrderCreated:
    order_id: OrderId
    correlation_id: UUID

    event_id: UUID = field(default_factory=uuid4)

    occurred_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )