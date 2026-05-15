from unittest.mock import MagicMock, patch

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
from app.infrastructure.messaging.rabbitmq_publisher import (
    RabbitMQPublisher,
)


@patch(
    "pika.BlockingConnection"
)
def test_event_can_be_published_to_rabbitmq(
    connection_mock,
):
    channel = MagicMock()

    connection = MagicMock()

    connection.channel.return_value = (
        channel
    )

    connection_mock.return_value = (
        connection
    )

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

    message = (
        OutboxMapper.to_model(
            event
        )
    )

    publisher = (
        RabbitMQPublisher()
    )

    publisher.publish(
        message
    )

    channel.basic_publish.assert_called_once()

    assert (
        message.published
        is True
    )