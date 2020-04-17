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
        print(self.__str__())

class int_node(node):
    def __init__(self,token):
        self.__token = token
        self.value = token.value
    def __str__(self):
        return "{}:{}".format(self.__token.token_type.name, self.value)
    def __repr__(self):
        print(self.__str__())