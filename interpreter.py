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


def parse_operator_tokens(tokens,index):
    if index < 0:
        return []
    if tokens[index].token_type in (token_types.OPERATOR_DELEN, token_types.OPERATOR_KEER, token_types.OPERATOR_MIN, token_types.OPERATOR_PLUS, token_types.OPERATOR_MACHT):
        return [op_node(node,tokens[index].value,node)] + parse_operator_tokens(tokens,index-1) 
    elif tokens[index].token_type == token_types.INTEGER:
        return [int_node(tokens[index])] + parse_operator_tokens(tokens,index-1) 
    return parse_operator_tokens(tokens,index-1)

def parse_operators(nodes, operators, index):
    if index  < 0:
        return nodes
    elif isinstance(nodes[index],op_node):
        if nodes[index].op in operators:
            new_node = op_node(nodes.pop(index+1),nodes.pop(index).op,nodes[index-1])
            nodes[index-1] = new_node
            return  parse_operators(nodes, operators, index-2)
    return parse_operators(nodes, operators, index-1)

def parse_row_tokens(tokens):
    numbers_operators = parse_operator_tokens(tokens,len(tokens)-1)
    power_lst = parse_operators(numbers_operators,(op_macht,),len(numbers_operators)-1)
    mul_dev_lst = parse_operators(power_lst,(op_keer,op_delen),len(power_lst)-1)
    output = parse_operators(mul_dev_lst,(op_min,op_plus),len(mul_dev_lst)-1)
    # for i in power_lst:
    #     print(i)
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