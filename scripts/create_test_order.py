from uuid import uuid4

from app.domain.orders.entities import (
    Order,
)
from app.domain.orders.value_objects import (
    CustomerId,
    IdempotencyKey,
)
from app.infrastructure.db import models
from app.infrastructure.db.session import (
    create_session_factory,
)
from app.infrastructure.repositories.order_repository import (
    SqlAlchemyOrderRepository,
)


def main() -> None:

    _ = models

    SessionLocal = (
        create_session_factory(
            "sqlite:///orders.db"
        )
    )

    session = (
        SessionLocal()
    )

    repository = (
        SqlAlchemyOrderRepository(
            session
        )
    )

    order = (
        Order.create(
            customer_id=(
                CustomerId.generate()
            ),
            item_count=1,
            correlation_id=(
                uuid4()
            ),
            idempotency_key=(
                IdempotencyKey(
                    str(uuid4())
                )
            ),
        )
    )

    repository.save(
        order
    )

    session.commit()

    print(
        "Order created"
    )


if __name__ == "__main__":

    main()