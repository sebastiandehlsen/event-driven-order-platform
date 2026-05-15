from uuid import UUID

from app.domain.orders.entities import Order
from app.domain.orders.value_objects import (
    CustomerId,
    IdempotencyKey,
)
from app.infrastructure.repositories.order_repository import (
    InMemoryOrderRepository,
)


def test_order_can_be_saved_and_loaded():
    repository = InMemoryOrderRepository()

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

    repository.save(order)

    loaded = repository.get_by_id(
        order.order_id
    )

    assert loaded is not None
    assert loaded.order_id == order.order_id