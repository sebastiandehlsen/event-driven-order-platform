from abc import ABC, abstractmethod

from app.domain.orders.entities import Order
from app.domain.orders.value_objects import OrderId


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