from app.infrastructure.repositories.order_projection_repository import (
    OrderProjectionRepository,
)


class InventoryReleasedHandler:

    def __init__(
        self,
        repository: (
            OrderProjectionRepository
        ),
    ) -> None:

        self._repository = (
            repository
        )

    def __call__(
        self,
        payload: dict,
    ) -> None:

        order_id = (
            payload[
                "order_id"
            ][
                "value"
            ]
        )

        projection = (
            self._repository.get_by_id(
                order_id
            )
        )

        if projection is None:

            return

        projection.status = (
            "CANCELLED"
        )

        self._repository.commit()