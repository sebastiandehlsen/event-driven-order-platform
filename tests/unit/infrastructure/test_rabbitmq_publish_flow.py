from uuid import UUID, uuid4
import time
import os

import pika

from app.domain.orders.events import (
    OrderCreated,
)
from app.domain.orders.value_objects import (
    CustomerId,
    OrderId,
)
from app.infrastructure.mappers.outbox_mapper import (
    OutboxMapper,
)
from app.infrastructure.messaging.rabbitmq_publisher import (
    RabbitMQPublisher,
)


def test_event_can_be_published_to_live_rabbitmq():

    queue_name = (
        f"test-orders-{uuid4()}"
    )

    connection = (
        pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.getenv(
                    "RABBITMQ_HOST",
                    "localhost",
                ),
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

    channel = (
        connection.channel()
    )

    publisher = (
        RabbitMQPublisher()
    )

    channel.queue_declare(
        queue=queue_name,
        durable=False,
    )

    channel.queue_bind(
        exchange="orders",
        queue=queue_name,
        routing_key="#",
    )

    event = (
        OrderCreated(
            order_id=OrderId(
                UUID(
                    "12345678-1234-5678-1234-567812345678",
                )
            ),
            customer_id=CustomerId(
                UUID(
                    "11111111-1111-1111-1111-111111111111",
                )
            ),
            correlation_id=UUID(
                "87654321-4321-8765-4321-876543218765",
            ),
        )
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
            queue_name,
            auto_ack=True,
        )
    )

    assert method is not None
    assert body is not None

    publisher._connection.close()

    connection.close()