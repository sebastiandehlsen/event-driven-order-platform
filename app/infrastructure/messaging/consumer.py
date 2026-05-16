import json

import pika

from app.application.event_handlers import (
    EventHandlers,
)


class RabbitMQConsumer:

    def __init__(
        self,
        handlers: (
            EventHandlers
        ),
    ) -> None:

        self._handlers = (
            handlers
        )

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

        self._channel.queue_declare(
            queue="order-events",
            durable=True,
        )

        self._channel.queue_bind(
            exchange="orders",
            queue="order-events",
            routing_key="#",
        )

    def start(
        self,
    ) -> None:

        def callback(
            ch,
            method,
            properties,
            body,
        ):

            payload = (
                json.loads(
                    body.decode()
                )
            )

            print(
                method.routing_key,
                payload,
            )

            self._handlers.handle(
                method.routing_key,
                payload,
            )

        self._channel.basic_consume(
            queue="order-events",
            on_message_callback=callback,
            auto_ack=True,
        )

        self._channel.start_consuming()