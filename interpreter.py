from lex import lex, verbose_lex
from token_class import token
from nodes import *
from operators import *
from token_types import token_types
from parser_atp import parse_program, verbose_parse_program
from typing import List,Union
from program_state import program_state
from time import time
import sys
from os import path
import threading
import platform
import argparse

def visit(node : node,program_state : program_state) -> Union[program_state,Union[int,float]]:
    """
    This function "visits" a node of the ast, depending on the node type it is called again to visit its childs.
    After all childs have been visited the operator(that belongs to the node) is called and returns a program state.
    This function returns a number(float or int) if a getal_node or name_node is visited otherwise a program_state.
    """
    if isinstance(node,op_node):
        if node.op == op_assign:
            return node.op(node.lhs.name,visit(node.rhs,program_state),program_state)
        return node.op(visit(node.lhs,program_state),visit(node.rhs,program_state))
    if isinstance(node,(als_node,zolang_node)):
        return update_row_number(node.op(visit(node.conditie,program_state),node.eind_locatie),program_state)
    if isinstance(node,print_node):
        return node.op(visit(node.to_print,program_state),program_state)
    if isinstance(node,einde_zolang):
        return update_row_number(node.hoeveelheid_regels_terug,program_state)
    if isinstance(node,einde_als_node):
        return update_row_number(1,program_state)
    if isinstance(node,getal_node):
        return node.value 
    if isinstance(node,name_node):
        return program_state.variables[node.name]

def set_stack_recursion():
    """
    Function that sets recusion limit to 0x1000000 and increases stacksize based on OS
    """
    sys.setrecursionlimit(0x1000000)
    if platform.system() == "Linux":
        print("running on linux stack size: 2gb\n")
        threading.stack_size(2147483648) #set stack to 2gb
    else:
        print("running on windows stack size: 256mb\n")
        threading.stack_size(256000000)

def main():
    """
    Main function called if script starts, procceses arguments and starts interpreter
    """
    global parse_program
    global lex
    parser = argparse.ArgumentParser(description="interpreter for gerrit-- programming language")
    parser.add_argument("file_name", type=str, metavar='File name', help="the file name that needs to be interpreted")
    parser.add_argument('-v', dest='verbose-all', action='store_true',default=False, help="run with verbose lexing and parsing")
    parser.add_argument('-l', dest='verbose-lex', action='store_true',default=False, help="run with verbose lexing")
    parser.add_argument('-p', dest='verbose-parse', action='store_true',default=False, help="run with verbose parsing")
    parser.add_argument('-s', dest='statistic', action='store_true',default=False, help="time statistics")
    arguments = vars(parser.parse_args())

    set_stack_recursion()
    #check if file exists
    if (not path.exists(arguments['file_name'])):
        print("no file at specified path: {}".format(arguments["file_name"]))
        return
    
    #use decorated functions based on verbose flags
    if (arguments['verbose-all'] == True or arguments['verbose-parse'] == True):
        parse_program = verbose_parse_program(parse_program)
    if (arguments['verbose-all'] == True or arguments['verbose-lex'] == True):
        lex = verbose_lex(lex)
    if (arguments['statistic'] == True):
        start_time = time()
    
    lex_out = lex(arguments['file_name'])
    program = parse_program(lex_out)

    print("program output:")
    t = threading.Thread(target=run(program))
    t.start()
    t.join()

    if(arguments['statistic']==True):
        print("time to run program: {} seconds".format(round(time()-start_time,4)))

class run:
    def __init__(self,program):
        self._program = program
    def __call__(self):
        self.run_program(self._program,program_state(0,{}))

    def run_program(self,program : List[node],program_state : program_state) -> program_state:
        """
        function to run the program, stops if the row number is increased beyond the program size.
        """
        if program_state.row_number >= len(program):
            print("\nfinished running program\nprogram state at the end of program:")
            print(program_state,"\n")
            return program_state
        return self.run_program(program,visit(program[program_state.row_number],program_state))

if __name__ == "__main__":
    main()