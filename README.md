# Event-Driven Order Platform

A production-inspired event-driven order processing platform built with Python, FastAPI, RabbitMQ, SQLAlchemy, Docker, Prometheus, Grafana, and GitHub Actions.

Designed around real-world distributed systems patterns including Domain-Driven Design, CQRS, Event-Driven Messaging, Transactional Outbox Pattern, Dead Letter Queues, Idempotency, Structured Logging, Metrics, Observability, and Correlation Tracing.

---

## Features

- Domain-Driven Design (DDD)
- CQRS architecture
- Event-driven messaging with RabbitMQ
- Transactional Outbox Pattern
- Projection-based read models
- Saga-style compensation flows
- Dead Letter Queue (DLQ)
- Idempotent command handling
- Structured JSON logging
- Correlation ID tracing
- Prometheus metrics scraping
- Grafana live dashboards
- Dockerized microservices
- Automated CI pipeline
- Unit + integration tests

---

## Architecture

```text
Client
   ↓
FastAPI
   ↓
Commands
   ↓
Domain Aggregate
   ↓
SQL Write Model
   ↓
Outbox Table
   ↓
Dispatcher
   ↓
RabbitMQ Exchange
   ↓
Consumer
   ↓
Projection Handlers
   ↓
Read Model
```

---

## Event Flow

Successful flow:

```text
OrderCreated
    ↓
InventoryReserved
    ↓
PaymentAuthorized
    ↓
OrderConfirmed
```

Compensation flow:

```text
OrderCreated
    ↓
InventoryReserved
    ↓
PaymentFailed
    ↓
InventoryReleased
    ↓
Cancelled
```

---

## Dead Letter Flow

If event handling fails:

```text
RabbitMQ
   ↓
order-events
   ↓ failure
order-events-dlq
```

Failed events are acknowledged manually and routed to the Dead Letter Queue for later inspection.

---

## Observability

### Structured Logging

Example:

```json
{
  "service": "consumer",
  "correlation_id": "db8bc127-ce6c-4d7a-8112-1610dd9ca9a1",
  "event": "OrderCreated"
}
```

---

### Metrics

Prometheus scrapes live service metrics:

```text
GET /metrics
```

Example:

```text
orders_created_total 42
```

---

### Dashboards

Grafana visualizes live business metrics:

```text
Orders Created
Consumer Failures
```

---

### Correlation Tracing

Every domain event carries:

- correlation_id
- event_id
- occurred_at

This enables full traceability across:

```text
API → Command → Outbox → Dispatcher → RabbitMQ → Consumer → Projection
```

---

## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- RabbitMQ
- Docker + Docker Compose
- Prometheus
- Grafana
- Pytest
- GitHub Actions

---

## Run Locally

### Clone repository

```bash
git clone https://github.com/sebastiandehlsen/event-driven-order-platform.git
cd event-driven-order-platform
```

### Create virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run with Docker

```bash
docker compose up -d --build
```

Services:

- API Docs: http://localhost:8000/docs
- RabbitMQ Management: http://localhost:15672
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

Credentials:

```text
admin / admin
```

---

## Run Tests

```bash
python -m pytest -vv
```

Current test suite:

```text
30 tests passing
```

---

## API Endpoints

### Core

```text
POST /orders
GET /orders/{order_id}
```

### Workflow

```text
POST /orders/{order_id}/reserve-inventory
POST /orders/{order_id}/authorize-payment
POST /orders/{order_id}/fail-payment
POST /orders/{order_id}/release-inventory
POST /orders/{order_id}/confirm
```

### Observability

```text
GET /health
GET /metrics
```

---

## Continuous Integration

GitHub Actions automatically runs:

- Unit tests
- Integration tests
- RabbitMQ integration tests
- Docker build verification

---

## Project Status

Current release:

```text
v0.3.0
```

Status:

✅ Active  
✅ CI passing  
✅ Dockerized  
✅ Event-driven  
✅ CQRS operational  
✅ RabbitMQ integration verified  
✅ DLQ operational  
✅ Idempotency implemented  
✅ Structured logging operational  
✅ Prometheus operational  
✅ Grafana operational  
✅ Correlation tracing operational  

---

## Author

Sebastian Dehlsen