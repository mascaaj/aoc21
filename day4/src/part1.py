""" Puzzle for day4 advent of code 2021
"""
import numpy as np


# windows filepath
filename = '..\data\data.txt'
flag_bingo = 0
card_elements = 25
card_array = np.empty(0)
card_arr_nd = np.empty(0)


def test_grade(input):
    '''
    Checks row & col sums of input nd array
    '''
    row_sums = np.sum(input, axis=2)
    col_sums = np.sum(input, axis=1)

    # Test conditions
    if 5 in row_sums:
        return True
    elif 5 in col_sums:
        return True


# line read
with open(filename) as fn:
    ln = fn.readline()
    # Read the called out numbers, parse from string, cast as integer
    chosen_numbers = np.fromstring(ln, sep=",", dtype=int)
    while ln:
        ln = fn.readline()
        if ln == "\n":
            pass
        else:
            ln = ln.strip("\n")
            # append to initialized array, parse from string, cast as integer
            card_array = np.append(card_array, np.fromstring(ln, sep=" ", dtype=int))
    number_of_cards = int(card_array.size / card_elements)
    # reshape array as nd array
    card_arr_nd = card_array.reshape(number_of_cards, 5, 5)
    grader = np.zeros(np.shape(card_arr_nd))

    for i in chosen_numbers:
        # Find matching locations of elements in nd array
        locations = np.where(card_arr_nd == i)
        # Reformat from tuple to list
        loc_formatted = list(zip(*locations))
        for j in loc_formatted:
            # Flip found element value in the grader
            grader[j] = 1
            flag_bingo = test_grade(grader)
            if flag_bingo:
                break
        if flag_bingo:
            break

    negative = np.where(grader[j[0]] < 1, 1, 0)
    positive = card_arr_nd[j[0]]
    net = negative * positive
    print(i * np.sum(net))
