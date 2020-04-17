from token_class import token
from token_types import token_types
from operators import *


def get_and_split_input(fname : str)->str:
    infile = open(fname,'r')
    input_str = infile.read()
    str_lst = input_str.split("\n")
    input_lst = []
    for item in str_lst:
        input_lst.append(item.split(" "))
    return input_lst

def get_token(input_str : str) -> token: 
    if input_str == token_types.OPERATOR_PLUS.__name__:
        return token(token_types.OPERATOR_PLUS, op_plus)
    elif input_str == token_types.OPERATOR_MIN.__name__:
        return token(token_types.OPERATOR_MIN, op_min)
    elif input_str == token_types.OPERATOR_MACHT.__name__:
        return token(token_types.OPERATOR_MACHT, op_macht)
    elif input_str == token_types.OPERATOR_DELEN.__name__:
        return token(token_types.OPERATOR_DELEN, op_delen)
    elif input_str == token_types.OPERATOR_KEER.__name__:
        return token(token_types.OPERATOR_KEER, op_keer)
    elif any(map(str.isdigit,input_str)):
        return token(token_types.INTEGER, int(input_str))

def lex(fname : str) -> [token]:
    input_lst = get_and_split_input(fname)
    return list(map(lambda row: list(map(get_token,row)),input_lst))

def print_lex_output(tokens:[[token]]):
    for row in range(len(tokens)):
        print("row:",row)
        for token in tokens[row]:
            print(token)