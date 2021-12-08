""" Puzzle for day 8 advent of code 2021
"""
import numpy as np


# windows filepath
filename = '..\data\data.txt'
length_array = np.empty(0)

# line read
with open(filename) as fn:
    ln = fn.readline()
    signal_input = str.split(ln)
    while ln:
        lengths = [len(x) for x in signal_input[11:]]
        length_array = np.append(length_array, lengths)
        ln = fn.readline()
        signal_input = str.split(ln)
    length_array = length_array.reshape(length_array.shape[0] // 4, 4)
    sum1 = np.sum(np.where(np.logical_or(length_array == 2, length_array == 4), 1, 0))
    sum2 = np.sum(np.where(np.logical_or(length_array == 3, length_array == 7), 1, 0))
    print(sum1 + sum2)
