class WrongValue(Exception):
    def __str__(self):
        return f"Wrong value for {self.__class__}"


class WrongSizeValue(WrongValue): ...


class WrongOccupationValue(WrongValue): ...


class WrongFragileValue(WrongValue): ...


class WrongDistanceValue(WrongValue): ...


class UnsupportedDeliveryParameters(WrongValue): ...
