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