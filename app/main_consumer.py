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

from app.application.inventory_reserved_handler import (
    InventoryReservedHandler,
)

from app.application.payment_authorized_handler import (
    PaymentAuthorizedHandler,
)

from app.application.order_confirmed_handler import (
    OrderConfirmedHandler,
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

    handlers.register(
        "InventoryReserved",
        InventoryReservedHandler(
            repository
        ),
    )

    handlers.register(
        "PaymentAuthorized",
        PaymentAuthorizedHandler(
            repository
        ),
    )

    handlers.register(
        "OrderConfirmed",
        OrderConfirmedHandler(
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