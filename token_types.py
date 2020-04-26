from enum import Enum

class token_types(Enum):
    INTEGER = 1, "INTEGER"
    OPERATOR_PLUS = 2, "plus"
    OPERATOR_MIN  = 3, "min"
    OPERATOR_MACHT = 4, "macht"
    OPERATOR_DELEN = 5, "delen"
    OPERATOR_KEER = 6, "keer"
    OPERATOR_ASSIGN = 7, "is"
    OPERATOR_GELIJK_AAN = 8, "gelijk_aan"
    OPERATOR_KLEINER_DAN = 9, "kleiner_dan"
    OPERATOR_GROTER_DAN = 10, "groter_dan"
    ALS_STATEMENT = 11, "als_waar"
    EINDE_ALS = 12, "einde_als"
    ZOLANG_START = 13, "zolang"
    ZOLANG_EINDE = 14, "einde_zolang"
    PRINT = 15, "laat_zien"
    NAME = 100, "NAME"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.__name__ = name
        return member
