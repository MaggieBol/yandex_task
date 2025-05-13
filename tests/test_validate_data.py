import pytest

from delivery.calculate_price import validate_input_data
from delivery.exceptions import (
    WrongDistanceValue,
    WrongFragileValue,
    WrongOccupationValue,
    WrongSizeValue,
    UnsupportedDeliveryParameters,
)


def test_raise_exception_on_wrong_occumpation_value():
    with pytest.raises(WrongOccupationValue):
        validate_input_data(
            size="large", occupation="wrong value", fragile=False, distance=5
        )


def test_raise_exception_on_wrong_distance_type():
    with pytest.raises(WrongDistanceValue):
        validate_input_data(
            size="large", occupation="high", fragile=False, distance="far far away"
        )


@pytest.mark.parametrize("value", [-1, 0, -1.1])
def test_raise_exception_on_distance_negative_value(value):
    with pytest.raises(WrongDistanceValue):
        validate_input_data(
            size="large", occupation="high", fragile=False, distance=value
        )


def test_raise_exception_on_wrong_fragile_value():
    with pytest.raises(WrongFragileValue):
        validate_input_data(size="large", occupation="high", fragile=1, distance=1)


def test_raise_exception_on_wrong_size_value():
    with pytest.raises(WrongSizeValue):
        validate_input_data(
            size="very large", occupation="high", fragile=False, distance=1
        )


def test_raise_exception_wrong_distance_on_fragile_and_30km():
    with pytest.raises(UnsupportedDeliveryParameters):
        validate_input_data(size="large", occupation="high", fragile=True, distance=35)
