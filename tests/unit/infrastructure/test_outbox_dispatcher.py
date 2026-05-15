from unittest.mock import MagicMock

from app.infrastructure.messaging.dispatcher import (
    OutboxDispatcher,
)


def test_dispatcher_publishes_all_messages():

    repository = MagicMock()

    publisher = MagicMock()

    messages = [
        MagicMock(),
        MagicMock(),
        MagicMock(),
    ]

    repository.get_unpublished_messages.return_value = (
        messages
    )

    dispatcher = (
        OutboxDispatcher(
            repository,
            publisher,
        )
    )

    dispatcher.dispatch()

    assert (
        publisher.publish.call_count
        == 3
    )