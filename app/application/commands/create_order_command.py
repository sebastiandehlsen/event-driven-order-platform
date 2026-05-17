from uuid import (
    UUID,
    uuid4,
)

from app.domain.orders.entities import (
    Order,
)
from app.domain.orders.value_objects import (
    CustomerId,
    IdempotencyKey,
)
from app.infrastructure.repositories.order_repository import (
    SqlAlchemyOrderRepository,
)


class CreateOrderCommand:

    def __init__(
        self,
        repository: (
            SqlAlchemyOrderRepository
        ),
    ) -> None:

        self._repository = (
            repository
        )

    def execute(
        self,
        customer_id: UUID,
        item_count: int,
    ) -> str:

        order = (
            Order.create(
                customer_id=(
                    CustomerId(
                        customer_id
                    )
                ),
                idempotency_key=(
                    IdempotencyKey(
                        str(
                            uuid4()
                        )
                    )
                ),
                item_count=(
                    item_count
                ),
                correlation_id=(
                    uuid4()
                ),
            )
        )

        self._repository.save(
            order
        )

        return str(
            order.order_id.value
        )