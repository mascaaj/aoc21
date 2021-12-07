""" Puzzle for day7 advent of code 2021
"""
import numpy as np


# windows filepath
filename = '..\data\data.txt'
crab_ic = np.empty(0)
crab_corrected = np.empty(0)

# line read
with open(filename) as fn:
    ln = fn.readline()
    crab_ic = np.append(crab_ic, np.fromstring(ln, sep=",", dtype=int))

    for i in range(int(crab_ic.min()), int(crab_ic.max())):
        crab_corrected = np.append(crab_corrected, sum(abs(crab_ic - i)))
    print(int(crab_corrected.min()))
