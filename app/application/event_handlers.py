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
        event_type: str,
        event_payload: dict,
    ) -> None:

        if isinstance(
            event_payload,
            dict,
        ):

            customer = (
                event_payload.get(
                    "customer_id",
                    {},
                )
                .get(
                    "value",
                )
            )

            if customer == (
                "00000000-0000-0000-0000-000000000999"
            ):

                raise Exception(
                    "DLQ demo"
                )

        handler = (
            self._handlers.get(
                event_type
            )
        )

        if handler:

            handler(
                event_payload
            )