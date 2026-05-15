from app.application.order_handlers import (
    OrderCreatedHandler,
)


def test_order_created_handler_runs():

    handler = (
        OrderCreatedHandler()
    )

    payload = {
        "order_id": (
            "123"
        )
    }

    handler(
        payload
    )

    assert True