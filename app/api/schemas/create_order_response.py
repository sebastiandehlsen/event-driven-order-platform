from uuid import UUID

from pydantic import BaseModel


class CreateOrderResponse(
    BaseModel,
):
    order_id: UUID