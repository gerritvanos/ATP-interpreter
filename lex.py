from token_class import token
from token_types import token_types
from operators import *
from typing import List

def get_and_split_input(fname : str)->List[List[str]]:
    infile = open(fname,'r')
    input_str = infile.read()
    str_lst = input_str.split("\n")
    str_lst = list(filter(None,str_lst))
    return list(map(str.split,list(map(str.strip,str_lst))))

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
    elif input_str == token_types.OPERATOR_ASSIGN.__name__:
        return token(token_types.OPERATOR_ASSIGN,op_assign)
    elif input_str == token_types.OPERATOR_GELIJK_AAN.__name__:
        return token(token_types.OPERATOR_GELIJK_AAN,op_gelijk)
    elif input_str == token_types.OPERATOR_KLEINER_DAN.__name__:
        return token(token_types.OPERATOR_KLEINER_DAN,op_kleiner_dan)
    elif input_str == token_types.OPERATOR_GROTER_DAN.__name__:
        return token(token_types.OPERATOR_GROTER_DAN,op_groter_dan)
    elif input_str == token_types.ALS_STATEMENT.__name__:
        return token(token_types.ALS_STATEMENT,op_als)
    elif input_str == token_types.EINDE_ALS.__name__:
        return token(token_types.EINDE_ALS,"einde")
    elif input_str == token_types.ZOLANG_START.__name__:
        return token(token_types.ZOLANG_START,op_als)
    elif input_str == token_types.ZOLANG_EINDE.__name__:
        return token(token_types.ZOLANG_EINDE,"einde")
    elif all(map(str.isdigit,input_str)):
        return token(token_types.INTEGER, int(input_str))
    else:
        return token(token_types.NAME,input_str)

def lex(fname : str) -> List[List[token]]:
    input_lst = get_and_split_input(fname)
    return list(map(lambda row: list(map(get_token,row)),input_lst))

def print_lex_output(tokens:List[List[token]]):
    for row in range(len(tokens)):
        print("row:",row)
        for token in tokens[row]:
            print(token)