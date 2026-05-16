from fastapi import (
    FastAPI,
    HTTPException,
)

from app.application.commands.create_order_command import (
    CreateOrderCommand,
)
from app.application.queries.get_order_query import (
    GetOrderQuery,
)
from app.infrastructure.db.session import (
    SessionLocal,
)
from app.infrastructure.repositories.order_projection_repository import (
    OrderProjectionRepository,
)
from app.infrastructure.repositories.order_repository import (
    SqlAlchemyOrderRepository,
)

from app.application.commands.reserve_inventory_command import (
    ReserveInventoryCommand,
)


app = (
    FastAPI()
)


@app.post(
    "/orders",
)
def create_order():

    session = (
        SessionLocal()
    )

    repository = (
        SqlAlchemyOrderRepository(
            session
        )
    )

    command = (
        CreateOrderCommand(
            repository
        )
    )

    order_id = (
        command.execute()
    )

    return {
        "order_id": (
            order_id
        ),
    }

@app.post(
    "/orders/{order_id}/reserve-inventory",
)
def reserve_inventory(
    order_id: str,
):

    session = (
        SessionLocal()
    )

    repository = (
        SqlAlchemyOrderRepository(
            session
        )
    )

    command = (
        ReserveInventoryCommand(
            repository
        )
    )

    command.execute(
        order_id
    )

    return {
        "status": (
            "inventory_reserved"
        ),
    }



@app.get(
    "/orders/{order_id}",
)
def get_order(
    order_id: str,
) -> dict:

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
            order_id
        )
    )

    if not order:

        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return order