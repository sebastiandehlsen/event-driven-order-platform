import json

from app.infrastructure.db.models import (
    OutboxMessageModel,
)
from app.infrastructure.messaging.publisher import (
    EventPublisher,
)


class JsonEventPublisher(
    EventPublisher
):

    def __init__(
        self,
    ) -> None:

        self.messages: list[dict] = []

    def publish(
        self,
        message: OutboxMessageModel,
    ) -> None:

        payload = json.loads(
            message.payload
        )

        broker_message = {
            "event_type": (
                message.event_type
            ),
            "aggregate_id": (
                message.aggregate_id
            ),
            "payload": payload,
        }

        self.messages.append(
            broker_message
        )

        message.published = True