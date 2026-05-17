from fastapi import (
    FastAPI,
    HTTPException,
)

from app.domain.orders.exceptions import (
    EmptyOrderError,
)

from app.api.schemas.get_order_response import (
    GetOrderResponse,
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

from app.application.commands.authorize_payment_command import (
    AuthorizePaymentCommand,
)

from app.application.commands.confirm_order_command import (
    ConfirmOrderCommand,
)

from app.application.commands.fail_payment_command import (
    FailPaymentCommand,
)

from app.application.commands.release_inventory_command import (
    ReleaseInventoryCommand,
)

from app.api.schemas.create_order_request import (
    CreateOrderRequest,
)

from app.api.schemas.create_order_response import (
    CreateOrderResponse,
)


app = (
    FastAPI()
)

@app.get(
    "/health",
)
def health():
    return {
        "status": "ok",
    }

@app.post(
    "/orders",
    response_model=CreateOrderResponse,
)
def create_order(
    request: CreateOrderRequest,
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
        CreateOrderCommand(
            repository
        )
    )

    try:

        order_id = (
            command.execute(
                customer_id=(
                    request.customer_id
                ),
                item_count=(
                    request.item_count
                ),
            )
        )

    except EmptyOrderError:

        raise HTTPException(
            status_code=400,
            detail=(
                "Order must contain at least one item"
            ),
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

@app.post(
    "/orders/{order_id}/authorize-payment",
)
def authorize_payment(
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
        AuthorizePaymentCommand(
            repository
        )
    )

    command.execute(
        order_id
    )

    return {
        "status": (
            "payment_authorized"
        ),
    }

@app.post(
    "/orders/{order_id}/fail-payment",
)
def fail_payment(
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
        FailPaymentCommand(
            repository
        )
    )

    command.execute(
        order_id
    )

    return {
        "status": (
            "payment_failed"
        ),
    }

@app.post(
    "/orders/{order_id}/release-inventory",
)
def release_inventory(
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
        ReleaseInventoryCommand(
            repository
        )
    )

    command.execute(
        order_id
    )

    return {
        "status": (
            "inventory_released"
        ),
    }

@app.post(
    "/orders/{order_id}/confirm",
)
def confirm_order(
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
        ConfirmOrderCommand(
            repository
        )
    )

    command.execute(
        order_id
    )

    return {
        "status": (
            "confirmed"
        ),
    }





@app.get(
    "/orders/{order_id}",
    response_model=GetOrderResponse,
)
def get_order(
    order_id: str,
):

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