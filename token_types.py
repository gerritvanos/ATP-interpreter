from enum import Enum
from operators import *
class token_types(Enum):
    OPERATOR_PLUS = op_plus, "plus"
    OPERATOR_MIN  = op_min, "min"
    OPERATOR_MACHT = op_macht, "macht"
    OPERATOR_DELEN = op_delen, "delen_door"
    OPERATOR_KEER = op_keer, "keer"
    OPERATOR_ASSIGN = op_assign, "wordt"
    OPERATOR_GELIJK_AAN = op_gelijk, "gelijk_aan"
    OPERATOR_KLEINER_DAN = op_kleiner_dan, "kleiner_dan"
    OPERATOR_GROTER_DAN = op_groter_dan, "groter_dan"
    OPERATOR_GROTER_GELIJK = op_groter_gelijk, "groter_gelijk"
    OPERATOR_KLEINER_GELIJK = op_kleiner_gelijk, "kleiner_gelijk"
    OPERATOR_NIET_GELIJK = op_niet_gelijk, "anders_dan"
    ALS_STATEMENT = 11, "als_waar"
    EINDE_ALS = 12, "einde_als"
    ZOLANG_START = 13, "zolang"
    ZOLANG_EINDE = 14, "einde_zolang"
    PRINT = 15, "laat_zien"
    NAME = 16, "NAME"
    STR = 17, "STR"
    GETAL = 18, "GETAL"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.__name__ = name
        return member

#tuple with strings used to check if input string is operator
token_operator_strings = tuple(filter(None, list(map(lambda t: t.__name__ if t.value in all_op else None, token_types))))
#tuple with all operator token types
token_operator_types   = tuple(filter(None, list(map(lambda t: t if t.value in all_op else None, token_types))))