from app.infrastructure.db import models

from app.infrastructure.db.session import (
    create_session_factory,
)
from app.infrastructure.messaging.dispatcher import (
    OutboxDispatcher,
)
from app.infrastructure.messaging.rabbitmq_publisher import (
    RabbitMQPublisher,
)
from app.infrastructure.repositories.order_repository import (
    SqlAlchemyOrderRepository,
)


def main() -> None:

    _ = models

    SessionLocal = (
        create_session_factory(
            "sqlite:///orders.db"
        )
    )

    session = (
        SessionLocal()
    )

    repository = (
        SqlAlchemyOrderRepository(
            session
        )
    )

    publisher = (
        RabbitMQPublisher()
    )

    dispatcher = (
        OutboxDispatcher(
            repository,
            publisher,
        )
    )

    dispatcher.run_forever()


if __name__ == "__main__":

    main()