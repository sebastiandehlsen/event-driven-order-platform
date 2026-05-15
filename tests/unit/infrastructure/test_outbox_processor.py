from uuid import UUID

from app.domain.orders.events import (
    OrderCreated,
)
from app.domain.orders.value_objects import (
    OrderId,
)
from app.infrastructure.mappers.outbox_mapper import (
    OutboxMapper,
)
from app.infrastructure.messaging.publisher import (
    InMemoryEventPublisher,
)
from app.infrastructure.repositories.order_repository import (
    InMemoryOrderRepository,
)
from app.infrastructure.messaging.processor import (
    OutboxProcessor,
)


def test_outbox_processor_publishes_messages():
    event = OrderCreated(
        order_id=OrderId(
            UUID(
                "12345678-1234-5678-1234-567812345678"
            )
        ),
        correlation_id=UUID(
            "87654321-4321-8765-4321-876543218765"
        ),
    )

    message = OutboxMapper.to_model(
        event
    )

    repository = (
        InMemoryOrderRepository()
    )

    repository._messages = [
        message
    ]

    repository.get_unpublished_messages = (
        lambda: repository._messages
    )

    repository._session = type(
        "SessionStub",
        (),
        {
            "commit": lambda self: None
        },
    )()

    publisher = (
        InMemoryEventPublisher()
    )

    processor = OutboxProcessor(
        repository=repository,
        publisher=publisher,
    )

    processor.process()

    assert len(
        publisher.messages
    ) == 1

    assert (
        message.published
        is True
    )