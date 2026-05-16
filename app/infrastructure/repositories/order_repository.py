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

from app.infrastructure.mappers.outbox_mapper import (
    OutboxMapper,
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

        order_model = (
            OrderMapper.to_model(
                order
            )
        )

        self._session.merge(
            order_model
        )

        for event in (
            order.pending_events
        ):

            outbox_model = (
                OutboxMapper.to_model(
                    event
                )
            )

            self._session.add(
                outbox_model
            )

        self._session.commit()

        order.clear_pending_events()

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

    def get_unpublished_messages(
        self,
    ) -> list:

        from app.infrastructure.db.models import (
            OutboxMessageModel,
        )

        return (
            self._session.query(
                OutboxMessageModel
            )
            .filter_by(
                published=False
            )
            .all()
        )