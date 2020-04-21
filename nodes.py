class node():
    pass

class op_node(node):
    def __init__(self,lhs,op,rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
    def __str__(self):
        return "[lhs: {}, op: {}, rhs: {}]".format(self.lhs,self.op.__name__,self.rhs)
    def __repr__(self):
        return self.__str__()

class int_node(node):
    def __init__(self,token):
        self.__token = token
        self.value = token.value
    def __str__(self):
        return "{}:{}".format(self.__token.token_type.name, self.value)
    def __repr__(self):
        return self.__str__()

class name_node(node):
    def __init__(self,token):
        self.__token = token
        self.name = token.value
    def __str__(self):
        return "{}:{}".format(self.__token.token_type.name, self.name)
    def __repr__(self):
        return self.__str__()

class als_node(node):
    def __init__(self,conditie,op,eind_locatie):
        self.conditie = conditie
        self.op = op
        self.eind_locatie = eind_locatie
    def __str__(self):
        return "als = conditie: {} : einde_als: {}".format(self.conditie, self.eind_locatie)
    def __repr__(self):
        return self.__str__()

class einde_als_node(node):
    def __init__(self):
        pass
    def __str__(self):
        return "einde_als_node"
    def __repr__(self):
        return self.__str__()

class zolang_node(node):
    def __init__(self,conditie, op, eind_locatie):
        self.conditie = conditie
        self.op = op
        self.eind_locatie = eind_locatie
    def __str__(self):
        return "zolang = conditie: {} : einde zolang: {}".format(self.conditie, self.eind_locatie)
    def __repr__(self):
        return self.__str__()


class einde_zolang(node):
    def __init__(self,terug_locatie):
        self.terug_locatie = terug_locatie
    def __str__(self):
        return "einde_zolang: terugspring regel = {}".format(self.terug_locatie)
    def __repr__(self):
        return self.__str__()
    


