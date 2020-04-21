def op_plus(a : int,b : int):
    return a + b

def op_min(a : int,b : int):
    return a - b

def op_macht(a : int,b : int):
    return a ** b

def op_keer(a : int,b : int):
    return a * b

def op_delen(a : int,b : int):
    return a / b

def op_gelijk(a : int,b :int) -> int:
    return int(a == b)

def op_groter_dan(a : int,b : int) -> int:
    return int(a > b)

def op_kleiner_dan(a : int,b : int) -> int:
    return int(a < b)

def op_als(conditie, aantal_regels):
    if conditie:
        return 1
    return aantal_regels

def op_assign(name,value,program_state):
    output = program_state.copy()
    to_append = {name:value, "row_number":program_state["row_number"] + 1}
    output.update(to_append)
    return output

def update_row_number(aantal_regels,program_state):
    output = program_state.copy()
    to_change = {"row_number":program_state["row_number"] + aantal_regels}
    output.update(to_change)
    return output