# from token_types import token_types
# import functools
# print(token_types.OPERATOR_PLUS)
# def get_and_split_input_old(fname : str)->str:
#     infile = open(fname,'r')
#     input_str = infile.read()
#     str_lst = input_str.split("\n")
#     for row in str_lst:
#         if row.strip() == '':
#             str_lst.remove(row)
#     input_lst = []
#     for item in str_lst:
#         input_lst.append(item.strip().split(" "))
#     return input_lst

# def get_and_split_input(fname : str)->str:
#     infile = open(fname,'r')
#     input_str = infile.read()
#     str_lst = input_str.split("\n")
#     str_lst = list(filter(None,str_lst))
#     return list(map(str.split,list(map(str.strip,str_lst))))

# old = get_and_split_input_old("test.txt")
# new = get_and_split_input("test.txt")
# print("old:")
# print(old)
# print("new:")
# print(new)
# print(new == old)

# lst = [1,2,3,4]
# print(lst[1:])

# import sys
# import threading

# class SomeCallable:
#     def __call__(self):
#         try:
#             self.recurse(99900)
#         except RecursionError:
#             print("Booh!")
#         else:
#             print("Hurray!")
#     def recurse(self, n):
#         if n > 0:
#             self.recurse(n-1)



# # recurse in greedy thread
# sys.setrecursionlimit(100000)
# threading.stack_size(0x2000000)
# t = threading.Thread(target=SomeCallable())
# t.start()
# t.join()

lst = [[(1,2),(10,50)],[5,6],[2,1]]

def combine_list(lst):
    if len(lst) < 1:
        return lst
    a, *tail = lst
    return a + combine_list(tail)

print(combine_list(lst))

from nodes import *

from token_types import token_types
for item in token_types:
    print(item.__name__)
print(list(map(lambda item: item.__name__,token_types)))
print(token_types["OPERATOR_PLUS"].value)
test = node()
print(test)

for item in token_types:
    print(item)
# print(functools.reduce(lambda a,b: a if a>b else b ,lst))