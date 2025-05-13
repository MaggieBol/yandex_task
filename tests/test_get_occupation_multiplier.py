import pytest
from delivery.calculate_price import get_occupation_multiplier


def test_get_occupation_multiplier_default():
    assert 1 == get_occupation_multiplier(None)


@pytest.mark.parametrize(
    ("occupation", "multiplier"), [("high", 1.6), ("medium", 1.4), ("low", 1.2)]
)
def test_get_occupation_multiplier_high(occupation, multiplier):
    assert multiplier == get_occupation_multiplier(occupation)
