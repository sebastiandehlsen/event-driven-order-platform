from app.infrastructure.repositories.order_repository import (
    SqlAlchemyOrderRepository,
)
from app.infrastructure.messaging.publisher import (
    EventPublisher,
)


class OutboxDispatcher:

    def __init__(
        self,
        repository: (
            SqlAlchemyOrderRepository
        ),
        publisher: (
            EventPublisher
        ),
    ) -> None:

        self._repository = (
            repository
        )

        self._publisher = (
            publisher
        )

    def dispatch(
        self,
    ) -> None:

        messages = (
            self._repository.get_unpublished_messages()
        )

        for message in messages:

            self._publisher.publish(
                message
            )