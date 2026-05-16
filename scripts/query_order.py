from app.application.queries.get_order_query import (
    GetOrderQuery,
)
from app.infrastructure.db.session import (
    SessionLocal,
)
from app.infrastructure.repositories.order_projection_repository import (
    OrderProjectionRepository,
)


def main() -> None:

    session = (
        SessionLocal()
    )

    repository = (
        OrderProjectionRepository(
            session
        )
    )

    query = (
        GetOrderQuery(
            repository
        )
    )

    order = (
        query.execute(
            input(
                "Order id: "
            )
        )
    )

    print(
        order
    )


if __name__ == "__main__":

    main()