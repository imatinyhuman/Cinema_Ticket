import pytest
from src.cinema_entry import can_watch


@pytest.mark.parametrize(
    ("age", "expected_result"),
    [
        (0, False),    # newborn cannot watch
        (10, False),   # below minimum age
        (15, False),   # just below minimum age
        (16, True),    # minimum eligible age
        (17, True),    # just above minimum age
        (18, True),    # adult can watch
        (65, True),    # senior can watch
    ],
)
def test_can_watch(age, expected_result):
    assert can_watch(age) == expected_result


@pytest.mark.parametrize(
    "age",
    [
        -1,    # negative age
        -5,    # invalid negative age
        -100,  # large negative age
    ],
)
def test_can_watch_invalid(age):
    with pytest.raises(ValueError):
        can_watch(age)


@pytest.mark.parametrize(
    "age",
    [
        16.5,     # float instead of integer
        "16",     # string instead of integer
        None,     # None is not an integer
        True,     # boolean is not accepted
    ],
)
def test_can_watch_invalid_type(age):
    with pytest.raises(TypeError):
        can_watch(age)
