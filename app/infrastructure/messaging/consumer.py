import json
import os
import time

import pika

from app.shared.logger import (
    log_event,
)

from app.application.event_handlers import (
    EventHandlers,
)


class RabbitMQConsumer:

    def __init__(
        self,
        handlers: EventHandlers,
    ) -> None:

        self._handlers = (
            handlers
        )

        while True:

            try:

                self._connection = (
                    pika.BlockingConnection(
                        pika.ConnectionParameters(
                            host=os.getenv(
                                "RABBITMQ_HOST",
                                "rabbitmq",
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

                break

            except Exception:

                log_event(
                    service="consumer",
                    event="rabbitmq_waiting",
                )

                time.sleep(
                    2
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
            queue="order-events-dlq",
            durable=True,
        )

        self._channel.queue_declare(
            queue="order-events",
            durable=True,
            arguments={
                "x-dead-letter-exchange": "",
                "x-dead-letter-routing-key": ( "order-events-dlq" ),
            },
        )

        self._channel.queue_bind(
            exchange="orders",
            queue="order-events",
            routing_key="#",
        )

    def start(
        self,
    ) -> None:

        log_event(
            service="consumer",
            event="consumer_started",
        )

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

            log_event(
                service="consumer",
                correlation_id=(
                    payload[
                        "correlation_id"
                    ]
                ),
                event=method.routing_key,
                payload=payload,
            )

            try:
            
                self._handlers.handle(
                    method.routing_key,
                    payload,
                )

                ch.basic_ack(
                    delivery_tag=(
                        method.delivery_tag
                    )
                )

            except Exception:
            
                log_event(
                    service="consumer",
                    correlation_id=(
                        payload[
                            "correlation_id"
                        ]
                    ),
                    event="handler_failed",
                    payload=payload,
                )

                ch.basic_nack(
                    delivery_tag=(
                        method.delivery_tag
                    ),
                    requeue=False,
                )

        self._channel.basic_consume(
            queue="order-events",
            on_message_callback=callback,
            auto_ack=False,
        )

        self._channel.start_consuming()