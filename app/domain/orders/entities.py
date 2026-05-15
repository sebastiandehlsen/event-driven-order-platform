from dataclasses import dataclass, field
from uuid import UUID

from app.domain.orders.enums import OrderStatus
from app.domain.orders.events import (
    InventoryReserved,
    OrderConfirmed,
    OrderCreated,
    PaymentAuthorized,
)
from app.domain.orders.exceptions import (
    EmptyOrderError,
    InvalidOrderStateTransitionError,
)
from app.domain.orders.value_objects import (
    CustomerId,
    IdempotencyKey,
    OrderId,
)


@dataclass
class Order:
    order_id: OrderId
    customer_id: CustomerId
    status: OrderStatus
    version: int
    idempotency_key: IdempotencyKey

    pending_events: list = field(default_factory=list)

    @classmethod
    def create(
        cls,
        customer_id: CustomerId,
        idempotency_key: IdempotencyKey,
        item_count: int,
        correlation_id: UUID,
    ) -> "Order":

        if item_count < 1:
            raise EmptyOrderError()

        order = cls(
            order_id=OrderId.generate(),
            customer_id=customer_id,
            status=OrderStatus.PENDING,
            version=1,
            idempotency_key=idempotency_key,
        )

        order.pending_events.append(
            OrderCreated(
                order_id=order.order_id,
                correlation_id=correlation_id,
            )
        )

        return order

    def reserve_inventory(
        self,
        correlation_id: UUID,
    ) -> None:

        if self.status != OrderStatus.PENDING:
            raise InvalidOrderStateTransitionError()

        self.status = OrderStatus.INVENTORY_RESERVED

        self.version += 1

        self.pending_events.append(
            InventoryReserved(
                order_id=self.order_id,
                correlation_id=correlation_id,
            )
        )
    def mark_payment_authorized(
        self,
        correlation_id: UUID,
) ->     None:

        if self.status != OrderStatus.INVENTORY_RESERVED:
            raise InvalidOrderStateTransitionError()

        self.status = OrderStatus.PAYMENT_AUTHORIZED

        self.version += 1

        self.pending_events.append(
            PaymentAuthorized(
                order_id=self.order_id,
                correlation_id=correlation_id,
            )
        )

    def mark_confirmed(
        self,
        correlation_id: UUID,
) ->     None:
    
        if self.status != OrderStatus.PAYMENT_AUTHORIZED:
            raise InvalidOrderStateTransitionError()
    
        self.status = OrderStatus.CONFIRMED
    
        self.version += 1
    
        self.pending_events.append(
            OrderConfirmed(
                order_id=self.order_id,
                correlation_id=correlation_id,
            )
        )

    def clear_pending_events(self) -> None:
        self.pending_events.clear()