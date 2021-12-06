""" Puzzle for day6 advent of code 2021
"""
import numpy as np

# windows filepath
filename = '..\data\data.txt'

# line read
with open(filename) as fn:
    ln = fn.readline()
    input_array = np.fromstring(ln, sep=",", dtype=int)
    # Max count is 10, calculate histogram
    hist_fish = np.histogram(input_array, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])[0]
    # initialize spawn fish value
    new_fish = hist_fish[0]
    # iterate thru days
    for i in range(0, 256):
        # set spawn clock
        hist_fish[9] = new_fish
        # reset parent clock
        hist_fish[7] = hist_fish[7] + new_fish
        # shift array to left (frequency domain)
        hist_fish[0:9] = hist_fish[1:10]
        # capture spawn count
        new_fish = hist_fish[0]
    print(sum(hist_fish[0:9]))
