from nodes import *
from operators import *
from token_class import token
from token_types import token_types
from lex import lex

def parse_tokens_to_nodes(tokens):
    if len(tokens) == 0:
        return []
    a, *tail = tokens
    if a.token_type in (token_types.OPERATOR_DELEN, token_types.OPERATOR_KEER, token_types.OPERATOR_MIN, token_types.OPERATOR_PLUS, token_types.OPERATOR_MACHT, token_types.OPERATOR_ASSIGN, token_types.OPERATOR_GELIJK_AAN, token_types.OPERATOR_GROTER_DAN, token_types.OPERATOR_KLEINER_DAN):
        return [op_node(node,a.value,node)] + parse_tokens_to_nodes(tail) 
    if a.token_type in (token_types.ALS_STATEMENT,):
        return [als_node(node,a.value,0)] + parse_tokens_to_nodes(tail) 
    elif a.token_type == token_types.INTEGER:
        return [int_node(a)] + parse_tokens_to_nodes(tail) 
    elif a.token_type == token_types.EINDE_ALS:
        return [einde_als_node(0)] + parse_tokens_to_nodes(tail)
    elif a.token_type == token_types.NAME:
        return [name_node(a)] + parse_tokens_to_nodes(tail)
    return parse_tokens_to_nodes(tail)

def check_operator(a,b,c, operators):
    if isinstance(b,op_node):
        if b.op in operators:
            new_node = op_node(a,b.op,c)
            return [new_node]
    return [a,b,c]

def parse_operators(nodes : list, operators : tuple):
    if len(nodes) < 3:
        return nodes
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

def check_als(a,b):
    if isinstance(a,als_node):
        if a.op in (op_als,):
            new_node = als_node(b,a.op,None)
            return [new_node]
    return [a,b]

def parse_als(nodes):
    if len(nodes) <= 1:
        return nodes
    if len(nodes) == 2:
        a,b = nodes
        return check_als(a,b)
    a, *tail = nodes
    new_lst = parse_als(tail)
    if len(new_lst)==1:
        b = new_lst[0]
        extra = []
    else:
        b, *extra = new_lst
    return check_als(a,b) + extra


def parse_row_tokens(tokens):
    numbers_operators = parse_tokens_to_nodes(tokens)
    power_lst = parse_operators(numbers_operators,(op_macht,))
    mul_dev_lst = parse_operators(power_lst,(op_keer,op_delen))
    plus_min_lst = parse_operators(mul_dev_lst,(op_min,op_plus))
    operator_output = parse_operators(plus_min_lst,(op_assign,op_gelijk,op_groter_dan,op_kleiner_dan))
    output = parse_als(operator_output)
    return output[0]

def find_einde_als(nodes):
    if isinstance(nodes[len(nodes)-1],einde_als_node):
        return 0
    else:
        return 1 + find_einde_als(nodes[:-1])

def fill_als(nodes):
    if len(nodes) <=1:
        return [nodes]
    a, *tail = nodes
    if isinstance(a,als_node):
        einde_index = len(tail) - find_einde_als(tail)
        return [als_node(a.conditie,a.op,einde_index)] + fill_als(tail[:-1]) + tail[einde_index:]
    return [a] + fill_als(tail)

def parse_program(file_name):
    return fill_als(list(map(parse_row_tokens,lex(file_name))))