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
