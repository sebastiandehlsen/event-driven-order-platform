import json
from unittest.mock import (
    MagicMock,
)

from app.application.event_handlers import (
    EventHandlers,
)


def test_registered_handler_is_called():

    handlers = (
        EventHandlers()
    )

    handler = (
        MagicMock()
    )

    handlers.register(
        "OrderCreated",
        handler,
    )

    payload = {
        "event_type": (
            "OrderCreated"
        ),
    }

    handlers.handle(
        json.dumps(
            payload
        ).encode()
    )

    handler.assert_called_once()