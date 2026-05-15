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

1.

2.

3.

4.

5.