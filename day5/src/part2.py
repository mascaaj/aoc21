""" Puzzle for day5 advent of code 2021
"""
import numpy as np


# windows filepath
filename = '..\data\data.txt'
input_data = np.empty(0)
orthogonal_data = np.empty(0)

# line read
with open(filename) as fn:
    lncount = 0
    ln = fn.readline()
    while ln:
        lncount += 1
        ln = ln.replace(" -> ", ",")
        input_data = np.append(input_data, np.fromstring(ln, sep=",", dtype=int))
        ln = fn.readline()
    input_data_formatted = input_data.reshape(lncount, 2, 2)
    # need to do this because it does not mention maps always being symmetric
    interim_format = input_data.reshape(lncount*2, 2)
    map_size = tuple(np.max(interim_format, axis=0))
    map_floor = np.zeros((int(map_size[0])+1, int(map_size[1])+1))
    orthogonal_data = input_data_formatted

    # There must be a better way to approach this, need to study and reimplement
    for i in input_data_formatted:
        if i[0][1] == i[1][1]:
            # y's are same, horizontal
            if int(i[0][0]) < int(i[1][0]):
                for k in range(int(i[0][0]), int(i[1][0]) + 1):
                    map_floor[int(i[0][1]), k] += 1
            else:
                for k in range(int(i[0][0]), int(i[1][0] - 1), -1):
                    map_floor[int(i[0][1]), k] += 1
        elif i[0][0] == i[1][0]:
            # x's are same, vertical
            if int(i[0][1]) < int(i[1][1]):
                for k in range(int(i[0][1]), int(i[1][1] + 1)):
                    map_floor[k, int(i[1][0])] += 1
            else:
                for k in range(int(i[0][1]), int(i[1][1] - 1), -1):
                    map_floor[k, int(i[1][0])] += 1
        else:
            # must have diagonals
            if int(i[0][0]) < int(i[1][0]):
                if int(i[0][1]) < int(i[1][1]):
                    for k, p in zip(range(int(i[0][0]), int(i[1][0]) + 1),
                                    range(int(i[0][1]), int(i[1][1]) + 1)):
                        map_floor[p, k] += 1
                else:
                    for k, p in zip(range(int(i[0][0]), int(i[1][0]) + 1),
                                    range(int(i[0][1]), int(i[1][1]) - 1, -1)):
                        map_floor[p, k] += 1
            else:
                if int(i[0][1]) < int(i[1][1]):
                    for k, p in zip(range(int(i[0][0]), int(i[1][0]) - 1, -1),
                                    range(int(i[0][1]), int(i[1][1]) + 1)):
                        map_floor[p, k] += 1
                else:
                    for k, p in zip(range(int(i[0][0]), int(i[1][0]) - 1, -1),
                                    range(int(i[0][1]), int(i[1][1]) - 1, -1)):
                        map_floor[p, k] += 1

    locations = np.where(map_floor >= 2, 1, 0)
    print(np.sum(locations))
