from uuid import UUID

import pytest

from app.domain.orders.entities import Order
from app.domain.orders.enums import OrderStatus
from app.domain.orders.exceptions import (
    EmptyOrderError,
    InvalidOrderStateTransitionError,
)
from app.domain.orders.value_objects import (
    CustomerId,
    IdempotencyKey,
)


def test_order_can_be_created():
    order = Order.create(
        customer_id=CustomerId(
            UUID("12345678-1234-5678-1234-567812345678")
        ),
        idempotency_key=IdempotencyKey("order-request-1"),
        item_count=1,
        correlation_id=UUID(
            "87654321-4321-8765-4321-876543218765"
        ),
    )

    assert order.status == OrderStatus.PENDING
    assert order.version == 1
    assert len(order.pending_events) == 1


def test_empty_order_is_rejected():
    with pytest.raises(EmptyOrderError):
        Order.create(
            customer_id=CustomerId(
                UUID("12345678-1234-5678-1234-567812345678")
            ),
            idempotency_key=IdempotencyKey("order-request-1"),
            item_count=0,
            correlation_id=UUID(
                "87654321-4321-8765-4321-876543218765"
            ),
        )

def test_inventory_can_be_reserved():
    order = Order.create(
        customer_id=CustomerId(
            UUID("12345678-1234-5678-1234-567812345678")
        ),
        idempotency_key=IdempotencyKey("order-request-1"),
        item_count=1,
        correlation_id=UUID(
            "87654321-4321-8765-4321-876543218765"
        ),
    )

    order.reserve_inventory(
        UUID("87654321-4321-8765-4321-876543218765")
    )

    assert order.status == OrderStatus.INVENTORY_RESERVED
    assert order.version == 2
    assert len(order.pending_events) == 2


def test_invalid_inventory_transition_is_rejected():
    order = Order.create(
        customer_id=CustomerId(
            UUID("12345678-1234-5678-1234-567812345678")
        ),
        idempotency_key=IdempotencyKey("order-request-1"),
        item_count=1,
        correlation_id=UUID(
            "87654321-4321-8765-4321-876543218765"
        ),
    )

    order.reserve_inventory(
        UUID("87654321-4321-8765-4321-876543218765")
    )

    with pytest.raises(
        InvalidOrderStateTransitionError
    ):
        order.reserve_inventory(
            UUID("87654321-4321-8765-4321-876543218765")
        )