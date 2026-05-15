from app.application.event_handlers import (
    EventHandlers,
)
from app.application.projection_handlers import (
    OrderCreatedProjectionHandler,
)
from app.infrastructure.db.session import (
    Base,
    SessionLocal,
    engine,
)
from app.infrastructure.messaging.consumer import (
    RabbitMQConsumer,
)
from app.infrastructure.models.order_projection import (
    OrderProjection,
)
from app.infrastructure.repositories.order_projection_repository import (
    OrderProjectionRepository,
)


def main() -> None:

    Base.metadata.create_all(
        bind=engine,
    )

    session = (
        SessionLocal()
    )

    repository = (
        OrderProjectionRepository(
            session
        )
    )

    handlers = (
        EventHandlers()
    )

    handlers.register(
        "OrderCreated",
        OrderCreatedProjectionHandler(
            repository
        ),
    )

    consumer = (
        RabbitMQConsumer(
            handlers
        )
    )

    consumer.start()


if __name__ == "__main__":
    main()