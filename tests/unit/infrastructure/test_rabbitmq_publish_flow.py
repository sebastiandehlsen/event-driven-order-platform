from uuid import UUID
import time

import pika

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


def test_event_can_be_published_to_live_rabbitmq():

    connection = (
        pika.BlockingConnection(
            pika.ConnectionParameters(
                host="localhost",
                port=5672,
                credentials=(
                    pika.PlainCredentials(
                        "admin",
                        "admin",
                    )
                ),
            )
        )
    )

    channel = connection.channel()

    publisher = (
        RabbitMQPublisher()
    )

    channel.queue_delete(
        queue="test-orders"
    )

    channel.queue_declare(
        queue="test-orders",
        durable=False,
    )

    channel.queue_bind(
        exchange="orders",
        queue="test-orders",
        routing_key="#",
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

    publisher.publish(
        message
    )

    time.sleep(
        0.2
    )

    method, _, body = (
        channel.basic_get(
            "test-orders",
            auto_ack=True,
        )
    )

    assert method is not None
    assert body is not None

    connection.close()