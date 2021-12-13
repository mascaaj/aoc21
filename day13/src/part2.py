""" Puzzle for day13 advent of code 2021
Solution has a bug, had to iteratively guess 2 alphabets
based on primitive shapes
"""
import numpy as np


# windows filepath
filename = '..\data\sample'
filename_instructions = filename + '_instructions'
punch_location = np.empty(0)
instructions = []


def file_read(file):
    punch_location = np.empty(0)
    lncount = 0
    with open(file + '.txt') as fn:
        ln = fn.readline()
        while ln:
            lncount += 1
            ln = ln.strip("\n")
            punch_location = np.append(punch_location, np.fromstring(ln, sep=",", dtype=int))
            ln = fn.readline()
        punch_location = punch_location.astype(int).reshape(lncount, 2)
        return punch_location


def file_read_instruction(file):
    instruction = []
    with open(file + '.txt') as fn:
        ln = fn.readline()
        while ln:
            ln = ln.strip("fold along ").strip("\n").split("=")
            instruction.append(ln)
            ln = fn.readline()
        return instruction


def update_pattern(location, grid):
    for i in location:
        grid[i[1], i[0]] = 1
    return grid


def fold_update(origami_state, instruction):
    if instruction[0] == 'x':
        if origami_state.shape[1] % 2 == 0:
            left_fold = origami_state[:, 0:int(instruction[1]) - 1]
        else:
            left_fold = origami_state[:, 0:int(instruction[1])]
        right_fold = np.flip(origami_state[:, int(instruction[1]) + 1:], 1)
        folded_origami = left_fold + right_fold
    elif instruction[0] == 'y':
        if origami_state.shape[0] % 2 == 0:
            top_fold = origami_state[0:int(instruction[1]) - 1, :]
        else:
            top_fold = origami_state[0:int(instruction[1]), :]
        bottom_fold = np.flip(origami_state[int(instruction[1]) + 1:, :], 0)
        folded_origami = top_fold + bottom_fold
    dot_count = np.where(folded_origami >= 1, '#', ' ')
    return folded_origami, dot_count


def join_characters(list_input):
    char_val = ''
    for i in list_input:
        char_val += i
    return char_val


if __name__ == "__main__":
    punch_location = file_read(filename)
    instructions = file_read_instruction(filename_instructions)
    origami = np.zeros((max(punch_location[:, 1]) + 1, max(punch_location[:, 0]) + 1))
    updated_origami = update_pattern(punch_location, origami)
    for i in instructions:
        updated_origami, dot_count = fold_update(updated_origami, i)
    for i in range(len(dot_count)):
        print(join_characters(dot_count[i].tolist()))
