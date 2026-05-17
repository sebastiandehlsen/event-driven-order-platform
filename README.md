# Event-Driven Order Platform

A production-inspired event-driven order processing platform built with Python, FastAPI, RabbitMQ, SQLAlchemy, Docker, and GitHub Actions.

## Features

- Domain-Driven Design (DDD)
- CQRS architecture
- Event-driven messaging with RabbitMQ
- Outbox pattern
- Compensation flows (Saga-like behavior)
- Dockerized services
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
Outbox Table
   ↓
RabbitMQ
   ↓
Consumers
   ↓
Read Model / Projections
```

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

### Clone

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
docker compose up --build
```

Services:

- API: http://localhost:8000/docs
- RabbitMQ UI: http://localhost:15672

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

Returns:

```json
{
  "status": "ok"
}
```

---

## CI

GitHub Actions automatically runs:

- Unit tests
- Integration tests
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

---

## Author

Sebastian Dehlsen