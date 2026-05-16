FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install uv

RUN uv pip install --system . fastapi uvicorn sqlalchemy pika

EXPOSE 8000

CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]