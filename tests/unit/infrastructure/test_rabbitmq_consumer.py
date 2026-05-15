from unittest.mock import (
    MagicMock,
    patch,
)

from app.infrastructure.messaging.consumer import (
    RabbitMQConsumer,
)


@patch(
    "pika.BlockingConnection"
)
def test_consumer_can_be_created(
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

    consumer = (
        RabbitMQConsumer()
    )

    assert (
        consumer
        is not None
    )