from copy import copy
from program_state import program_state

#basic mathematical  operators
def op_plus(a : int,b : int) -> int:
    return a + b

def op_min(a : int,b : int) -> int:
    return a - b

def op_macht(a : int,b : int) -> int:
    return a ** b

def op_keer(a : int,b : int) -> int:
    return a * b

def op_delen(a : int,b : int) -> int:
    return a / b

#rational operators
def op_gelijk(a : int,b :int) -> int:
    return int(a == b)

def op_groter_dan(a : int,b : int) -> int:
    return int(a > b)

def op_kleiner_dan(a : int,b : int) -> int:
    return int(a < b)

#operators to modify program state and check ifs
def op_als(conditie : int, aantal_regels : int) -> int:
    if conditie:
        return 1
    return aantal_regels

def op_assign(name : str, value : int, program_state : program_state) -> program_state:
    output = copy(program_state)
    to_add = {name:value}
    output.variables.update(to_add)
    output.row_number +=1
    return output

def update_row_number(aantal_regels : int, program_state : program_state) -> program_state:
    output = copy(program_state)
    output.row_number += aantal_regels
    return output

def op_print(to_print,program_state):
    output = copy(program_state)
    output.row_number +=1
    print(to_print)
    return output

op_precedence1 = (op_macht,)
op_precedence2 = (op_keer,op_delen)
op_precedence3 = (op_min,op_plus)
op_precedence4 = (op_assign,op_gelijk,op_groter_dan,op_kleiner_dan)