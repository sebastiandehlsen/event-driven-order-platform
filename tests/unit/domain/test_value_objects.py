from uuid import UUID

import pytest

from app.domain.orders.value_objects import (
    CustomerId,
    IdempotencyKey,
    OrderId,
)


def test_order_id_can_be_generated():
    order_id = OrderId.generate()

    assert isinstance(order_id.value, UUID)


def test_customer_id_is_immutable():
    customer_id = CustomerId(value=UUID("12345678-1234-5678-1234-567812345678"))

    assert customer_id.value


def test_idempotency_key_cannot_be_empty():
    with pytest.raises(ValueError):
        IdempotencyKey(value="")