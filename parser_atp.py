from nodes import *
from operators import *
from token_class import token
from token_types import token_types
from lex import lex

def parse_tokens_to_nodes(tokens : [token]):
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
        return [einde_als_node()] + parse_tokens_to_nodes(tail)
    elif a.token_type == token_types.ZOLANG_START:
        return [zolang_node(node,a.value,0)] + parse_tokens_to_nodes(tail)
    elif a.token_type == token_types.ZOLANG_EINDE:
        return [einde_zolang(0)] + parse_tokens_to_nodes(tail)
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

def check_condition(a,b,node_type):
    if isinstance(a,node_type):
        if a.op in (op_als,):
            new_node = node_type(b,a.op,None)
            return [new_node]
    return [a,b]

def parse_condition(nodes,node_type):
    if len(nodes) <= 1:
        return nodes
    if len(nodes) == 2:
        a,b = nodes
        return check_condition(a,b,node_type)
    a, *tail = nodes
    new_lst = parse_condition(tail,node_type)
    if len(new_lst)==1:
        b = new_lst[0]
        extra = []
    else:
        b, *extra = new_lst
    return check_condition(a,b,node_type) + extra

def remove_als(nodes):
    if isinstance(nodes[0],als_node):
        return (nodes[1:],nodes[0])
    return (nodes,None)

def parse_row_tokens(tokens):
    removed_als = remove_als(parse_tokens_to_nodes(tokens))
    operator_output = parse_operators(parse_operators(parse_operators(parse_operators(removed_als[0],(op_macht,)),(op_keer,op_delen)),(op_min,op_plus)),(op_assign,op_gelijk,op_groter_dan,op_kleiner_dan))
    if removed_als[1] is not None:
        operator_output = [removed_als[1]] + operator_output
    output = parse_condition(parse_condition(operator_output,als_node),zolang_node)
    return output[0]

def find_node_backwards(nodes,node_type):
    if isinstance(nodes[len(nodes)-1],node_type):
        return 0
    else:
        return 1 + find_node_backwards(nodes[:-1],node_type)

#find zolang bij einde_zolang
def find_node_forwards(nodes,node_type):
    if isinstance(nodes[0],node_type):
        return 0 
    else:
        return 1 + find_node_forwards(nodes[1:],node_type)

def fill_condition(nodes,node_type,end_node_type):
    if len(nodes) ==1:
        return nodes
    a, *tail = nodes
    if isinstance(a,node_type):
        value = find_node_backwards(tail,end_node_type)
        einde_index = len(tail) - value
        return [node_type(a.conditie,a.op,einde_index+1)] + fill_condition(tail[:einde_index-1],node_type,end_node_type) + tail[einde_index-1:einde_index+value]
    return [a] + fill_condition(tail,node_type,end_node_type)

def fill_end_condition(nodes,node_type,end_node_type):
    if len(nodes) <=1:
        return nodes
    *head, a = nodes
    if isinstance(a,node_type):
        einde_index = (len(head) - find_node_forwards(head,end_node_type)) *-1
        return  fill_condition(head,node_type,end_node_type) +[node_type(einde_index)]
    return  fill_end_condition(head,node_type,end_node_type) + [a]


def parse_program(file_name):
    op_output = list(map(parse_row_tokens,lex(file_name)))
    als_filled = fill_condition(op_output,als_node,einde_als_node)
    zolang_filled = fill_condition(als_filled,zolang_node,einde_zolang)
    final_output = fill_end_condition(zolang_filled,einde_zolang,zolang_node)
    return final_output