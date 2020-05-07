"""
class to store the program_state which consists of a dictonary with the variables and the current row number
"""
class program_state:
    def __init__(self,row_number,variables):
        self.variables = variables
        self.row_number = row_number
    def __str__(self) -> str:
        return "program_state:\n  variables: {} \n  row_number: {}".format(self.variables,self.row_number)
    def __repr__(self) -> str:
        return self.__str__()