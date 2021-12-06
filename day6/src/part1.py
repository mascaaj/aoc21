""" Puzzle for day6 advent of code 2021
"""
import numpy as np

# windows filepath
filename = '..\data\sample.txt'


def age(input):
    # decrement age
    return input - 1


def multiply(fish):
    # identify fish spawned, reset parent clock, start spawn clock
    ripe = np.sum(fish < 0)
    if ripe > 0:
        fish = np.where(fish == -1, 6, fish)
        new_fish = np.ones(ripe, dtype=int) * 8
        fish = np.append(fish, new_fish)
    return fish


# line read
with open(filename) as fn:
    ln = fn.readline()
    input_array = np.fromstring(ln, sep=",", dtype=int)
    # iterate thru days
    for i in range(0, 80):
        input_array = multiply(age(input_array))
    print(input_array.size)
