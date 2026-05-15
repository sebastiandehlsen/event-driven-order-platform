from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class OrderId:
    value: UUID

    @classmethod
    def generate(cls) -> "OrderId":
        return cls(value=uuid4())


@dataclass(frozen=True)
class CustomerId:
    value: UUID


@dataclass(frozen=True)
class IdempotencyKey:
    value: str

    def __post_init__(self) -> None:
        if not self.value.strip():
            raise ValueError("idempotency key cannot be empty")