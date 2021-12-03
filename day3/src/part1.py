""" Puzzle for day3 advent of code 2021
"""
import pandas as pd

# windows filepath
filename = '..\data\data.txt'

# line read
with open(filename) as fn:
    ln = fn.readline()
    ln = ln.strip('\n')
    simple_list = [list(ln)]
    while ln:
        ln = fn.readline()
        ln = ln.strip('\n')
        simple_list.append(list(ln))
    df = pd.DataFrame(simple_list)
    df.drop(df.tail(1).index, inplace=True)

    df_numeric = df.apply(pd.to_numeric)
    df_average = df_numeric.sum(axis=0)/len(df_numeric.axes[0])
    df_round = df_average.apply(round, 0)
    print(df_round)

    gamma = int(str(110010111011), 2)
    epsilon = int(str(1101000100), 2)
    print(gamma*epsilon)
