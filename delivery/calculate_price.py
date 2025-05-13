import typing
import enum

from delivery import exceptions

SIZE_TYPE = typing.Literal["large", "small"]
OCCUPATION_TYPE = typing.Literal["high", "medium", "low"]
FRAGILE_TYPE: typing.TypeAlias = bool
DISTANCE_TYPE: typing.TypeAlias = int | float


class Occupation(enum.StrEnum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Size(enum.StrEnum):
    LARGE = "large"
    SMALL = "small"


DISTANCE_ADDED_VALUES = {(0, 2): 50, (2, 10): 100, (10, 30): 200, (30, 10000): 300}


OCCUPATION_MULTIPLIER = {
    Occupation.HIGH: 1.6,
    Occupation.MEDIUM: 1.4,
    Occupation.LOW: 1.2,
}

SIZE_ADDED_VALUE = {Size.LARGE: 200, Size.SMALL: 100}

FRAGILE_ADDED_VALUE = {True: 300, False: 0}


def calculate_price(
    size: SIZE_TYPE,
    occupation: OCCUPATION_TYPE | None,
    fragile: FRAGILE_TYPE,
    distance: DISTANCE_TYPE,
) -> float:
    """ Validate input parameters and calculate delivery """
    validate_input_data(size, occupation, fragile, distance)
    total_cost = 0
    total_cost += get_size_added_value(size)
    total_cost += get_fragile_added_value(fragile)
    total_cost += get_distance_added_value(distance)
    total_cost *= get_occupation_multiplier(occupation)
    return total_cost if total_cost > 400 else 400


def validate_input_data(
    size: SIZE_TYPE,
    occupation: OCCUPATION_TYPE | None,
    fragile: FRAGILE_TYPE,
    distance: DISTANCE_TYPE,
):
    if not isinstance(fragile, FRAGILE_TYPE):
        raise exceptions.WrongFragileValue(f"Invalid value {fragile}")

    if type(distance) not in [int, float] or distance <= 0:
        raise exceptions.WrongDistanceValue(f"Wrong value for distance {distance}")

    if distance > 30 and fragile:
        raise exceptions.UnsupportedDeliveryParameters(f"Impossible to transport fragile over 30 km")

    if occupation and occupation not in OCCUPATION_MULTIPLIER.keys():
        raise exceptions.WrongOccupationValue(
            f"Wrong value for occumpation {occupation}"
        )

    if size not in SIZE_ADDED_VALUE.keys():
        raise exceptions.WrongSizeValue(f"Box size is wrong: {size}")


def get_occupation_multiplier(occupation: OCCUPATION_TYPE | None) -> float:
    if occupation is None:
        return 1
    return OCCUPATION_MULTIPLIER[Occupation(occupation)]


def get_size_added_value(size: SIZE_TYPE) -> int:
    return SIZE_ADDED_VALUE[Size(size)]


def get_fragile_added_value(fragile: FRAGILE_TYPE = False) -> int:
    return FRAGILE_ADDED_VALUE[fragile]


def get_distance_added_value(distance: DISTANCE_TYPE) -> int:
    for interval in DISTANCE_ADDED_VALUES.keys():
        if interval[0] < distance < interval[1]:
            return DISTANCE_ADDED_VALUES[interval]
    else:
        return DISTANCE_ADDED_VALUES[(30, 10000)]
