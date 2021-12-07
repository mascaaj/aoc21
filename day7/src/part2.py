""" Puzzle for day7 advent of code 2021
"""
import numpy as np


# windows filepath
filename = '..\data\sample.txt'
crab_ic = np.empty(0)
crab_corrected = np.empty(0)
crab_step_sum = np.empty(0)

# line read
with open(filename) as fn:
    ln = fn.readline()
    crab_ic = np.append(crab_ic, np.fromstring(ln, sep=",", dtype=int))

    for i in range(int(crab_ic.min()), int(crab_ic.max())):
        # Calculate steps
        crab_steps = abs(crab_ic - i)+1
        step_sums = np.empty(0)
        for j in crab_steps:
            # Use arange to get np array of 0:steps, calculate sum
            step_sums = np.append(step_sums, int(np.sum(np.arange(j))))
        # sum up step_sums array
        crab_step_sum = np.append(crab_step_sum, np.sum(step_sums))
    print(int(crab_step_sum.min()))
