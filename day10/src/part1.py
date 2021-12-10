""" Puzzle for day10 advent of code 2021
"""
from collections import deque

# windows filepath
filename = '..\data\data.txt'
symbol_array = []
corrupt_array = []
prize_dict = {">": 25137, ")": 3, "]": 57, "}": 1197}
ord_dict = {">": 60, ")": 40, "]": 91, "}": 123}


def convert_string_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


def evaluate_syntax(input):
    stack = deque()
    for i in input:
        if i == "[" or i == "{" or i == "(" or i == "<":
            stack.append(i)
        else:
            if ord(stack.pop()) == ord_dict[i]:
                continue
            else:
                return i


# line read
with open(filename) as fn:
    ln = fn.readline()
    while ln:
        ln = ln.strip("\n")
        symbol_array = convert_string_to_list(ln)
        corrupt_array.append(evaluate_syntax(symbol_array))
        ln = fn.readline()
corrupt_array = list(filter(None, corrupt_array))
prize_array = [prize_dict[x] for x in corrupt_array]
print(sum(prize_array))
