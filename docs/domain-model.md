# Event Driven Order Platform

## Core Aggregate

Order

---

## Entities

- Order
- OrderItem

---

## Value Objects

- OrderId
- CustomerId
- ProductId
- Money
- IdempotencyKey

---

## Domain Events

- OrderCreated
- InventoryReserved
- InventoryReservationFailed
- PaymentAuthorized
- PaymentFailed
- OrderConfirmed
- FulfillmentRequested
- OrderFulfilled
- OrderCancelled

---

## Order States

- PENDING
- INVENTORY_RESERVED
- PAYMENT_AUTHORIZED
- CONFIRMED
- FULFILLMENT_REQUESTED
- FULFILLED
- CANCELLED
- REJECTED

---

## Invariants

1. An order must contain at least one order item before it can be created.

2. An order cannot transition to PAYMENT_AUTHORIZED unless inventory has been successfully reserved.

3. An order can only transition to CONFIRMED after payment authorization has succeeded.

4. An order with the same idempotency key must never be created more than once.

5. An order state transition must fail if the aggregate version does not match the expected version.

6. A cancelled or rejected order cannot transition to any active processing state.

7. Payment failure after inventory reservation must trigger inventory release before order cancellation.

8. Every successful state transition must emit exactly one domain event.

9. Every domain event must be traceable using a correlation identifier.

10. Order state transitions must be processed in causal order and cannot skip required intermediate states.