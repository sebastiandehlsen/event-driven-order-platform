from sqlalchemy import (
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.infrastructure.db.session import (
    Base,
)


class OrderProjection(
    Base
):

    __tablename__ = (
        "order_projections"
    )

    order_id: Mapped[
        str
    ] = mapped_column(
        String,
        primary_key=True,
    )

    customer_id: Mapped[
        str
    ] = mapped_column(
        String,
        nullable=False,
    )

    status: Mapped[
        str
    ] = mapped_column(
        String,
        nullable=False,
    )