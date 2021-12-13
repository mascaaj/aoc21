""" Puzzle for dayX advent of code 2021
"""
import numpy as np


# windows filepath
filename = '..\data\data'
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
        left_fold = np.flip(origami_state[:, 0:int(instruction[1])], 1)
        right_fold = origami_state[:, int(instruction[1]) + 1:]
        folded_origami = left_fold + right_fold
        print("folded origami left", folded_origami)
    else:
        top_fold = origami_state[0:int(instruction[1]), :]
        bottom_fold = np.flip(origami_state[int(instruction[1])+1:, :], 0)
        folded_origami = top_fold + bottom_fold
        print("folded origami bottom", folded_origami)
    dot_count = np.where(folded_origami >= 1, 1, 0).sum()
    return folded_origami, dot_count


if __name__ == "__main__":
    punch_location = file_read(filename)
    instructions = file_read_instruction(filename_instructions)
    origami = np.zeros((max(punch_location[:, 1]) + 1, max(punch_location[:, 0]) + 1))
    updated_origami = update_pattern(punch_location, origami)
    folded_origami, dot_count = fold_update(updated_origami, instructions[0])
    print(dot_count)
