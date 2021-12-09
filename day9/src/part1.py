""" Puzzle for dayX advent of code 2021
"""
import numpy as np

# windows filepath
filename = '..\data\data.txt'
input_map = np.empty(0)


def convert_string_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


def test_min(input):
    low_point_array = []
    for i in range(input.shape[0]):
        for j in range(input.shape[1]):
            flag = 0
            tv = input[i, j]
            t1, t2, t3, t4 = -1, -1, -1, -1
            if i - 1 >= 0:
                t1 = input[i - 1, j]
            if i + 1 < input.shape[0]:
                t2 = input[i + 1, j]
            if j - 1 >= 0:
                t3 = input[i, j - 1]
            if j + 1 < input.shape[1]:
                t4 = input[i, j + 1]

            test_list = [tv, t1, t2, t3, t4]
            if test_list.count(-1) > 0:
                test_list.remove(-1)
                if test_list.count(-1) > 0:
                    test_list.remove(-1)
            for j in range(1, len(test_list)):
                if test_list[0] >= test_list[j]:
                    flag = 1
            if flag == 0:
                low_point_array.append(test_list[0])
    return(low_point_array)


# line read
with open(filename) as fn:
    lncount = 0
    ln = fn.readline()
    while ln:
        ln = convert_string_to_list(ln.strip("\n"))
        lnwidth = len(ln)
        input_map = np.append(input_map, ln)
        ln = fn.readline()
        lncount += 1
    input_map = input_map.astype(int).reshape(lncount, lnwidth)
    location = np.array(test_min(input_map)) + 1
    print(location.sum())
