class program_state:
    def __init__(self,row_number,variables):
        self.variables = variables
        self.row_number = row_number
    def __str__(self):
        return "variables: {} \nrow_number: {}".format(self.variables,self.row_number)