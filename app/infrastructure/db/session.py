from sqlalchemy import (
    create_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
)


class Base(
    DeclarativeBase
):
    pass


engine = create_engine(
    "sqlite:///orders.db",
    echo=False,
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def create_session_factory(
    database_url: str,
):

    custom_engine = (
        create_engine(
            database_url,
        )
    )

    Base.metadata.create_all(
        bind=custom_engine,
    )

    return sessionmaker(
        bind=custom_engine,
        autoflush=False,
        autocommit=False,
    )


Base.metadata.create_all(
    bind=engine,
)