# Event-Driven Order Platform

A production-inspired event-driven order processing platform built with Python, FastAPI, RabbitMQ, SQLAlchemy, Docker, and GitHub Actions.

## Features

- Domain-Driven Design (DDD)
- CQRS architecture
- Event-driven messaging with RabbitMQ
- Outbox pattern
- Projection-based read models
- Compensation flows (Saga-like behavior)
- Dockerized microservices
- Automated CI pipeline with GitHub Actions
- Unit + integration tests

---

## Architecture

```text
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
RabbitMQ
   ↓
Consumers
   ↓
Projections
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

## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- RabbitMQ
- Docker + Docker Compose
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
pip install fastapi uvicorn sqlalchemy pika pytest
```

---

## Run with Docker

```bash
docker compose up -d --build
```

Services:

- API Docs: http://localhost:8000/docs
- RabbitMQ Management: http://localhost:15672

Credentials:

```text
admin / admin
```

---

## Run Tests

```bash
python -m pytest -vv
```

---

## Health Check

```bash
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

## Continuous Integration

GitHub Actions automatically runs:

- Unit tests
- Integration tests
- RabbitMQ integration checks
- Docker build verification

---

## Project Status

Current release:

```text
v0.1.0
```

Status:

✅ Active  
✅ CI passing  
✅ Dockerized  
✅ Event-driven  
✅ CQRS operational  
✅ RabbitMQ integration verified  

---

## Author

Sebastian Dehlsen