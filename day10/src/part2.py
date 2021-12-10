""" Puzzle for day10 advent of code 2021
"""
from collections import deque


# windows filepath
filename = '..\data\data.txt'
symbol_array = []
prize_array = []
prize_dict = {"<": 4, "(": 1, "[": 2, "{": 3}
ord_dict = {">": 60, ")": 40, "]": 91, "}": 123}


def convert_string_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


def evaluate_corrupt_syntax(input):
    stack = deque()
    for i in input:
        if i == "[" or i == "{" or i == "(" or i == "<":
            stack.append(i)
        else:
            if ord(stack.pop()) == ord_dict[i]:
                continue
            else:
                return i


def evaluate_completion_syntax(input):
    stack = deque()
    stack2 = deque()
    prize_total = 0
    for i in input:
        if i == "[" or i == "{" or i == "(" or i == "<":
            stack.append(i)
            stack2.append(i)
        elif ord(stack.pop()) == ord_dict[i]:
            stack2.pop()
            continue
        else:
            break
    while stack2:
        symbol = stack2.pop()
        prize_total = (prize_total * 5) + prize_dict[symbol]
    return prize_total


# line read
with open(filename) as fn:
    ln = fn.readline()
    while ln:
        ln = ln.strip("\n")
        symbol_array = convert_string_to_list(ln)
        if not evaluate_corrupt_syntax(symbol_array):
            prize_array.append(evaluate_completion_syntax(symbol_array))
        ln = fn.readline()
print(sorted(prize_array)[int(len(prize_array) // 2)])
