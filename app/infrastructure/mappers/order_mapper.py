from uuid import UUID

from app.domain.orders.entities import Order
from app.domain.orders.enums import OrderStatus
from app.domain.orders.value_objects import (
    CustomerId,
    IdempotencyKey,
    OrderId,
)
from app.infrastructure.db.models import OrderModel


class OrderMapper:

    @staticmethod
    def to_model(
        order: Order,
    ) -> OrderModel:

        return OrderModel(
            order_id=str(order.order_id.value),
            customer_id=str(
                order.customer_id.value
            ),
            status=order.status.value,
            version=order.version,
            idempotency_key=(
                order.idempotency_key.value
            ),
        )

    @staticmethod
    def to_domain(
        model: OrderModel,
    ) -> Order:

        return Order(
            order_id=OrderId(
                UUID(model.order_id)
            ),
            customer_id=CustomerId(
                UUID(model.customer_id)
            ),
            status=OrderStatus(
                model.status
            ),
            version=model.version,
            idempotency_key=(
                IdempotencyKey(
                    model.idempotency_key
                )
            ),
        )