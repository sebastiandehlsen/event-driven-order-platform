from app.domain.orders.enums import OrderStatus


def test_order_status_values_are_stable():
    assert OrderStatus.PENDING == "PENDING"
    assert OrderStatus.FULFILLED == "FULFILLED"
    assert OrderStatus.CANCELLED == "CANCELLED"