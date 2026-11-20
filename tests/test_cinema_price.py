import pytest
from src.cinema_price import ticket_price


@pytest.mark.parametrize(
    ("ticket_count", "expected_price"),
    [
        (0, 0),       # zero tickets should cost 0
        (1, 1200),    # one ticket costs 1200 cents
        (2, 2400),    # two tickets cost 2400 cents
        (5, 6000),    # five tickets cost 6000 cents
        (10, 12000),  # ten tickets cost 12000 cents
    ],
)
def test_ticket_price(ticket_count, expected_price):
    assert ticket_price(ticket_count) == expected_price


@pytest.mark.parametrize(
    "ticket_count",
    [
        -1,    # negative ticket count
        -5,    # multiple negative tickets
        -100,  # large negative ticket count
    ],
)
def test_ticket_price_invalid(ticket_count):
    with pytest.raises(ValueError):
        ticket_price(ticket_count)


@pytest.mark.parametrize(
    "ticket_count",
    [
        1.5,      # float instead of integer
        "2",      # string instead of integer
        None,     # None is not an integer
        True,     # boolean is not accepted
    ],
)
def test_ticket_price_invalid_type(ticket_count):
    with pytest.raises(TypeError):
        ticket_price(ticket_count)
