from uuid import uuid4

from app.domain.orders.entities import (
    Order,
)
from app.domain.orders.value_objects import (
    CustomerId,
    IdempotencyKey,
)
from app.infrastructure.db.session import (
    SessionLocal,
)
from app.infrastructure.repositories.order_repository import (
    SqlAlchemyOrderRepository,
)


def main() -> None:

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
            idempotency_key=(
                IdempotencyKey(
                    str(
                        uuid4()
                    )
                )
            ),
            item_count=1,
            correlation_id=(
                uuid4()
            ),
        )
    )

    repository.save(
        order
    )

    session.commit()

    print(
        f"Order created: {order.order_id.value}"
    )


if __name__ == "__main__":

    main()