<<<<<<< HEAD
""" Puzzle for dayX advent of code 2021
"""
# import numpy as np
import pandas as pd
# import math
# import re

# windows filepath
filename = '..\data\sample.txt'

# linux filepath
# filename = '../data/sample.txt'


# line read
with open(filename) as fn:
    lncount = 0
    ln = fn.readline()
    while ln:
        lint = int(ln)
        ln = fn.readline()

# Pandas read
colnames = ['data']
df = pd.read_csv(filename, header=None)
rows = df.shape[0]

# main if needed
# if __name__ == "__main__":
=======
""" Puzzle for day12 advent of code 2021
"""
from collections import defaultdict


def dfs(iter, end, visited, path_list, path, graph):
    global counter

    visited[iter] = 1
    path.append(iter)
    if iter.isupper():
        visited[iter] = 0
    if iter == 'end':
        counter += 1
        path_list.append(path)
        print(counter)
    else:
        for i in graph[iter]:
            if visited[i] == 0:
                dfs(i, end, visited, path_list, path, graph)
    path.pop()
    visited[iter] = 0


def read_input_data(filename):
    paths = []
    with open(filename) as fn:
        ln = fn.readline()
        while ln:
            ln = ln.strip("\n").split("-")
            paths.append(ln)
            ln = fn.readline()
    return paths


def build_tree_dict(path_list):
    element_list = []
    node_list = defaultdict(list)
    for i, j in path_list:
        element_list.append(i)
        element_list.append(j)
        if j != 'start':
            node_list[i] += [j]
        if i != 'start':
            node_list[j] += [i]
    element_list = sorted(set(element_list))
    return node_list, element_list


def initialize_dict(list):
    ret_dict = {}
    for i in list:
        ret_dict[i] = 0
    return ret_dict


# main if needed
if __name__ == "__main__":
    path_list = []
    counter = 0
    file = '..\data\data.txt'
    paths = read_input_data(file)
    node_list, element_list = build_tree_dict(paths)
    visited = initialize_dict(element_list)
    dfs(iter="start", end="end", visited=visited, path_list=path_list, path=[], graph=node_list)
>>>>>>> develop
