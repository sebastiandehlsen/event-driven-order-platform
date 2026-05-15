from unittest.mock import patch
import pytest

from app.infrastructure.messaging.dispatcher import (
    OutboxDispatcher,
)


@patch(
    "time.sleep"
)
def test_dispatcher_can_run_loop(
    sleep_mock,
):

    dispatcher = (
        OutboxDispatcher(
            repository=None,
            publisher=None,
        )
    )

    call_count = 0

    def fake_dispatch():

        nonlocal call_count

        call_count += 1

        if call_count == 1:

            raise KeyboardInterrupt

    dispatcher.dispatch = (
        fake_dispatch
    )

    with pytest.raises(
        KeyboardInterrupt
    ):
        dispatcher.run_forever()

    assert (
        call_count
        == 1
    )