from uuid import UUID

from pydantic import BaseModel


class GetOrderResponse(
    BaseModel,
):
    order_id: UUID
    customer_id: UUID
    status: str