import pytest

from delivery import calculate_price
from delivery import exceptions


def data_set():
    """Generator for test data and expected results

    used output from generate_pairwise_test_data.py
    to choose combination of all parameters to cover
    with 20% of tests check 80% of functionality

    data set has next order of parameters:
    `distance, fragile, occupation, size`

    Manually or using another validator calculated
    expected delivery price in expected_prices

    add expected result to row with tested data and return
    row for test
    """
    parameters_data_set = [
        [1, True, "high", "large"],
        [5, False, "medium", "large"],
        [25, False, "low", "small"],
        [25, True, "medium", "small"],
        [5, True, "low", "large"],
        [1, False, "high", "small"],
        [1, False, "low", "small"],
        [5, False, "high", "small"],
        [25, False, "high", "large"],
        [1, False, "medium", "small"],
    ]

    expected_prices = [
        880.0,
        420.0,
        400.0,
        840.0,
        720.0,
        400.0,
        400.0,
        400.0,
        640.0,
        400.0,
    ]

    for i, row in enumerate(parameters_data_set):
        yield [*row, expected_prices[i]]

"""Minumal positive numbers
"""
def test_calculate_smallest_number():
    assert 400 == calculate_price("small", "low", False, 1)

"""Check limit fragile and distance condition
"""
def test_raise_exception_on_fragile_over_30_km():
    with pytest.raises(exceptions.UnsupportedDeliveryParameters):
        assert 2040 == calculate_price("large", "high", True, 31)

"""Maximum positive numbers
"""
def test_calculate_largest_number():
    assert 800 == calculate_price("large", "high", False, 31)


@pytest.mark.parametrize(
    "distance, fragile, occupation, size, expected_price", data_set()
)
def test_pairwise_calculate_price(distance, fragile, occupation, size, expected_price):
    assert expected_price == calculate_price(
        distance=distance, size=size, fragile=fragile, occupation=occupation
    )
