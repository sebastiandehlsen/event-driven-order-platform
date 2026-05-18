import os


def pytest_sessionstart(
    session,
) -> None:

    os.environ.setdefault(
        "RABBITMQ_HOST",
        "localhost",
    )