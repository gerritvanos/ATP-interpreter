from lex import lex, print_lex_output
from token_class import token
from nodes import *
from operators import *
from token_types import token_types
from parser_atp import parse_program
from typing import List,Union
from program_state import program_state
from time import time
import sys
import threading

sys.setrecursionlimit(0x100000)
def visit(node : node,program_state : program_state) -> Union[program_state,int]:
    if isinstance(node,op_node):
        if node.op == op_assign:
            return node.op(node.lhs.name,visit(node.rhs,program_state),program_state)
        return node.op(visit(node.lhs,program_state),visit(node.rhs,program_state))
    if isinstance(node,als_node) or isinstance(node,zolang_node):
        return update_row_number(node.op(visit(node.conditie,program_state),node.eind_locatie),program_state)
    if isinstance(node,einde_zolang):
        return update_row_number(node.terug_locatie,program_state)
    if isinstance(node,einde_als_node):
        return update_row_number(1,program_state)
    if isinstance(node,int_node):
        return node.value 
    if isinstance(node,name_node):
        return program_state.variables[node.name]
    print("yolo")

def run_program(program : List[node],program_state : program_state) -> program_state:
    if program_state.row_number >= len(program):
        print("finished")
        return program_state
    print(program_state)
    return run_program(program,visit(program[program_state.row_number],program_state))
 
#should be container
start_time = time()
start_state = program_state(0,{})
output = run_program(parse_program("test.txt"),start_state)
print(output)
print("time to run program: ",time()-start_time)