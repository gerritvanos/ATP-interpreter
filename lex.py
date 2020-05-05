from token_class import token
from token_types import token_types
from operators import *
from typing import List, Callable
import shlex

def get_and_split_input(fname : str)->List[List[str]]:
    """
    function to read in the given file and split it by line and whitespace
    also remove extranius whitespaces
    """
    infile = open(fname,'r')
    input_str = infile.read()
    str_lst = input_str.splitlines()
    str_lst = list(filter(None,str_lst))
    return list(map(split_without_substr,list(map(str.strip,str_lst))))

def split_without_substr(in_str : str) -> List[str]:
    """
    function to split line on spaces except when within ""
    note: only works if one "" pair is used per rule
    """
    if "\"" in in_str:
        quote_index = in_str.find("\"")
        return in_str[:quote_index].split() + [in_str[quote_index:]]
    return in_str.split()

def get_token(input_str : str) -> token: 
    """
    get token based on string by comparing it to all token types 
    if no token type is found name token is constructed because if the string is no keyword it must be a variable name
    """
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
        return token(token_types.EINDE_ALS,"einde_als")
    elif input_str == token_types.ZOLANG_START.__name__:
        return token(token_types.ZOLANG_START,op_als)
    elif input_str == token_types.ZOLANG_EINDE.__name__:
        return token(token_types.ZOLANG_EINDE,"einde_zolang")
    elif input_str == token_types.PRINT.__name__:
        return token(token_types.PRINT,op_print)
    elif all(map(str.isdigit,input_str)) or (input_str[0] == '-' and all(map(str.isdigit,input_str[1:]))): #plus getal or min getal
        return token(token_types.GETAL, int(input_str))
    elif input_str.replace('.','',1).isdigit(): #floats
        return token(token_types.GETAL,float(input_str))
    elif input_str[0] == "\"":
        return token(token_types.STR,input_str.strip("\""))
    else:
        return token(token_types.NAME,input_str)

def lex(fname : str) -> List[List[token]]:
    """
    function to get the tokens for each line of the input file
    """
    return list(map(lambda row: list(map(get_token,row)),get_and_split_input(fname)))

def verbose_lex(f : Callable):
    """
    decorator to function lex for printing a bit more information
    """
    def inner(file_name : str):
        print("start lexing of program located in {}".format(file_name))
        print("lexer output")
        tokens = f(file_name)
        for row in range(len(tokens)):
            print("regel:",row+1)
            for token in tokens[row]:
                print(token)
        print("\n")
        return tokens
    return inner