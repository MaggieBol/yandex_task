import pytest
from delivery.calculate_price import get_size_added_value


@pytest.mark.parametrize(("size", "added_value"), [("large", 200), ("small", 100)])
def test_get_size_added_value_high(size, added_value):
    assert added_value == get_size_added_value(size)
