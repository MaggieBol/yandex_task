import pytest

from delivery.calculate_price import get_distance_added_value


@pytest.mark.parametrize(
    ("distance", "added_value"), [(1, 50), (5, 100), (15, 200), (25, 200), (35, 300)]
)
def test_added_value_per_km(distance, added_value):
    assert added_value == get_distance_added_value(distance)
