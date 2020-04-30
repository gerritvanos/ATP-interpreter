from typing import Callable
from token_class import token

class node():
    pass

class op_node(node):
    def __init__(self,lhs : node, op : Callable, rhs : node):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
    def __str__(self) -> str:
        return "{{lhs: {}, op: {}, rhs: {}}}".format(self.lhs,self.op.__name__,self.rhs)
    def __repr__(self) -> str:
        return self.__str__()

class int_node(node):
    def __init__(self, token : token):
        self.__token = token
        self.value = token.value
    def __str__(self) -> str:
        return "{}:{}".format(self.__token.token_type.name, self.value)
    def __repr__(self) -> str:
        return self.__str__()

class name_node(node):
    def __init__(self, token : token):
        self.__token = token
        self.name = token.value
    def __str__(self) -> str:
        return "{}:{}".format(self.__token.token_type.name, self.name)
    def __repr__(self) -> str:
        return self.__str__()

class als_node(node):
    def __init__(self,conditie : node, op : Callable, eind_locatie : int):
        self.conditie = conditie
        self.op = op
        self.eind_locatie = eind_locatie
    def __str__(self) -> str:
        return "{{als: conditie: {} : einde_als: {}}}".format(self.conditie, self.eind_locatie)
    def __repr__(self) -> str:
        return self.__str__()

class einde_als_node(node):
    def __init__(self):
        pass
    def __str__(self) -> str:
        return "{einde_als_node}"
    def __repr__(self) -> str:
        return self.__str__()

class zolang_node(node):
    def __init__(self, conditie : node, op : Callable, eind_locatie : int):
        self.conditie = conditie
        self.op = op
        self.eind_locatie = eind_locatie
    def __str__(self) -> str:
        return "{{zolang: conditie: {} : einde zolang: {}}}".format(self.conditie, self.eind_locatie)
    def __repr__(self) -> str:
        return self.__str__()


class einde_zolang(node):
    def __init__(self, hoeveelheid_regels_terug : int):
        self.hoeveelheid_regels_terug = hoeveelheid_regels_terug
    def __str__(self) -> str:
        return "{{einde_zolang: hoeveelheid_regels_terug = {}}}".format(self.hoeveelheid_regels_terug)
    def __repr__(self) -> str:
        return self.__str__()

class print_node(node):
    def __init__(self,to_print,op):
        self.to_print = to_print
        self.op = op
    def __str__(self):
        return "{{print: {}}}".format(self.to_print)
    def __repr__(Self):
        return self.__str__()

single_sided_nodes = (zolang_node,als_node,print_node)
