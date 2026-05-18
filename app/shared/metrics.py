from collections import defaultdict


_metrics = defaultdict(
    int
)


def increment(
    metric_name: str,
) -> None:

    _metrics[
        metric_name
    ] += 1


def snapshot(
) -> dict:

    return dict(
        _metrics
    )