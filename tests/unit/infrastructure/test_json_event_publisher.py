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
from app.infrastructure.messaging.json_publisher import (
    JsonEventPublisher,
)


def test_json_event_can_be_published():
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

    message = OutboxMapper.to_model(
        event
    )

    publisher = (
        JsonEventPublisher()
    )

    publisher.publish(
        message
    )

    assert len(
        publisher.messages
    ) == 1

    assert (
        message.published
        is True
    )