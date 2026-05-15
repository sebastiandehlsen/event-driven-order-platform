from uuid import UUID

from app.domain.orders.events import OrderCreated
from app.domain.orders.value_objects import OrderId


def test_order_created_event_contains_metadata():
    event = OrderCreated(
        order_id=OrderId.generate(),
        correlation_id=UUID("12345678-1234-5678-1234-567812345678"),
    )

    assert event.event_id
    assert event.occurred_at
    assert event.correlation_id