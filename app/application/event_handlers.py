import json
from typing import Callable


class EventHandlers:

    def __init__(
        self,
    ) -> None:

        self._handlers: dict[
            str,
            Callable,
        ] = {}

    def register(
        self,
        event_type: str,
        handler: Callable,
    ) -> None:

        self._handlers[
            event_type
        ] = handler

    def handle(
        self,
        event_payload: bytes,
    ) -> None:

        payload = json.loads(
            event_payload.decode()
        )

        event_type = payload[
            "event_type"
        ]

        handler = (
            self._handlers.get(
                event_type
            )
        )

        if handler:

            handler(
                payload
            )