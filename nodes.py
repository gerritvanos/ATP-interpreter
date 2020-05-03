from typing import Callable
from token_class import token

"""
This file contains all the nodes used in the AST all nodes are derived from the node class
"""
class node():
    pass

#operator node used to store lhs,rhs and the opperator
class op_node(node):
    def __init__(self,lhs : node, op : Callable, rhs : node):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
    def __str__(self) -> str:
        return "{{lhs: {}, op: {}, rhs: {}}}".format(self.lhs,self.op.__name__,self.rhs)
    def __repr__(self) -> str:
        return self.__str__()

#getal node used to store a integer value
class getal_node(node):
    def __init__(self, token : token):
        self.__token = token
        self.value = token.value
    def __str__(self) -> str:
        return "{}:{}".format(self.__token.token_type.name, self.value)
    def __repr__(self) -> str:
        return self.__str__()

#name node(used to store variable names)
class name_node(node):
    def __init__(self, token : token):
        self.__token = token
        self.name = token.value
    def __str__(self) -> str:
        return "{}:{}".format(self.__token.token_type.name, self.name)
    def __repr__(self) -> str:
        return self.__str__()

#als(if) node used to signal the start of a condition
class als_node(node):
    def __init__(self,conditie : node, op : Callable, eind_locatie : int):
        self.conditie = conditie
        self.op = op
        self.eind_locatie = eind_locatie
    def __str__(self) -> str:
        return "{{als: conditie: {} : einde_als: {}}}".format(self.conditie, self.eind_locatie)
    def __repr__(self) -> str:
        return self.__str__()

#einde als node used to signal the end of a condition
class einde_als_node(node):
    def __init__(self):
        pass
    def __str__(self) -> str:
        return "{einde_als_node}"
    def __repr__(self) -> str:
        return self.__str__()

#zolang(while) node used to signal the start of a loop
class zolang_node(node):
    def __init__(self, conditie : node, op : Callable, eind_locatie : int):
        self.conditie = conditie
        self.op = op
        self.eind_locatie = eind_locatie
    def __str__(self) -> str:
        return "{{zolang: conditie: {} : einde zolang: {}}}".format(self.conditie, self.eind_locatie)
    def __repr__(self) -> str:
        return self.__str__()

#einde zolang node used to signal the end of a loop
class einde_zolang(node):
    def __init__(self, hoeveelheid_regels_terug : int):
        self.hoeveelheid_regels_terug = hoeveelheid_regels_terug
    def __str__(self) -> str:
        return "{{einde_zolang: hoeveelheid_regels_terug = {}}}".format(self.hoeveelheid_regels_terug)
    def __repr__(self) -> str:
        return self.__str__()

#print node used for printing variables and or expressions
class print_node(node):
    def __init__(self,to_print : node,op : Callable):
        self.to_print = to_print
        self.op = op
    def __str__(self):
        return "{{print: {}}}".format(self.to_print)
    def __repr__(Self):
        return self.__str__()

#tuple to store all single sided nodes this makes it easy to check if the node is single sided
single_sided_nodes = (print_node,zolang_node,als_node)