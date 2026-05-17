from uuid import UUID

from pydantic import BaseModel


class CreateOrderRequest(
    BaseModel,
):
    customer_id: UUID
    item_count: int