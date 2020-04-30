class token():
    def __init__(self,token_type,value):
        self.token_type = token_type
        self.value = value
    def __str__(self):
        return "(type: {} , value: {})".format(self.token_type.name ,self.value)
    def __repr__(self):
        return self.__str__()