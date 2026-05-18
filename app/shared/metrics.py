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


def get_metric(
    metric_name: str,
) -> int:

    return _metrics[
        metric_name
    ]


def snapshot(
) -> dict:

    return dict(
        _metrics
    )