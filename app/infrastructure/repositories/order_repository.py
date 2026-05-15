from abc import ABC, abstractmethod

from app.domain.orders.entities import Order
from app.domain.orders.value_objects import OrderId

from sqlalchemy.orm import Session

from app.infrastructure.db.models import (
    OrderModel,
)
from app.infrastructure.mappers.order_mapper import (
    OrderMapper,
)


class OrderRepository(ABC):

    @abstractmethod
    def save(
        self,
        order: Order,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        order_id: OrderId,
    ) -> Order | None:
        raise NotImplementedError
    
class InMemoryOrderRepository(OrderRepository):

    def __init__(self) -> None:
        self._orders: dict[OrderId, Order] = {}

    def save(
        self,
        order: Order,
    ) -> None:
        self._orders[order.order_id] = order

    def get_by_id(
        self,
        order_id: OrderId,
    ) -> Order | None:
        return self._orders.get(order_id)
    
class SqlAlchemyOrderRepository(
    OrderRepository
):

    def __init__(
        self,
        session: Session,
    ) -> None:

        self._session = session

    def save(
        self,
        order: Order,
    ) -> None:

        model = OrderMapper.to_model(
            order
        )

        self._session.merge(
            model
        )

    def get_by_id(
        self,
        order_id: OrderId,
    ) -> Order | None:

        model = self._session.get(
            OrderModel,
            str(order_id.value),
        )

        if model is None:
            return None

        return OrderMapper.to_domain(
            model
        )