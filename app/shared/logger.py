import json
import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
)

logging.getLogger(
    "pika"
).setLevel(
    logging.WARNING
)


def log_event(
    **kwargs,
) -> None:

    logging.info(
        json.dumps(
            kwargs
        )
    )