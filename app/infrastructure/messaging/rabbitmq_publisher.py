import pika

from app.infrastructure.db.models import (
    OutboxMessageModel,
)
from app.infrastructure.messaging.publisher import (
    EventPublisher,
)


class RabbitMQPublisher(
    EventPublisher
):

    def __init__(
        self,
    ) -> None:

        self._connection = (
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

        self._channel = (
            self._connection.channel()
        )

        self._channel.exchange_declare(
            exchange="orders",
            exchange_type="topic",
            durable=True,
        )

    def publish(
        self,
        message: OutboxMessageModel,
    ) -> None:

        routing_key = (
            message.event_type
        )

        self._channel.basic_publish(
            exchange="orders",
            routing_key=routing_key,
            body=message.payload,
        )

        message.published = True