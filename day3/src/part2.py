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

    df1 = df_numeric
    df2 = df_average
    df3 = df_round

# O2 calculations
    for i in range(0, 12):
        if df2[i] == 0.500000:
            df1 = df1.drop(df1.loc[df1[i] != 1].index)
        else:
            df1 = df1.drop(df1.loc[df1[i] != df3[i]].index)
        df2 = df1.sum(axis=0) / len(df1.axes[0])
        df3 = df2.apply(round, 0)
        print(df1)
        print("Column Number", i)
        print(df2)
        print("***********")

    df1 = df_numeric
    df2 = df_average
    df3 = df_round

# Co2 calculations
    for i in range(0, 9):
        if df2[i] == 0.50000:
            df1 = df1.drop(df1.loc[df1[i] != 0].index)
        else:
            df1 = df1.drop(df1.loc[df1[i] == df3[i]].index)
        df2 = df1.sum(axis=0) / len(df1.axes[0])
        df3 = df2.apply(round, 0)
        print(df1)
        print("Column Number", i)
        print(df2)
        print("***********")

# 0   1   1   1   1   1   0   1   1   0   1   1   1
# 216   0   0   1   0   1   0   1   1   0   0   1   0
    oxygen = int(str(111110110111), 2)
    co2 = int(str(1010110010), 2)
    print(oxygen * co2)
