from sqlalchemy.orm import (
    Session,
)

from app.infrastructure.models.order_projection import (
    OrderProjection,
)


class OrderProjectionRepository:

    def __init__(
        self,
        session: Session,
    ) -> None:

        self._session = (
            session
        )

    def save(
        self,
        projection: (
            OrderProjection
        ),
    ) -> None:

        existing = (
            self._session.get(
                OrderProjection,
                projection.order_id,
            )
        )

        if existing:

            return

        self._session.add(
            projection
        )

        self._session.commit()

    def get_by_id(
        self,
        order_id: str,
    ) -> (
        OrderProjection
        | None
    ):

        return (
            self._session.get(
                OrderProjection,
                order_id,
            )
        )