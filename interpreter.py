from lex import lex, print_lex_output
from nodes import *
from token_class import token
from token_types import token_types
from operators import *

def visit_int_node(node : node) -> int:
    return node.value

def visit(node : node) -> int:
    if isinstance(node,op_node):
        return node.op(visit(node.lhs),visit(node.rhs))
    if isinstance(node,int_node):
        return node.value

tokens = lex("test.txt")
print_lex_output(tokens)


def parse_operator_tokens(tokens):
    if len(tokens) == 0:
        return []
    a, *tail = tokens
    if a.token_type in (token_types.OPERATOR_DELEN, token_types.OPERATOR_KEER, token_types.OPERATOR_MIN, token_types.OPERATOR_PLUS, token_types.OPERATOR_MACHT):
        return [op_node(node,a.value,node)] + parse_operator_tokens(tail) 
    elif a.token_type == token_types.INTEGER:
        return [int_node(a)] + parse_operator_tokens(tail) 
    return parse_operator_tokens(tail)
#

def check_operator(a,b,c, operators):
    if isinstance(b,op_node):
        if b.op in operators:
            new_node = op_node(a,b.op,c)
            return [new_node]
    return [a,b,c]

def parse_operators(nodes : list, operators : tuple):
    if len(nodes) == 3:
        a,b,c = nodes
        return check_operator(a,b,c,operators)
    a, b, *tail = nodes
    new_lst = parse_operators(tail,operators)
    if len(new_lst) == 1:
        c = new_lst[0]
        extra =[]
    else:
        c , *extra = new_lst
    return check_operator(a,b,c,operators) + extra

def parse_row_tokens(tokens):
    numbers_operators = parse_operator_tokens(tokens)
    power_lst = parse_operators(numbers_operators,(op_macht,))
    mul_dev_lst = parse_operators(power_lst,(op_keer,op_delen))
    output = parse_operators(mul_dev_lst,(op_min,op_plus))
    return output[0]


print(visit(parse_row_tokens(tokens[1])))
#boom
# node1 = int_node(tokens[1][0])
# node2 = int_node(tokens[1][2])
# node3 = int_node(tokens[1][4])
# node4 = int_node(tokens[1][6])
# onode1 = op_node(node2,tokens[1][3].value,node3)
# onode3 = op_node(node1,tokens[1][1].value,onode1)
# onode2 = op_node(onode3,tokens[1][5].value, node4)