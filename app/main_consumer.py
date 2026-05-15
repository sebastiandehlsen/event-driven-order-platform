from app.application.event_handlers import (
    EventHandlers,
)
from app.application.order_handlers import (
    OrderCreatedHandler,
)
from app.infrastructure.messaging.consumer import (
    RabbitMQConsumer,
)


def main() -> None:

    handlers = (
        EventHandlers()
    )

    handlers.register(
        "OrderCreated",
        OrderCreatedHandler(),
    )

    consumer = (
        RabbitMQConsumer(
            handlers
        )
    )

    consumer.start()


if __name__ == "__main__":

    main()