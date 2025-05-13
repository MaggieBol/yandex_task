import pytest
from delivery.calculate_price import get_fragile_added_value


@pytest.mark.parametrize(("fragile", "added_value"), [(True, 300), (False, 0)])
def test_get_size_added_value_high(fragile, added_value):
    assert added_value == get_fragile_added_value(fragile)
