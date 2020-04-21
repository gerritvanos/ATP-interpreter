from token_types import token_types

print(token_types.OPERATOR_PLUS)
def get_and_split_input_old(fname : str)->str:
    infile = open(fname,'r')
    input_str = infile.read()
    str_lst = input_str.split("\n")
    for row in str_lst:
        if row.strip() == '':
            str_lst.remove(row)
    input_lst = []
    for item in str_lst:
        input_lst.append(item.strip().split(" "))
    return input_lst

def get_and_split_input(fname : str)->str:
    infile = open(fname,'r')
    input_str = infile.read()
    str_lst = input_str.split("\n")
    str_lst = list(filter(None,str_lst))
    return list(map(str.split,list(map(str.strip,str_lst))))

old = get_and_split_input_old("test.txt")
new = get_and_split_input("test.txt")
print("old:")
print(old)
print("new:")
print(new)
print(new == old)


lst = [1,2,3,4]
print(lst[1:])