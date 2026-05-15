from uuid import UUID

from app.domain.orders.events import (
    OrderCreated,
)
from app.domain.orders.value_objects import (
    OrderId,
)
from app.infrastructure.mappers.outbox_mapper import (
    OutboxMapper,
)


def test_domain_event_can_be_mapped_to_outbox():
    event = OrderCreated(
        order_id=OrderId(
            UUID(
                "12345678-1234-5678-1234-567812345678"
            )
        ),
        correlation_id=UUID(
            "87654321-4321-8765-4321-876543218765"
        ),
    )

    model = OutboxMapper.to_model(
        event
    )

    assert model.event_id is not None
    assert model.event_type == (
        "OrderCreated"
    )
    assert model.aggregate_id == (
        "12345678-1234-5678-1234-567812345678"
    )