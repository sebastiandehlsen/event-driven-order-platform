from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
)


class Base(
    DeclarativeBase
):
    pass


def create_session_factory(
    database_url: str,
):

    engine = create_engine(
        database_url,
    )

    Base.metadata.create_all(
        bind=engine,
    )

    return sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
    )


# SessionLocal = (
#     create_session_factory(
#         "sqlite:///orders.db"
#     )
# )