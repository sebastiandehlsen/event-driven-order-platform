import time

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

    def run_forever(
        self,
        poll_interval: float = (
            1.0
        ),
    ) -> None:

        while True:

            self.dispatch()

            time.sleep(
                poll_interval
            )