from uuid import UUID

from app.domain.orders.entities import Order
from app.domain.orders.value_objects import (
    CustomerId,
    IdempotencyKey,
)
from app.infrastructure.mappers.order_mapper import (
    OrderMapper,
)


def test_order_can_be_mapped_to_model():
    order = Order.create(
        customer_id=CustomerId(
            UUID("12345678-1234-5678-1234-567812345678")
        ),
        idempotency_key=IdempotencyKey(
            "order-request-1"
        ),
        item_count=1,
        correlation_id=UUID(
            "87654321-4321-8765-4321-876543218765"
        ),
    )

    model = OrderMapper.to_model(order)

    assert model.order_id is not None
    assert model.status == "PENDING"


def test_model_can_be_mapped_to_domain():
    order = Order.create(
        customer_id=CustomerId(
            UUID("12345678-1234-5678-1234-567812345678")
        ),
        idempotency_key=IdempotencyKey(
            "order-request-1"
        ),
        item_count=1,
        correlation_id=UUID(
            "87654321-4321-8765-4321-876543218765"
        ),
    )

    model = OrderMapper.to_model(order)

    restored = OrderMapper.to_domain(
        model
    )

    assert restored.order_id == order.order_id
    assert restored.status == order.status