from uuid import (
    uuid4,
)

from app.domain.orders.value_objects import (
    OrderId,
)
from app.infrastructure.repositories.order_repository import (
    SqlAlchemyOrderRepository,
)


class ConfirmOrderCommand:

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
        order_id: str,
    ) -> None:

        order = (
            self._repository.get_by_id(
                OrderId(
                    order_id
                )
            )
        )

        if order is None:

            return

        order.mark_confirmed(
            correlation_id=(
                uuid4()
            )
        )

        self._repository.save(
            order
        )