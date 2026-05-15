from abc import ABC, abstractmethod

from app.infrastructure.db.models import (
    OutboxMessageModel,
)


class EventPublisher(ABC):

    @abstractmethod
    def publish(
        self,
        message: OutboxMessageModel,
    ) -> None:
        raise NotImplementedError
    
class InMemoryEventPublisher(
    EventPublisher
):

    def __init__(
        self,
    ) -> None:

        self.messages: list = []

    def publish(
        self,
        message: OutboxMessageModel,
    ) -> None:

        self.messages.append(
            message
        )

        message.published = True