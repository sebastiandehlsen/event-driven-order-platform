from app.infrastructure.models.order_projection import (
    OrderProjection,
)
from app.infrastructure.repositories.order_projection_repository import (
    OrderProjectionRepository,
)


class OrderCreatedProjectionHandler:

    def __init__(
        self,
        repository: OrderProjectionRepository,
    ) -> None:

        self._repository = repository

    def __call__(
        self,
        payload: dict,
    ) -> None:

        projection = OrderProjection(
            order_id=payload["order_id"]["value"],
            customer_id=payload["order_id"]["value"],
            status="CREATED",
        )

        self._repository.save(
            projection
        )