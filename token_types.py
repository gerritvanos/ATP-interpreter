from enum import Enum

class token_types(Enum):
    INTEGER = 1, "INTEGER"
    OPERATOR_PLUS = 2, "plus"
    OPERATOR_MIN  = 3, "min"
    OPERATOR_MACHT = 4, "macht"
    OPERATOR_DELEN = 5, "delen"
    OPERATOR_KEER = 6, "keer"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.__name__ = name
        return member
