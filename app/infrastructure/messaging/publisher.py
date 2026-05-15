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