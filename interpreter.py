from lex import lex, print_lex_output
from token_class import token
from nodes import *
from operators import *
from token_types import token_types
from parser_atp import parse_program

global_program_state = {}
row_number = 0
def visit(node : node) -> int:
    global global_program_state
    global row_number
    if isinstance(node,op_node):
        if node.op == op_assign:
            global_program_state = node.op(node.lhs.name,visit(node.rhs),global_program_state)
            return None
        return node.op(visit(node.lhs),visit(node.rhs))
    if isinstance(node,als_node) or isinstance(node,zolang_node):
        row_number += node.op(visit(node.conditie),node.eind_locatie)
    if isinstance(node,einde_zolang):
        row_number -= node.terug_locatie
    if isinstance(node,int_node):
        return node.value
    if isinstance(node,name_node):
        return global_program_state[node.name]


output = parse_program("test.txt")

while(row_number < len(output)):
    prev_row = row_number
    visit(output[row_number])
    if prev_row == row_number:
        row_number +=1
    print(global_program_state)

print(global_program_state)