from app.infrastructure.repositories.order_projection_repository import (
    OrderProjectionRepository,
)


class GetOrderQuery:

    def __init__(
        self,
        repository: (
            OrderProjectionRepository
        ),
    ) -> None:

        self._repository = (
            repository
        )

    def execute(
        self,
        order_id: str,
    ) -> dict | None:

        projection = (
            self._repository.get_by_id(
                order_id
            )
        )

        if not projection:

            return None

        return {
            "order_id": (
                projection.order_id
            ),
            "customer_id": (
                projection.customer_id
            ),
            "status": (
                projection.status
            ),
        }