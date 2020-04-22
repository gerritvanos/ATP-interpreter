from lex import lex, print_lex_output
from token_class import token
from nodes import *
from operators import *
from token_types import token_types
from parser_atp import parse_program
from typing import List

def visit(node : node,program_state : dict) -> dict:
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
        return program_state[node.name]

def run_program(program : List[node],program_state : dict) -> dict:
    if program_state["row_number"] >= len(program):
        return program_state
    return run_program(program,visit(program[program_state["row_number"]],program_state))
 
start_state =  {"row_number":0}
print(run_program(parse_program("test.txt"),start_state))