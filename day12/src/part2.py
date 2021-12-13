""" Puzzle for day12 advent of code 2021
"""
from collections import defaultdict


def dfs(iter, end, visited, path_list, path, graph, flag):
    global counter
    global double
    # visited[iter] = 1
    path.append(iter)
    if iter != 'start' and iter != 'end':

        if iter.islower() and flag < 1:
            visited[iter] = 0
            flag = 1
            double.append(iter)
            print(iter)
        elif iter.isupper():
            visited[iter] = 0
        else:
            visited[iter] = 1
    if iter == 'end':
        counter += 1
        flag = 0
        path_list.append(path)
        print(counter)
    else:
        for i in graph[iter]:
            if visited[i] == 0:
                dfs(i, end, visited, path_list, path, graph, flag)
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
    double = []
    counter = 0
    file = '..\data\sample3.txt'
    paths = read_input_data(file)
    node_list, element_list = build_tree_dict(paths)
    visited = initialize_dict(element_list)
    dfs(iter="start", end="end", visited=visited, path_list=path_list, path=[], graph=node_list, flag=0)
    print(double)