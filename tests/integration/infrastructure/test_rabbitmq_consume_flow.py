from uuid import UUID
import time
import os

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


def test_event_can_be_consumed_from_live_rabbitmq():

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

    channel.queue_delete(
        queue="consume-test"
    )

    channel.queue_declare(
        queue="consume-test",
        durable=False,
    )

    channel.queue_bind(
        exchange="orders",
        queue="consume-test",
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
            "consume-test",
            auto_ack=True,
        )
    )

    assert method is not None

    assert body is not None

    connection.close()