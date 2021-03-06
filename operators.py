from copy import copy
from program_state import program_state
from typing import Union

#basic mathematical operators for floats and ints
def op_plus(a : Union[int,float],b : Union[int,float]) -> Union[int,float]:
    return a + b

def op_min(a : Union[int,float],b : Union[int,float]) -> Union[int,float]:
    return a - b

def op_macht(a : Union[int,float],b : Union[int,float]) -> Union[int,float]:
    return a ** b

def op_keer(a : Union[int,float],b : Union[int,float]) -> Union[int,float]:
    return a * b

def op_delen(a : Union[int,float],b : Union[int,float]) -> Union[int,float]:
    return a / b

#rational operators
def op_gelijk(a : Union[int,float],b :Union[int,float]) -> int:
    return int(a == b)

def op_groter_dan(a : Union[int,float],b : Union[int,float]) -> int:
    return int(a > b)

def op_kleiner_dan(a : Union[int,float],b : Union[int,float]) -> int:
    return int(a < b)

def op_groter_gelijk(a : Union[int,float],b : Union[int,float]) -> int:
    return int(a >= b)

def op_kleiner_gelijk(a : Union[int,float],b : Union[int,float]) -> int:
    return int(a <= b)

def op_niet_gelijk(a : Union[int,float],b : Union[int,float]) -> int:
    return int(a != b)

#operators to modify program state and check ifs
def op_als(conditie : Union[int,float], aantal_regels : int) -> int:
    """
    operator to check if condition and return 1(go to next row) or the amount of rows to skip
    """
    if conditie:
        return 1
    return aantal_regels

def op_assign(name : str, value : Union[int,float], program_state : program_state) -> program_state:
    """
    operator to assign a value to a certain variable. and return a new program state(with row number increased by one)
    """
    output = copy(program_state)
    to_add = {name:value}
    output.variables.update(to_add)
    output.row_number +=1
    return output

def update_row_number(aantal_regels : int, program_state : program_state) -> program_state:
    """
    operator to increase row number based on aantal_regels
    """
    output = copy(program_state)
    output.row_number += aantal_regels
    return output

def op_print(to_print : Union[int,float], program_state : program_state) -> program_state:
    """
    operator to print the to_print part" and increase row number by one
    """
    output = copy(program_state)
    output.row_number +=1
    print(to_print)
    return output

op_precedence1 = (op_macht,)
op_precedence2 = (op_keer,op_delen)
op_precedence3 = (op_min,op_plus)
op_precedence4 = (op_assign,op_gelijk,op_groter_dan,op_kleiner_dan,\
                  op_groter_gelijk, op_kleiner_gelijk, op_niet_gelijk)
all_op = op_precedence1 + op_precedence2 + op_precedence3 + op_precedence4