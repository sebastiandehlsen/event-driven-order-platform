import json
from dataclasses import asdict

from app.domain.orders.events import (
    DomainEvent,
)
from app.infrastructure.db.models import (
    OutboxMessageModel,
)


class OutboxMapper:

    @staticmethod
    def to_model(
        event: DomainEvent,
    ) -> OutboxMessageModel:

        payload = json.dumps(
            asdict(
                event,
            ),
            default=str,
        )

        aggregate_id = str(
            event.order_id.value
        )

        return OutboxMessageModel(
            event_id=str(
                event.event_id
            ),
            event_type=type(
                event
            ).__name__,
            aggregate_id=aggregate_id,
            payload=payload,
            occurred_at=event.occurred_at,
        )