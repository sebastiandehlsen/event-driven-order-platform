from app.infrastructure.db import models

from app.infrastructure.db.session import (
    SessionLocal,
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