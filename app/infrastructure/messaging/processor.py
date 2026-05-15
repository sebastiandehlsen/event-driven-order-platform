from app.infrastructure.messaging.publisher import (
    EventPublisher,
)
from app.infrastructure.repositories.order_repository import (
    SqlAlchemyOrderRepository,
)


class OutboxProcessor:

    def __init__(
        self,
        repository: SqlAlchemyOrderRepository,
        publisher: EventPublisher,
    ) -> None:

        self._repository = repository
        self._publisher = publisher

    def process(
        self,
    ) -> None:

        messages = (
            self._repository
            .get_unpublished_messages()
        )

        for message in messages:

            self._publisher.publish(
                message
            )

        self._repository._session.commit()