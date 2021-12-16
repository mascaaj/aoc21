""" Puzzle for day14 advent of code 2021
"""
from collections import Counter


# windows filepath
filename = '..\data\data.txt'


def read_file(file):
    key = {}
    with open(file) as fn:
        ln = fn.readline()
        data = ln.strip("\n")
        while ln:
            ln = fn.readline()
            ln = ln.strip("\n").split(" -> ")
            if len(ln) > 1:
                key[ln[0]] = ln[1]
            else:
                break
    return data, key


def update_string(string, string_key):
    new_kab = ''
    for i in range(len(string) - 1):
        hadi = string_key[string[i:i + 2]]
        new_kab = new_kab + string[i] + hadi
    return new_kab + string[-1]


# main if needed
if __name__ == "__main__":
    data, key = read_file(filename)
    # this method will not work, need to use histogram of pair occurances
    # new_string = update_string(data, key)
    # for i in range(9):
    #     new_string = update_string(new_string, key)
    # string_counts = Counter(new_string)
    # max_count = max(sorted(string_counts.values()))
    # min_count = min(sorted(string_counts.values()))
    # print(max_count - min_count)
